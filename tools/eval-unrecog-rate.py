#!/usr/bin/python

import fileinput

def main():
	wordTypes = {}
	unrecgnizedWordTypeCount = 0
	tokenCount = 0
	unrecognizedWordTokenCount = 0
	for line in fileinput.input():
		if(line.strip() == ""):
			tokenCount+=1	
			continue
		items = line.strip().split()
		if(items[1]=="+?"):
			unrecognizedWordTokenCount += 1

		#new word type
		if(wordTypes.has_key(items[0]) == False):
			wordTypes[items[0]]=''
			if(items[1]=="+?"):
				unrecgnizedWordTypeCount+=1
	
	print "word type count:"
	print str(len(wordTypes))	
	print "word type recognition rate:"
	print str(float(len(wordTypes) - unrecgnizedWordTypeCount)/float(len(wordTypes)))
	
	print "============"
	print "word token count:"
	print str(tokenCount)
	print "word token recognition rate:"
	print str(float(tokenCount - unrecognizedWordTokenCount)/float(tokenCount))

if __name__ == "__main__":
	main()
