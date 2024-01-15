def main():
    numbers = {}  # A dictionary to store phone numbers and the count of each entry

    while True:
        # Request a phone number from the user
        phone_number = input("Please enter your phone number or 'exit' to exit: ")

        # Check if the user wants to exit
        if phone_number.lower() == 'exit':
            break

        # Remove any non-digit characters from the input
        cleaned_phone_number = ''.join(c for c in phone_number if c.isdigit())

        # Check if the cleaned phone number is valid
        if len(cleaned_phone_number) == 10:
            formatted_phone_number = f"{cleaned_phone_number[:3]}-{cleaned_phone_number[3:6]}-{cleaned_phone_number[6:]}"
        else:
            print("The phone number entered is not valid. Please enter a valid 10-digit phone number.")
            continue

        # Check if the formatted phone number is already in the dictionary
        if formatted_phone_number in numbers:
            numbers[formatted_phone_number]["count"] += 1
            print(f"This phone number has been entered {numbers[formatted_phone_number]['count']} times.")
        else:
            # Add the formatted phone number to the dictionary with a unique identifier
            unique_id = len(numbers) + 1
            numbers[formatted_phone_number] = {"id": unique_id, "count": 1}
            print(f"The phone number has been successfully saved with ID {unique_id}.")

        # Save the dictionary of phone numbers to a text file after each entry
        save_numbers_to_file(numbers)

    # Save the final version of the dictionary to a text file before exiting
    save_numbers_to_file(numbers)

def save_numbers_to_file(numbers):
    # Open a file for writing
    with open('phone_numbers.txt', 'w') as file:
        # Write phone numbers and entry counts to the file, sorted by ID
        sorted_numbers = sorted(numbers.items(), key=lambda x: x[1]["id"])
        for formatted_number, data in sorted_numbers:
            file.write(f"{data['id']}. {formatted_number} (entry count: {data['count']})\n")

if __name__ == "__main__":
    main()
