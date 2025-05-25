import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r""
name_regex = re.compile(name)

phone_number = r""
phone_regex = re.compile(phone_number)

email_address = r""
email_regex = re.compile(email_address)
import re

# Name regex:
# - Allows multiple parts separated by spaces or hyphens
# - Allows apostrophes within names (like D'Angelo)
# - Each name part starts with uppercase, followed by lowercase letters or apostrophes/hyphens
name_regex = re.compile(
    r"^[A-Z][a-zA-Z']*(?:[- ][A-Z][a-zA-Z']*)*$"
)

# Phone number regex:
# - Matches 10 digit numbers with optional separators: space, dash, parentheses for area code
# - Examples matched: 5555555555, 555-555-5555, (555) 555-5555
phone_regex = re.compile(
    r"^(?:\(\d{3}\)\s?|\d{3}[- ]?)?\d{3}[- ]?\d{4}$"
)

# Email regex:
# - Username: letters, digits, dots, underscores, plus, hyphens
# - Domain: letters, digits, hyphens
# - Extension: 2+ letters
email_regex = re.compile(
    r"^[A-Za-z][\w\.\+\-]*@[\w\-]+\.[a-zA-Z]{2,}$"
)


