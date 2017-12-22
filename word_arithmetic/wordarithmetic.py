'''
CLI tool to do arithmetic with words
Basics:
	- call wordarithmetic.py with a string of words followed by either a '+' or '-' to
		sum the embeddings of the words to return an 'answer' word.

How to Use:
	- install dependencies (scipy, argparse, inflect, numpy)
	- download one of the JSON wordMap files. EX. 'wordMap200d.json'
	- call script: 'python3 wordarithmetic.py 
		--equation [EX. 'berlin+germany-america'] 
	- for help: 'python3 wordarithmetic.py --help' 
'''
import json
import numpy as np
from scipy import spatial
import time
import argparse
import re
import inflect


'''
private helper _create_args()
------------------------------
Sets up CLI with one input: --equation. --equation should be a string 
of words with '+' or '-' in between words. No spaces.
EX. 'berlin+germany-america'

Input
	Void
Output 
	Void
'''
def _create_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("--equation", help="--equation should be a string \
		of words with '+' or '-' in between words. No spaces.", type=str, required=True)

	args = parser.parse_args()
	return args

'''
private helper _process_args(equation)
------------------------------
Pass in raw --equation string and returns an ordered list of words and list of operations

Input
	equation 	- raw string of words and operations 
Output 
	tokens 		- list of words in order they appear 
	operations	- list of operations in order they appear 
'''
def _process_args(equation):
	tokens = re.split('[\+\-]', equation)
	operations = re.sub("[a-zA-Z_]", "", equation)

	return(tokens,operations)
	
'''
private helper _read_wordMap()
------------------------------
Reads in the wordMap and returns it as a dict

Input
	verbose 	- default False
Output 
	wordMap 	- dict of words to their embeddings
'''
def _read_wordMap(verbose=False):
	file_name = "wordMap200d.json"
	wordMap = open(file_name,'r').read()
	if verbose:
		print("JSON read: {}".format(time.time()-start_time))
	wordMap = json.loads(wordMap)
	if verbose:
		print("JSON loaded: {}".format(time.time()-start_time))
	return wordMap

'''
function create_sum_words(tokens, operations, wordMap)
------------------------------
Pass in tokens, operations, and wordMap. Return the summed embedding.

Input
	tokens 		- list of words in order they appear 
	operations	- list of operations in order they appear 
	wordMap 	- dict of words to their embeddings
	verbose		- default False
Output 
	sumWord 	- summed embedding 
'''
def create_sum_words(tokens, operations, wordMap, verbose=False):
	sumWord = np.array(wordMap[tokens[0]])
	for i,op in enumerate(operations):
		if op == "+": 
			sumWord += np.array(wordMap[tokens[i+1]]) 
		else:
			sumWord += -1*(np.array(wordMap[tokens[i+1]]))
	if verbose:
		print("sumWord created: {}".format(time.time()-start_time))

	return sumWord

'''
function find_most_similar(num, sumWord, wordMap)
------------------------------
Pass in number of words to return the summed embedding and wordMap. Returns the top num most 
similar words to sumWord in wordMap

Input
	num 		- number of most similar words to return
	sumWord 	- summed embedding
	wordMap 	- dict of words to their embeddings
	verbose		- default False
Output 
	mostSimilar - list of length num of the most similar words to sumWord
'''
def find_most_similar(num, sumWord, wordMap, verbose=False):
	vectors = np.array(list(wordMap.values()))
	words = list(wordMap.keys())

	ranks = np.dot(sumWord,vectors.T)/np.sqrt(np.sum(vectors**2,1))
	if verbose:
		print("Vectorized COSINE: {}".format(time.time()-start_time))

	mostSimilar = []
	[mostSimilar.append(words[idx]) for idx in ranks.argsort()[-num:][::-1]]
		
	return mostSimilar

'''
private helper _remove_redundencies(mostSimilar, tokens)
------------------------------
Pass in the top num most similar words and tokens. Removes redundent words from mostSimilar

Input
	mostSimilar - list of length num of the most similar words to sumWord
	tokens		- list of words in order they appear 
Output 
	mostSimilar - list of length finalNum of the most similar words to sumWord
'''
def _remove_redundencies(mostSimilar, tokens, finalNum):
	engine = inflect.engine()
	mostSimilarCopy = mostSimilar
	for word in tokens:
		if word in mostSimilar:
			mostSimilar.remove(word)
		plural = engine.plural(word)
		if plural in mostSimilar:
			mostSimilar.remove(plural)

	return mostSimilar[:finalNum]


if __name__ == '__main__':
	global start_time
	start_time = time.time()

	args = _create_args()
	tokens, operations = _process_args(args.equation)
	wordMap = _read_wordMap(verbose=True)
	sumWord = create_sum_words(tokens,operations, wordMap, verbose=True)
	mostSimilar = find_most_similar(len(tokens)+7, sumWord, wordMap, verbose=True)
	mostSimilar = _remove_redundencies(mostSimilar, tokens, 5)
	print(mostSimilar)





'''
Stupid weighting
----------------------------------
	- Search each individual word 
	- Search the sumWord
	- Weight each word that is being summed by how many times their synonyms show up in the sumWord search
EX:
if we add solder + iron we see that the results for the sum is 
	- iron
	- solder
	- metal
	- zinc
	- copper
	- molten
	- pipe
if we look up just solder we get 
	- solder
	- soldering
	- tapioca
	- lead-free
	- pyrolysis
	- hammerfall
	- sintered
if we look up just iron we get 
	- iron
	- steel
	- metal
	- copper
	- zinc
	- pipe
	- aluminum

We can see that results for sumWord is heavily influenced by "iron"
In fact we can see 5 of the 7 results comes from iron. So we weight iron by 2/7 and we 
weight solder by 5/7

We get 
	- solder
	- soldering
	- molten
	- pyrite
	- tapioca
	- metal
	- ores

Which is qualitatively more similar to what we expect
'''