def computepay(h,r):
    ovt = h - 40.0
    if ovt > 0 :
        tot = (40.0 * r) + (ovt * r * 1.5)
    else:
        tot = (h * r)
    return tot

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
p = computepay(h,r)
print(p)