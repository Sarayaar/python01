fname = raw_input('Enter File: ')

if len(fname) == 0:
	fname = 'mbox-short.txt'

try:
	fh = open(fname)
except:
	print "Not a file bro.."

emails = {}
email_list[]
for line in fh:
	if not line.startswith('From '):
		continue
	words = line.split()
	email = word[1]
	email_list.append(email)

for address in email_list:
	emails[address] = emails.get(address, 0) = 1


big_address = None
big_count = None

for address, count in emails.items():
	if big_count is None or count > big_count:
		big_count = count
		big_address = address

print big_count, big_address