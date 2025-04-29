day=input("What day is it today?: ").lower()
if day in ['monday','tuesday','wednesday','thursday','friday']:
    print("Work Day!")
elif day == "saturday":
    print("Family Time!")
elif day == "sunday":
    print("Relax Time!")
else:
    print("Invalid day entered")
