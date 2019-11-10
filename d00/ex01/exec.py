import sys

str = sys.argv[1]
strl=len(str)
revstring=str[strl::-1]
print(revstring.swapcase())
