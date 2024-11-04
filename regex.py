import re

# Find all dates in the format dd-mm-yyyy in a text
text = "My dates of birth are 23-05-1995 and 14-08-1997."
pattern = r"\d{2}-\d{2}-\d{4}"  # Pattern for dates

matches = re.findall(pattern, text)
print(matches)  


# Define the email pattern
email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

# Sample emails to test
emails = ["harsh@example.com", "invalid-email", "patwa@domain.com", "hello@domain@domain.com"]

# Function to validate email
def validate_email(email):
    if re.match(email_pattern, email):
        return f"{email} is a valid email."
    else:
        return f"{email} is not a valid email."

# Test the function
for email in emails:
    print(validate_email(email))



    # Define the phone number pattern
phone_pattern = r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"

# Sample text containing phone numbers
text = "Contact us at 123-456-7890 or 123.456.7890. Our alternate number is 9876543210."

# Find all matching phone numbers
phone_numbers = re.findall(phone_pattern, text)
print("Extracted Phone Numbers:", phone_numbers)