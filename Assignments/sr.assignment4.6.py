hrs = float(raw_input("Enter Hours: "))
rte = float(raw_input("Rate: "))

def ot_paycalc(rte, hrs):

	if hrs > 40:
		extra_hrs = hrs - 40
		tnh = rte * 1.5
		total = (rte * 40) + (extra_hrs * tnh)
		return total

	else:
		total = hrs * rte
		return total

pay = ot_paycalc(10, 44)