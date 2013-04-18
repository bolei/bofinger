#!/usr/bin/python

import fileinput

def main():
	wordRecord = {}
	totalWordCount = 0
	unrecgnizedWordCount = 0
	for line in fileinput.input():
		if(line.strip() == ""):
			continue
		items = line.strip().split()
		if(wordRecord.has_key(items[0]) == False):
			wordRecord[items[0]]=''
			totalWordCount+=1
			if(items[1]=="+?"):
				unrecgnizedWordCount+=1
	
	print "word type count:"
	print str(totalWordCount)	
	print "recognition rate:"
	print str(float(totalWordCount - unrecgnizedWordCount)/float(totalWordCount))
		

if __name__ == "__main__":
	main()
