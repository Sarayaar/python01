score = float (raw_input('Enter your score'))

if score > 0 or score is < 1:
	print "Score is out of range!"
elif score >= .9:
	print "A"
elif score >= .8:
	print "B"
elif score >= .7:
	print "C"
elif score >= .6:
	print "D"
elif score < .5:
	print "F"
