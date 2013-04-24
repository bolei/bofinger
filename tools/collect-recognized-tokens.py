#!/usr/bin/python
import fileinput

def main():
	notRecog = set([])
	for line in fileinput.input():
		line = line.strip()
		if(line != "" and line.endswith("+?")):
			notRecog.add(line.split()[0])

	for item in notRecog:
		print item

if __name__ == "__main__":
	main()
