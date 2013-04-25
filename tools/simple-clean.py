#!/usr/bin/python
# -*- coding: utf-8 -*-
import fileinput
import re

_digits = re.compile('\d')
def contains_digits(d):
    return bool(_digits.search(d))

def main():
	for line in fileinput.input():
		word = line.strip()
		if word != "" and len(word) > 1 and len(word.split()) == 1 and (word.isalpha() or word.find('.') == -1) and contains_digits(word) == False and not word.endswith("ment"):
			print word

if __name__ == "__main__":
	main()
