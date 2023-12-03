heightCm=int(input("type your height in cm: "))

heightInches=heightCm/2.54
heightFeet=int(heightInches//12)
remainingInches=int(round(heightInches%12,0))

print(f"I'm {heightCm}cm tall, this is {heightFeet} feet and {remainingInches} inches")
