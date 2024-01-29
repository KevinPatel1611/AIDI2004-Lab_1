def calculate_bmi(weight_kg, height_m):
    """
    Calculate BMI (Body Mass Index) using weight in kilograms and height in meters.
    Formula: BMI = weight (kg) / (height (m) ** 2)
    """
    if height_m <= 0:
        raise ValueError("Height must be greater than zero.")
    
    bmi = weight_kg / (height_m ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret BMI and provide a corresponding message.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    """
    Main function to execute BMI calculation and interpretation.
    """
    print("=== BMI Calculator ===")

    # Get user input
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    try:
        # Calculate BMI
        bmi_result = calculate_bmi(weight, height)

        # Interpret BMI
        bmi_category = interpret_bmi(bmi_result)

        # Display result
        print(f"Your BMI is: {bmi_result:.2f}")
        print(f"You are categorized as: {bmi_category}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
