while True:
    try:
        weight,height = input("Please enter (weight in kilograms, height in centimeters): ").split(",")
        weight = float(weight)
        height = float(height)
        break
    except ValueError:
        print("Invalid input. Please enter valid floats.")
print("Your BMI is: " + str(weight/(height/100)**2))