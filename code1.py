# Basic Key Programming Activities

def get_user_input():
    """
    Function to get user input for a key programming activity.
    """
    user_input = input("Enter a key or string: ")
    return user_input

def process_input(input_data):
    """
    Function to process the user input for key programming.
    """
    processed_data = input_data.upper()  # Convert input to uppercase
    return processed_data

def display_result(result):
    """
    Function to display the result of key programming activity.
    """
    print("Processed Result:", result)

def main():
    """
    Main function to orchestrate key programming activities.
    """
    print("=== Key Programming Activities ===")

    # Step 1: Get user input
    user_input = get_user_input()

    # Step 2: Process input
    processed_result = process_input(user_input)

    # Step 3: Display result
    display_result(processed_result)

if __name__ == "__main__":
    main()
