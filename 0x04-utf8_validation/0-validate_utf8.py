#!/usr/bin/python3
"""
UTF-8 Validation

In this implementation, we iterate over each byte in the given data set.
We maintain a num_bytes variable to keep track of the number of bytes
expected in the current UTF-8 character.

If the current byte is a continuation byte (i.e., the two most
significant bits are 10), we decrement num_bytes since it is part
of the current character.

If the current byte is a new UTF-8 character (i.e., the two most
significant bits are not 10), we determine the number of bytes in
the character based on the first few bits. We update num_bytes
accordingly.

If the current byte doesn't match the expected pattern for a
continuation byte or a new character, the data set is considered
invalid, and we return False.

Finally, after iterating over all the bytes, we check if num_bytes
is 0. If it is, it means all UTF-8 characters were properly
terminated, and we return True. Otherwise, we return False.

Note that this implementation assumes that the input data set
contains valid UTF-8 encoded bytes, represented as integers.
It only checks the basic validity of the UTF-8 encoding and
doesn't perform full validation against the entire Unicode character set.
"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding
    """
    #if data is None:
    #   return False

    # Variable to track the number of bytes in the current UTF-8 character
    num_bytes = 0

    for num in data:
        # Check if the current byte is a continuation byte
        if num_bytes > 0 and (num >> 6) == 0b10:
            num_bytes -= 1
        # Check if the current byte is a new UTF-8 character
        elif num_bytes == 0:
            # Determine the number of bytes in the current UTF-8 character
            if (num >> 7) == 0b0:
                num_bytes = 0  # Single-byte character
            elif (num >> 5) == 0b110:
                num_bytes = 1  # Two-byte character
            elif (num >> 4) == 0b1110:
                num_bytes = 2  # Three-byte character
            elif (num >> 3) == 0b11110:
                num_bytes = 3  # Four-byte character
            else:
                return False  # Invalid UTF-8 character start byte
        else:
            return False  # Invalid UTF-8 continuation byte

    return num_bytes == 0  # All UTF-8 characters were properly terminated
