hrs = float(raw_input("Enter Hours: "))
rte = float(raw_input("Rate: "))


if hrs > 40:
	extra_hrs = hrs - 40
	tnh = rte * 1.5
	total = (rte * 40) + (extra_hrs * tnh)

else:
	total = hrs * rte