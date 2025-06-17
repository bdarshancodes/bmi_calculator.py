print("Welcome \n" \
"BMI calculator by bdarshancodes\n")
while True:
    try:
        name=input("Please enter your beautiful name\n")
    except ValueError:
        print("please use valid keywords\n")
        continue


    try:
        weight=float(input(f"Hello {name} please enter you weight in kg \n"))
        height=float(input(f"Dear {name} please enter your height in feet\n"))
    except ValueError:
        print("please use valid keywords\n")
        continue

    height_m = height * 0.3048  
    BMI = weight / (height_m ** 2)
    
    print(f"Dear {name} your BMI is :" ,round(BMI , 2))
    if BMI<18.5:
        print(f"Dear {name} you are Underweight! please have proper diet meal")
    elif 18.5<= BMI < 24.9:
        print(f"Dear {name} you are normal and fit! well done,keep it up")
    elif 25 <= BMI < 29.9:
        print(f"Dear {name} you are Overweight! please go to gym regularly")
    elif  BMI >= 30:
        print(f"Dear {name} you are Obese! it is very dangerous")
    else:
        print("please enter valid details")
    again = input("\nDo you want to calculate again? (yes/no): ").lower()
    if again != 'yes':
        print("Thank you for using BMI calculator. Stay healthy!")
        break