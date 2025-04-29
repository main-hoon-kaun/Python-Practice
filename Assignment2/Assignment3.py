units=float(input("Enter the number of units consumed: "))
bill=0
if units <=100:
    bill=units*0.5
elif units <=300:
    bill=(100*0.5)+((units-100)*0.75)
else:
    bill=(100*0.5)+(200*0.75) +((units-300)*1.2)
print(f"Total electricity bill fot {units} is : ${bill:.2f}")
