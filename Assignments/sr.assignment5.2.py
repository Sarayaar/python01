while True:
	input_num == "done":
		break
	try:
		num = int(raw_input('Enter a number: '))
	except:
		print "Thats not a number"
		continue
	largest = None
	smallest = None

	if largest is None or num > largest:
		largest = num
	if smallest is None or num < smallest:
		smallest = num
print "Largest:", largest, "Smallest:", smallest