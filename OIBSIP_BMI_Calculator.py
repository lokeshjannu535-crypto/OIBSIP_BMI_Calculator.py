try:
    weight = float(input("Enter your weight in kg: "))
except ValueError:
    print("Please enter a valid number.")
    exit()

if weight <= 0:
    print("Weight must be greater than 0.")
    exit()

try:
    height = float(input("Enter your height in meters: "))
except ValueError:
    print("Please enter a valid number.")
    exit()

if height <= 0:
    print("Height must be greater than 0.")
    exit()

bmi = weight / (height ** 2)

print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("category:obese")