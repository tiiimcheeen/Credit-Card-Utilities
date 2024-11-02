"""
credit_card_validator.py

This script validates credit card numbers based on card type, length, and the Luhn algorithm.
Users can input a single credit card number to verify if it’s valid. The program checks:
1. Card type based on IIN ranges (Visa, MasterCard, American Express, Discover).
2. Card number length to match card type requirements.
3. Luhn algorithm to ensure the credit card number structure is valid.

Users can enter 'exit' to quit the program.
"""

import re

# Define card types with known IIN ranges and expected lengths
CARD_TYPES = {
    "visa": {"iin": ["4"], "length": [13, 16, 19]},
    "mastercard": {"iin": ["51", "52", "53", "54", "55"], "length": [16]},
    "american express": {"iin": ["34", "37"], "length": [15]},
    "discover": {"iin": ["6011", "65"], "length": [16, 19]},
}


def get_card_type(card_number):
    """Identify the card type based on IIN ranges."""
    for card_type, info in CARD_TYPES.items():
        for iin in info["iin"]:
            if card_number.startswith(iin):
                return card_type
    return None


def luhn_check(card_number):
    """Perform Luhn algorithm to validate credit card number."""
    sum_odd_digits = 0
    sum_even_digits = 0
    card_number = card_number[::-1]

    # Step 2: Sum odd-position digits
    for x in card_number[::2]:
        sum_odd_digits += int(x)

    # Step 3: Double even-position digits and adjust if necessary
    for x in card_number[1::2]:
        x = int(x) * 2
        if x >= 10:
            sum_even_digits += (1 + (x % 10))
        else:
            sum_even_digits += x

    # Step 4: Sum totals and check divisibility by 10
    total = sum_odd_digits + sum_even_digits
    return total % 10 == 0


def validate_card(card_number):
    # Step 1: Clean up the card number
    card_number = re.sub(r"[^0-9]", "", card_number)  # Remove non-numeric characters

    # Check card type and length
    card_type = get_card_type(card_number)
    if not card_type:
        return "INVALID - Unknown card type"

    if len(card_number) not in CARD_TYPES[card_type]["length"]:
        return f"INVALID - Incorrect length for {card_type.capitalize()} card"

    # Perform Luhn check
    if luhn_check(card_number):
        return f"VALID - {card_type.capitalize()} card"
    else:
        return "INVALID - Failed Luhn check"


def main():
    while True:
        card_number = input("\nEnter a credit card number (or type 'exit' to quit): ")
        if card_number.lower() == 'exit':
            print("Goodbye!")
            break
        result = validate_card(card_number)
        print(f"Result: {result}")


if __name__ == '__main__':
    main()
