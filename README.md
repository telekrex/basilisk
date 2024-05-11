<div align="center">
  <img src="docs/Basilisk-Grayscale.svg" height="200"/>
</div>
<h1 align="center" style="margin-top: -10px"> Basilisk </h1>
<p align="center" style="width: 100;">
   Text encryption cipher.<br>
</p>

## Getting Started
The only requirement is an installation of Python 3.
1. Clone or download this repository.
2. If you want to create a binary for this, see #compiling. Otherwise, you're good to go.

## How to Use
Basilisk can encrypt or decrypt plain text. It uses a key to generate the sequence it will use to transpose and encrypt the text, so you'll need to come up with a key (think of it like a password) for whatever you're going to encrypt. To decrypt, just like a login, you'll need to provide the key. 

Important: Use alphabet characters only. No symbols or numbers. Spaces can be used, but just for clarity on the human end really; they will not count as a character, they will be omitted. Personally I reccommend using a phrase for a key, instead of a word. Examples of good keys would be something like "weliveinatwilightworld" or "andtherearenofriendsatdusk".

From within the directory that basilisk is in, run the program from a terminal with the following arguments:
1. `encrypt` or `decrypt`
2. The text you are encrypting or decrypting
3. The key

Examples:  
Encrypting: `python basilisk.py encrypt mysecretcontents supersecretkey`  
Decrypting: `python basilisk.py decrypt wiogsjgioeagnagd supersecretkey` 

## Compiling
`basilisk.py` is fully functional as is without installing anything other than python, but if you really want a binary, I would suggest installing [PyInstaller](https://pyinstaller.org/en/stable/installation.html) and running `python -m PyInstaller --onefile basilisk.py`. This would make sense if you have a device where you want basilisk, but not python.

## Credits
Orignal work written by telekrex. Please direct any suggestions, questions, or suspected security vulnerabilities to telekrex@gmail.com.