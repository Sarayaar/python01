fname = raw_input('File Name: ')

if len(fname) == 0:
	fname = 'mbox-short.txt'

	try:
		fh = open (fname)
	except:
		print "Not a file bro.."

count = 0
for line in fh:
	if not line.startswith('X-DSPAM-Confidence:'):
		continue

	num_start = line.find('0')
	num = line[num_start:]
	flt = float (num)
	count += flt

print count 