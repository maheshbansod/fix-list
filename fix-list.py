
import sys
import re

if(len(sys.argv)<2):
	sys.exit(1)

def checkLine(line, cnt):
	"""Checks if the given line is in correct format.
		The given string is expected to be a single line with no trailing spaces.
	"""
	cnt+=1

	m = re.match(r'\A(\d+)\.\s[^a-z].*\Z',line)

	if(not m):
		p=re.match(r'\A(\d+)(.*)\Z',line)
		if not p: #doesn't have a digit at the beginning
			line=str(cnt)+line
			return checkLine(line, cnt-1)
		else:
			rest = p.group(2)
			add=". "
			if(rest[0] == '.'):
				rest=rest[1:]
			if(rest[0] == ' '):
				rest=rest[1:]
			rest=rest.title() #remove this and replace with rest.capitalize()
			line = p.group(1)+add+rest
			return checkLine(line, cnt-1)
	else:
		n = int(m.group(1))
		if(cnt!=n):
			p=re.match(r'\A(\d+)(.*)\Z',line)
			line=str(cnt)+p.group(2)
	
	return line, cnt

filename = sys.argv[1]
cnt = 0
try:
	f = open(filename, "r")
	for line in f:
		line=line.strip()
		(line,cnt)=checkLine(line, cnt)
		print(line)

except FileNotFoundError:
	print("The file '"+filename+"' was not found.")


