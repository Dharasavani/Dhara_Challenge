import re

def validate_credit_card(card_number):
    # Remove any whitespace and hyphens from the card number
    card_number = card_number.replace('-', '')

    # Check if the card number starts with 4, 5, or 6
    if not re.match(r'^[456]', card_number):
        return False

    # Check if the card number contains exactly 16 digits
    if not re.match(r'^\d{16}$', card_number):
        return False
    
    # Check if the card number only consists of digits (0-9)
    if not re.match(r'^\d+$', card_number):
        return False
    
    # Check if the card number does not have 4 or more consecutive repeated digits
    if re.search(r'(\d)\1{3,}', card_number):
        return False
    
    return True

def check_credit_card_numbers(input_file):
    with open(input_file, 'r') as file:
        # Read the credit card numbers from the input file
        for line_number, line in enumerate(file, start=1):
            card_number = line.strip()
            if validate_credit_card(card_number):
                print('Valid')
            else:
                print('Invalid')

if __name__ == "__main__":
    input_file = "credit_cards_input.txt"  # Specify your input file here
    check_credit_card_numbers(input_file)
