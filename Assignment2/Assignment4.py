speed = int(input("Enter the speed of car (in km/hr): "))
if speed <=60:
    print("No fine.")
elif speed <=80:
    print("$100 fine.")
elif speed <=100:
    print("$300 fine.")
else:
    print("License Suspended.")
