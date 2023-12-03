height=float(input("Enter your height in cm: "))
weight=float(input("Enter your weight in kg: "))
BMI = weight/ ((height/100) ** 2)
correctness = 18.5<= BMI <= 24.9
print(f"Your BMI index: {BMI}")
print(f"Correct weight: {correctness}")
