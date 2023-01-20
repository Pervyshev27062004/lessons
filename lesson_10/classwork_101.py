import re
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_string(string):
    return re.search(r"\+\d{1,3}\s\(\d{2}\)\s\d{3}\-\d{2}\-\d{2}", string)
if __name__ == "__main__":
    test_string = "An example word:cat!!"
    test_string = input("Enter a string:")
    match = check_string(test_string)
    if match:
        print(f"Found, {match.group()}")  # Found word:cat
    else:
        print("Did not find")