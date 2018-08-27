import os
import jsonlist
from vocab import Vocab

SENT_START = "<sentence_start>"
SENT_END = "<sentence_end>"

def create_speechtexts():

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

    return speechtexts

def create_sets(part):
    """ Gets the dataset for 'part' being train|test|valid. """
    speechtexts = create_speechtexts()
    if part == "train":
        return speechtexts[0:int(0.85 * len(speechtexts))]
    elif part == "valid":
        return speechtexts[int(0.85 * len(speechtexts)):int(0.9 * len(speechtexts))]
    else:
        return speechtexts[int(0.9 * len(speechtexts)):]

def load(speech_data, index):
    """ Loads the wikitext2 data at the given path using
    the given index (maps tokens to indices). Returns
    a list of sentences where each is a list of token
    indices.
    """
    start = index.add(SENT_START)
    sentences = []
    for paragraph in speech_data:
        for sentence in paragraph.split(" . "):
            tokens = sentence.split()
            if not tokens:
                continue
            sentence = [index.add(SENT_START)]
            sentence.extend(index.add(t.lower()) for t in tokens)
            sentence.append(index.add(SENT_END))
            sentences.append(sentence)

    return sentences


def main():
    print("Debate Speech preprocessing and dataset statistics")
    index = Vocab()
    for part in ("train", "valid", "test"):
        print("Processing", part)
        sentences = load(create_sets(part), index)
        print("Found", sum(len(s) for s in sentences),
              "tokens in", len(sentences), "sentences")
    print("Found in total", len(index), "tokens")


if __name__ == '__main__':
    main()
