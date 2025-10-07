# Pre-pass for a Luhn Algorithm implementation

## Input

The number will be provided as a string.

## Validation

- Strings of length 1 or less are not valid.
- Spaces are allowed in the input, but they should be stripped before checking.
- All other non-digit characters are disallowed.

## Processing

- The first step of the Luhn algorithm is to start at the end of the number and double every second digit, beginning with the second digit from the right and moving left.
- If the result of doubling a digit is greater than 9, we subtract 9 from that result.
- Finally, we sum all digits.
- If the sum is evenly divisible by 10, the original number is valid.

## Output

Decision as boolean value.

## Example implementation

```JavaScript
function valid(number) {
    var splitNumber = number.replace(/\s+/g, '').split("").map(Number); // Remove spaces and split into digits
    var total = 0;
    var length = splitNumber.length;

    for (var i = 0; i < length; i++) {
        var digit = splitNumber[length - 1 - i]; // Access digits from the right
        if (i % 2 === 1) { // Double every second digit from the right
            var doubled = digit * 2;
            total += (doubled > 9) ? doubled - 9 : doubled;
        } else {
            total += digit;
        }
    }
    return total % 10 === 0;
}
```
