fname = raw_input('File Name: ')

if len(fname) == 0
fname = 'mbox-short.txt'

try:
	fh = open(fname)
except:
	print "Not a file bro.."

count = 0
for line in fh:
	if not line.startswith('From'):
		continue
	words_list = line.split()
	email = words_list[1]
	count += 1
	print email

print count