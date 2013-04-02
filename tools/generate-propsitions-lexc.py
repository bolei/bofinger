#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import sys

def main():
	f = codecs.open(sys.argv[1], "r", "utf-8")
	line = f.readline()
	while line!="":
		if not isinstance(line, unicode):
			line = line.decode('utf-8') # assumes using UTF-8
		print u"{0}+Prep:{0}\t#;".format(line.strip())
		line = f.readline()

if __name__ == "__main__":
	main()
