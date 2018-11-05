
import sys
import re

if(len(sys.argv)<2):
	sys.exit(1)

def checkLine(line, cnt):
	"""Checks if the given line is in correct format.
		The given string is expected to be a single line with no trailing spaces.
	"""
	cnt+=1
	line=line.strip()

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
			rest=rest.title() #replace with rest.capitalize() in the future
			line = p.group(1)+add+rest
			return checkLine(line, cnt-1)
	else:
		n = int(m.group(1))
		p=re.match(r'\A(\d+)(.*)\Z',line)
		rest = p.group(2)
		if(cnt!=n):
			line=str(cnt)+rest
		# the next few lines are added for a special case
		# when a number appears inside the list
		# then that number is assumed to be part of the next list item
		p2=re.match(r'\A([\D]*)(\d+.*)\Z',rest)
		if p2:
			line=str(cnt)+p2.group(1)
			print(line)
			line=p2.group(2)
			return checkLine(line, cnt)
	
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


