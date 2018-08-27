Presidential debate quotes dataset v1.0 (released February 2018)

Distributed together with:

Chenhao Tan, Hao Peng, and Noah A. Smith.
"You are no Jack Kennedy": On Media Selection of Highlights from Presidential Debates.
In Proceedings of The Web Conference (WWW), 2018.

The paper, data, and associated materials can be found at:
http://chenhaot.com/papers/debate-quotes.html

If you use this dataset, please cite

@inproceedings{tan+peng+smith:18, 
    author = {Chenhao Tan and Hao Peng and Noah A. Smith}, 
    title = {``You are no Jack Kennedy'': On Media Selection of Highlights from Presidential Debates}, 
    year = {2018}, 
    booktitle = {Proceedings of WWW} 
}

=================

The dataset includes:

1. debate_speech.jsonlist contains debate speeches as a jsonlist, and each line represents a debate with structure:

	- 'url': url of the debate html page, used as an unique identifier
	- 'speeches': speeches in each debate (we use turn and speech interchangably in this file):
		- 'speaker': speaker of the speech
		- 'text': speech text
    	- 'tokenized_text': tokenized text, sentences are separated by '\n'
    	- 'quoted': a list of integers, indicating the number of quotes for each sentence

2. meta_debates.jsonlist contains auxiliary information to each debate, i.e., date and debate information:
	
	- 'url': url of the debate html page, used as an unique identifier
	- 'date': date of the debate
	- 'name': debate name/type

3. quotes.jsonlist consists of all the quotes. Each line represents a quote:

    - 'quote': the quote text
	- 'news_name': newspaper name
    - 'news_headline': the first three lines in the original news article, can be used to search for the original text. We do not release the full text for copy right reasons.
	- 'news_date': the release data of the corresponding news article
	- 'debate_url': url of the debate html page, used as an unique identifier
    - 'debate_name': debate name as in meda_debates.jsonlist
    - 'debate_date': date of the debate
    - 'speaker': speaker of the matched turn in the debate
    - 'speech_index': speech index of the matched turn in the debate

4. train_pairs.jsonlist/heldout_pairs.jsonlist contain the train/test split. Each line represents a pair of sentences as a list, including

	- a debate url identifier
	- count of quotes of the highlighted sentence
	- speech index of the highlighted sentence
	- speaker of the highlighted sentence
	- index of the highlighted sentence within the speech
	- highlighted sentence
	- speech index of the not-highlighted sentence
	- speaker of the not-highlighted sentence
	- index of the not-highlighted sentence within the speech
	- not-highlighted sentence

