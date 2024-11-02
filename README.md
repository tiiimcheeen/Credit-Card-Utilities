# Credit Card Utilities

This repository contains two Python scripts for working with credit card numbers. These utilities can **generate** random valid credit card numbers and **validate** existing credit card numbers based on industry standards.

## Files

- `credit_card_generator.py`: Generates random valid credit card numbers for various card types (Visa, MasterCard, American Express, Discover).
- `credit_card_validator.py`: Validates credit card numbers by checking card type, length, and using the Luhn algorithm to verify the number structure.

## Features

### `credit_card_generator.py`
- Allows the user to specify a card type for generation.
- Generates a credit card number with a valid structure and check digit based on the Luhn algorithm.
- Optionally formats the generated card number in groups for readability.

### `credit_card_validator.py`
- Accepts a credit card number input for validation.
- Identifies the card type and checks the number’s length.
- Verifies the number’s validity using the Luhn algorithm.

## How to Use

### Requirements
Ensure you have Python 3 installed.

### Run `credit_card_generator.py`
To generate a valid random credit card number:
```bash
python credit_card_generator.py
```
Follow the prompts to select a card type and generate a number.

### Run `credit_card_validator.py`
To validate a credit card number, run:
```bash
python credit_card_validator.py
```
Enter a card number when prompted to check if it’s valid.
