# Number Reversal Algorithm

A simple and efficient Python algorithm to reverse an integer without converting it to a string.

## Description

This algorithm reverses a given integer by extracting each digit and rebuilding the number in reverse order. For example, `123456789` becomes `987654321`.

### How It Works

The algorithm uses basic arithmetic operations to:
1. Extract each digit from right to left
2. Build the reversed number from left to right
3. Process until all digits are handled

## Code Example

```python
number = 123456789
rev = 0

while number:
    tmp = number % 10      # Get rightmost digit
    rev = rev * 10 + tmp   # Add digit to reversed number
    number //= 10          # Remove rightmost digit
    
print(rev)  # Output: 987654321
```

### Step-by-Step Explanation

Let's break down how the algorithm works using the number 123:

1. First Iteration:
   - `tmp = 123 % 10 = 3`
   - `rev = 0 * 10 + 3 = 3`
   - `number = 123 // 10 = 12`

2. Second Iteration:
   - `tmp = 12 % 10 = 2`
   - `rev = 3 * 10 + 2 = 32`
   - `number = 12 // 10 = 1`

3. Third Iteration:
   - `tmp = 1 % 10 = 1`
   - `rev = 32 * 10 + 1 = 321`
   - `number = 1 // 10 = 0`

4. Loop ends as `number` becomes 0

## Time and Space Complexity

- Time Complexity: O(log n), where n is the input number
- Space Complexity: O(1), uses only a constant amount of extra space

## Usage

```python
# To use with a different number:
number = 123456789  # Replace with any integer
rev = 0

while number:
    tmp = number % 10
    rev = rev * 10 + tmp
    number //= 10

print(rev)
```

## Limitations

1. Only works with positive integers
2. May not preserve leading zeros
3. Limited by the maximum integer size in Python

## Possible Improvements

1. Add input validation
2. Handle negative numbers
3. Add error handling for integer overflow

## Example Implementation with Improvements

```python
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
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
