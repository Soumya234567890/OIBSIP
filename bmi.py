print("This program calculates bmi(body mass index ) of a person\n")
name= input("Enter Your Name:")
weight=float(input("Enter your Weight:"))
height=float(input("Enter your height:"))

bmi= weight/(height**2)

if bmi<25:
    print(f"{name} is Underweight by {bmi} BMI")
else:
    print(f"{name} is Overweight by {bmi} BMI")





