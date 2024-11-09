def reverse_number(number):
    """
    Reverse a given integer.

    Args:
        number (int): The number to reverse

    Returns:
        int: The reversed number

    Raises:
        ValueError: If input is not an integer
    """
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    
    # Handle negative numbers
    is_negative = number < 0
    number = abs(number)
    
    # Reverse the number
    rev = 0
    while number:
        tmp = number % 10
        rev = rev * 10 + tmp
        number //= 10
    
    return -rev if is_negative else rev


if __name__ == "__main__":
    # Example usage
    try:
        number = int(input("Enter an integer to reverse: "))
        print(f"Reversed number: {reverse_number(number)}")
    except ValueError as e:
        print(f"Error: {e}")
