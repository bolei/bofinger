#!/usr/bin/python
# -*- coding: utf-8 -*-
import fileinput

ignorelist = ('!', '-', '_', '(', ')', ',', '.', ':', ';', '"', '\'', '?')

def displayword(w):
	if w != "":
		print w
#		print w.lower()

def handletail(w):
#	print w
	if(w == ""):
		return
	if(ignorelist.count(w[len(w)-1]) > 0):
		handletail(w[0:len(w)-1])
		displayword(w[len(w)-1])
	else:
		displayword(w[0:len(w)])

def handleword(w):
	if(w[0] in ignorelist):
		displayword(w[0])
		w = w[1:len(w)]
	pos = w.find('\'')
	if(pos >= 0):
		displayword(w[0:pos+1])
		w = w[pos+1:len(w)]
	handletail(w)

def main():
	for line in fileinput.input():
		words = line.split()
		for w in words:
			handleword(w)

if __name__ == "__main__":
	main()
#	handletail('abc...')
