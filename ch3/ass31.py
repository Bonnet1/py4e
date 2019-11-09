hrs = input("Enter Hours:")
pay = input("Entry pay per hours:")
try:
    h = float(hrs)
    p = float(pay)
except:
    print("Error, please enter numeric input")
    quit()

ovt = h - 40.0

if ovt > 0 :
    tot = (40.0 * p) + (ovt * p * 1.5)
else:
    tot = (h * p)

print("Pay:",tot)