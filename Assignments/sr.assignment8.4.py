fname = raw_input('Enter File : ')

if len(fname) == 0:
	fname = 'romeo.txt'

try:
	fh = open(fname)
except:
	print "Not a file bro.."

words = []

for line in fh:
	line_words = line.split()
	for word in list_words:
		if word in words:
			continue
		words.append(word)

print sorted(words)