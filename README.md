# Basilisk

The key word makes the transposing sequence unique, so it's near impossible to crack without the key word. I mainly made this for fun, but it could serve a purpose for someone. A basic knowledge of python scripts should be all you need to use it. It should be compatible with pen on paper as well, since it uses only math and sequences, and no python-specific functions. You'd just have to spend some time copying the engineering. I'd prefer to leave the explicit just to code, but if someone thinks it should be explained in this readme, contact me. I'm also open to any suggestions or contribution ideas.

### Install

*Requires: Python 3*  
1. Install Python 3 if you don't have it  
2. Download or clone this repository  


### Encoding
`python basilisk.py <encode> <message> <keyword>`  

### Decoding
`python basilisk.py <decode> <message> <keyword>`  

- Something worth mentioning is that these functions lazilly accept anything as input. It is intended that the keyword and/or message does not include spaces, symbols, and numbers. I could add sanitizing to sturdy up those functions if needed.
