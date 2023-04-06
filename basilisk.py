#!/usr/bin/env python3


#
#                    BASILISK
#
#                      _/
#                   __~a~_/
#                   ~~;  ~_/
#     _                ~  ~_/                _
#    '_\;__._._._._._._]   ~_._._._._._.__;/_'
#    '(/'/'/'/'|'|'|'| (    )|'|'|'|'\'\'\'\)'
#    (/ / / /, | | | |(/    \) | | | ,\ \ \ \)
#   (/ / / / / | | | ^(/    \) ^ | | \ \ \ \ \)
#  (/ / / / /  ^ ^ ^   (/  \)    ^ ^  \ \ \ \ \)
# (/ / / / ^           /(||)\          ^ \ \ \ \)
# ^ / / ^             M /||\ M            ^ \ \ ^
#  ^ ^                  /||\                 ^ ^
#                      //||\\
#                      //||\\
#                      //||\\
#                      '/||\'
#


import sys


alphabet = [
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z'
           ]
alphebet = [
                'x', 'e', 'o', 'y', 'z', 'k', 'n', 't', 'b', 'c',
                'v', 'i', 'r', 's', 'w', 'q', 'a', 'd', 'l', 'u',
                'j', 'f', 'g', 'm', 'h', 'p'
           ]


def key(keyword):

	characters = [*keyword]
	numbers = []

	for x in range(7):
		for character in characters:
			x = characters.index(character)  # this letter in the keyword
			a = alphabet.index(character)  # this letter's index in the alphabet
			try:
				y = characters[x + 1]  # the next letter in the keyword
			except(Exception) as e:
				y = characters[0]  # the next letter in the keyword
			b = alphabet.index(y)  # the next letter's index in the alphabet
			numbers.append(str(abs(a - b)))

	key = str(''.join(numbers))  # like teeth on a key
	return key


def encode(message, keyword):

	sequence = key(keyword)
	characters = [*message]
	transpositions = [*sequence]
	results = []

	for index, character in enumerate(characters):
		position = alphabet.index(character)
		transposition = int(transpositions[index])
		x = alphebet[position + transposition]
		results.append(x)

	return str('').join(results)


def decode(codetxt, keyword):

	sequence = key(keyword)
	characters = [*codetxt]
	transpositions = [*sequence]
	results = []

	for index, character in enumerate(characters):
		position = alphebet.index(character)
		transposition = int(transpositions[index])
		x = alphabet[position - transposition]
		results.append(x)

	return str('').join(results)


if __name__ == '__main__':

	if sys.argv[1] == 'encode':
		print(encode(sys.argv[2], sys.argv[3]))

	if sys.argv[1] == 'decode':
		print(decode(sys.argv[2], sys.argv[3]))
