Height=int(input("Enter you height in CM:"))
weight=int(input("Enter your weight in KG:"))
Height=Height/100
BMI=weight/(Height*Height)
print("your Body Mass Index is: ",BMI)
if(BMI>0):
	if(BMI<=12):
		print("You are severely underweight")
	elif(BMI<=15.5):
		print("You are underweight")
	elif(BMI<=25):
		print("You are Healthy")
	elif(BMI<=30):
		print("You are overweight")
	else: print("You are severely overweight")
else:("enter valid details")