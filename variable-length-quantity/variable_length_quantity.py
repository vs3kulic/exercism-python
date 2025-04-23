"""
Module for Variable Length Quantity (VLQ) encoding and decoding.

Takes a list of non-negative integers and encodes them into a list of bytes
using VLQ encoding. The encoded bytes can then be decoded back into the original
list of integers.
"""

def encode(numbers):
    """
    Encode a list of integers into VLQ byte list.
    
    Args:
        numbers (list of int): Non-negative integers to encode.
    
    Returns:
        list of int: VLQ encoded bytes.
    """
    encoded_bytes = []

    for number in numbers:
        chunks = []

        if number == 0:
            encoded_bytes.append(0) # Zero is encoded as single byte 0x00
            continue

        while number > 0:
            chunks.append(number % 128)  # Extract 7 bits
            number //= 128 # Shift right by 7 bits
    
        chunks.reverse()  # Reverse chunks for big-endian order

        for i in range(len(chunks) - 1):  # Iterate over all but the last chunk
            chunks[i] += 128  # Set continuation bit (MSB)

        encoded_bytes.extend(chunks)

    return encoded_bytes


def decode(bytes_):
    """
    Decode a list of VLQ encoded bytes into list of integers.
    
    Args:
        bytes_ (list of int): VLQ encoded bytes.
    
    Returns:
        list of int: Decoded integers.
    
    Raises:
        ValueError: If sequence is incomplete.
    """
    numbers = []

    current_number = 0
    expecting_more = False

    for byte in bytes_:
        if not 0 <= byte <= 255:
            raise ValueError(f"Invalid byte value: {byte}")

        decoded_value = byte % 128 # Extract 7 bits data
        current_number = current_number * 128 + decoded_value # Shift left by 7 bits and add new value

        if byte >= 128: # Check continuation flag / byte (MSB)
            expecting_more = True # expect more bytes

        else:
            numbers.append(current_number) # Append complete number
            current_number = 0 # Reset for next integer
            expecting_more = False

    if expecting_more:
        raise ValueError("incomplete sequence")

    return numbers
