km=float(input("Enter the kilometres travelled: "))
if km<=5:
    fare=10
elif km<=15:
    fare=20
elif km<=25:
    fare=30
else:
    fare=50
print(f"Total fare: ${fare}")
