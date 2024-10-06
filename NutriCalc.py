def calculate_caloric_needs():
    # Get user inputs
    weight = float(input("Enter your weight in kilograms: "))  # Weight in kg
    height = float(input("Enter your height in centimeters: "))  # Height in cm
    age = int(input("Enter your age in years: "))  # Age in years
    gender = input("Enter your gender (male/female): ").strip().lower()
    goal = input("Do you want to gain weight (type 'gain') or lose weight (type 'lose')? ").strip().lower()

    # Calculate BMR using Mifflin-St Jeor Equation
    if gender == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender == "female":
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    else:
        print("Please enter a valid gender (male or female).")
        return

    # Calculate daily caloric needs
    if goal == "gain":
        daily_calories = bmr + 500
    elif goal == "lose":
        daily_calories = bmr - 500
    else:
        print("Please enter a valid goal (gain or lose).")
        return

    # Calculate protein intake
    protein = weight * 1.6  # Protein in grams
    protein_calories = protein * 4  # Total calories from protein

    # Calculate healthy fats intake
    fat_percentage = float(input("Enter the percentage of healthy fats (between 20 to 30)%: ")) / 100
    if fat_percentage < 0.2 or fat_percentage > 0.3:
        print("Please enter a valid fat percentage between 20% and 30%.")
        return

    fat_calories = daily_calories * fat_percentage

    # Calculate carbohydrate intake
    carb_calories = daily_calories - (protein_calories + fat_calories)

    # Display results
    print(f"\nDaily caloric needs: {daily_calories:.2f} calories")
    print(f"Calories from protein: {protein_calories:.2f} calories ({protein:.2f} grams of protein)")
    print(f"Calories from healthy fats: {fat_calories:.2f} calories")
    print(f"Calories from carbohydrates: {carb_calories:.2f} calories")

# Call the function to run the program
calculate_caloric_needs()