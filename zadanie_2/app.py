import re
from datetime import datetime
from typing import List

def is_valid_email(email: str) -> bool:
    print("App module loaded for email validation")
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def calculate_area(shape: str, *dimensions: float) -> float:
    print("App module loaded for calculating area")
    if shape == "circle" and len(dimensions) == 1:
        return 3.14159 * dimensions[0] ** 2
    elif shape == "rectangle" and len(dimensions) == 2:
        return dimensions[0] * dimensions[1]
    elif shape == "triangle" and len(dimensions) == 2:
        return 0.5 * dimensions[0] * dimensions[1]
    else:
        raise ValueError("Invalid shape or dimensions")

def process_list(data: List[int], operation: str) -> List[int]:
    print("App module loaded for list processing")
    if operation == "sort":
        return sorted(data)
    elif operation == "filter_even":
        return [x for x in data if x % 2 == 0]
    else:
        raise ValueError("Invalid operation")

def convert_date_format(date_str: str, input_format: str, output_format: str) -> str:
    print("App module loaded for converting data format")
    try:
        date_obj = datetime.strptime(date_str, input_format)
        return date_obj.strftime(output_format)
    except ValueError:
        raise ValueError("Invalid date format")

def is_palindrome(text: str) -> bool:
    print("App module loaded for palindrom validation")
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    return cleaned_text == cleaned_text[::-1]

if __name__ == "__main__":
    print(is_valid_email("test@example.com"))  
    print(calculate_area("circle", 5))  
    print(process_list([5, 3, 8, 1], "sort"))  
    print(convert_date_format("2025-03-19", "%Y-%m-%d", "%d/%m/%Y"))  
    print(is_palindrome("A man, a plan, a canal: Panama"))  
