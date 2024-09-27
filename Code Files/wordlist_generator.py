#!/usr/bin/env python

import subprocess

def wordlist_generator():
	want_pattern = input("\033[1;32mDo you want to speify a pattern? [y/n]: \033[0m")
	if want_pattern == "y":
		pattern = input("\033[1;32mEnter your pattern where '@' denotes blank spaces: \033[0m")
		length = len(pattern)
		min = str(length)
		max = str(length)
	else:
		min = input("\033[1;32mEnter minimum word length: \033[0m")
		max = input("\033[1;32mEnter mamimum word length: \033[0m")
	character_list = input("\033[1;32mEnter characters you want in your word list: \033[0m")
	output_file = input("\033[1;32mEnter the wordlist file-name: \033[0m")
	if want_pattern == "y":
		subprocess.run(["crunch", min, max, character_list, "-o", output_file, "-t", pattern])
	else:
		subprocess.run(["crunch", min, max, character_list, "-o", output_file])

wordlist_generator()