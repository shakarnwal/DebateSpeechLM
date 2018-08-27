import jsonlist
from nltk.tokenize import word_tokenize
from collections import Counter, defaultdict
from nltk import trigrams
from math import exp, log
from vocab import Vocab
import data_loader

infile = jsonlist.load_file('debate_speech.jsonlist')

speechtexts = []
for i in range(0, len(infile)):
    for j in range(0, len(infile[i]['speeches'])):
        speechtexts.append(infile[i]['speeches'][j]['text'])

for i in range(0, len(speechtexts)):
    speechtexts[i] = speechtexts[i].replace("\n","")
    speechtexts[i] = speechtexts[i].replace(","," ,")
    speechtexts[i] = speechtexts[i].replace("."," . ")
    speechtexts[i] = speechtexts[i].replace("?"," ? ")
    speechtexts[i] = speechtexts[i].replace("--"," -- ")
    speechtexts[i] = speechtexts[i].replace(";"," ; ")
    speechtexts[i] = speechtexts[i].replace("\'","'")
    speechtexts[i] = speechtexts[i].replace("(","( ")
    speechtexts[i] = speechtexts[i].replace(")"," )")
    speechtexts[i] = speechtexts[i].replace("[","[ ")
    speechtexts[i] = speechtexts[i].replace("]"," ]")    
    
speechtokenize = []
for i in range(0, len(speechtexts)):
    speechtokenize.append(word_tokenize(speechtexts[i]))
    
training = speechtokenize[0:int(0.9 * len(speechtokenize))]
testing = speechtokenize[int(0.9 * len(speechtokenize)):]

trigram_model = defaultdict(lambda: defaultdict(lambda:0))
total_counts = defaultdict(lambda: defaultdict(lambda:0))

for i in range(0, len(training)):
    for w1, w2, w3 in trigrams(training[i], pad_left = True, pad_right=True):
        trigram_model[(w1,w2)][w3] += 1

for w1_w2 in trigram_model:
    total_count = float(sum(trigram_model[w1_w2].values()))
    for w3 in trigram_model[w1_w2]:
        total_counts[w1_w2][w3] += total_count        
        
unique_vals = []
for i in range(0, len(training)):
    for w in training[i]:
        if (w.lower() not in unique_vals) and (w.lower().isalpha() == True):
            unique_vals.append(w.lower())

ct = 0
logprob = 0.0
k = 0.01
V = int(len(unique_vals)/10)
prob_count = []

for i in range(0, len(testing)):
    
    textgen = [None, None]
    ct = 0
    logprob = 0.0
    for word in testing[i]:
        textgen.append(word)
        logprob += log((trigram_model[tuple(textgen[-2:])][word] + k) / (total_counts[tuple(textgen[-2:])][word] + k * V))
        ct += 1
    prob_count.append([logprob, ct])

ct1 = 0
pp = 0
for i in range(0, len(prob_count)):
    if (prob_count[i][0] > -745 and prob_count[i][0] != 0.0):
        temp = exp(prob_count[i][0])
        pp += temp ** ((-1)/prob_count[i][1])
        ct1 += 1

perplexity = pp/ct1

print ("The perplexity of the model is ->")
print (perplexity)

