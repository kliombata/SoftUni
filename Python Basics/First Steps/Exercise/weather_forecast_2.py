degrees = float(input())

if degrees >= 5.00 and degrees <= 11.9:
    print ("Cold")
elif degrees >= 12.00 and degrees <= 14.9:
    print ("Cool")
elif degrees >= 15.00 and degrees <= 20.00:
    print ("Mild")
elif degrees >= 20.10 and degrees <= 25.90:
    print ("Warm")
elif degrees >= 26.00 and degrees <= 35.00:
    print ("Hot")

else:
    print ("unknown")