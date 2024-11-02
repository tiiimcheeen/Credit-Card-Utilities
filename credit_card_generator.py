"""
credit_card_generator.py

This script generates valid random credit card numbers for various card types
based on user input. Users can select a card type (Visa, MasterCard, American Express, Discover),
and the program generates a credit card number that:
1. Starts with the correct Issuer Identification Number (IIN) for the specified card type.
2. Matches the correct length for the selected card type.
3. Includes a valid check digit calculated using the Luhn algorithm to ensure the number structure is valid.

Users have the option to format the generated number in groups of four for readability.
The program will continue running until the user chooses to exit.
"""

import random

# Define card types with known IIN ranges and expected lengths
CARD_TYPES = {
    "visa": {"iin": ["4"], "length": 16},
    "mastercard": {"iin": ["51", "52", "53", "54", "55"], "length": 16},
    "american express": {"iin": ["34", "37"], "length": 15},
    "discover": {"iin": ["6011", "65"], "length": 16},
}


def generate_card_number(card_type, formatted=False):
    """Generate a random valid credit card number based on card type."""
    card_type = card_type.lower()  # Normalize input to lowercase
    if card_type not in CARD_TYPES:
        raise ValueError(f"Unsupported card type: {card_type.capitalize()}")

    # Select a random IIN for the card type
    iin = random.choice(CARD_TYPES[card_type]["iin"])
    card_length = CARD_TYPES[card_type]["length"]

    # Generate the initial part of the card number
    number = iin + ''.join([str(random.randint(0, 9)) for _ in range(card_length - len(iin) - 1)])

    # Calculate the check digit using the Luhn algorithm
    check_digit = calculate_luhn_check_digit(number)
    card_number = number + str(check_digit)

    # Optionally format the card number for readability
    return format_card_number(card_number) if formatted else card_number


def calculate_luhn_check_digit(number):
    """Calculate the Luhn check digit for a card number without the last digit."""
    digits = [int(d) for d in number]
    sum_digits = 0

    # Reverse the digits and apply the Luhn algorithm
    for i, digit in enumerate(reversed(digits)):
        if i % 2 == 0:  # Double every second digit from the right
            doubled = digit * 2
            sum_digits += doubled - 9 if doubled > 9 else doubled
        else:
            sum_digits += digit

    # Calculate the check digit to make the total sum divisible by 10
    check_digit = (10 - (sum_digits % 10)) % 10
    return check_digit


def format_card_number(card_number):
    """Format card number into groups for readability."""
    return ' '.join([card_number[i:i + 4] for i in range(0, len(card_number), 4)])


def main():
    while True:
        print("\nAvailable card types: Visa, MasterCard, American Express, Discover")
        card_type = input("Enter card type (or 'exit' to quit): ")

        if card_type.lower() == 'exit':
            print("Goodbye!")
            break

        # Ask if the user wants formatted output
        formatted = input("Do you want the card number formatted (yes/no)? ").strip().lower() == 'yes'

        try:
            card_number = generate_card_number(card_type, formatted=formatted)
            print(f"Generated {card_type.capitalize()} number: {card_number}")
        except ValueError as e:
            print(e)


if __name__ == '__main__':
    main()
