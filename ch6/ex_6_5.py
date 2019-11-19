text = "X-DSPAM-Confidence:    0.8475"
ipos = text.find(':')
piece = text[ipos+1:]
clean = piece.strip()
value = float(clean)
print(value)