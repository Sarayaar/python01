text = "X-DSPAM-Confidence:    0.8475"

num_strt = text.find("0")
num = text[num_strt:]

flt = float(num)

print flt