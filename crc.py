def crc_remainder(data, divisor):
    """Calculates the CRC remainder of a given data word and divisor"""
    # Append zeros to the data word equal to the degree of the divisor
    data = data + '0' * (len(divisor) - 1)
    # Convert the data word and divisor from strings to lists of integers
    data = [int(bit) for bit in data]
    divisor = [int(bit) for bit in divisor]
    
    # Perform CRC division
    for i in range(len(data) - len(divisor) + 1):
        if data[i] == 1:
            for j in range(len(divisor)):
                data[i + j] ^= divisor[j]
    
    # Return the CRC remainder as a string
    return ''.join(str(bit) for bit in data[-(len(divisor) - 1):])

def crc_encode(data, divisor):
    """Encodes the given data word using CRC"""
    remainder = crc_remainder(data, divisor)
    # Append the CRC remainder to the original data word
    return data + remainder

def crc_decode(received_data, divisor):
    """Decodes the received data word using CRC"""
    remainder = crc_remainder(received_data, divisor)
    # Check if the remainder is all zeros
    if all(bit == '0' for bit in remainder):
        return received_data[:-len(divisor) + 1]  # Return the original data word
    else:
        return None  # Return None if CRC check fails

# Get user input for data word
data_word = input("Enter a binary data word: ")
if not all(bit in '01' for bit in data_word):
    print("Invalid input. Please enter a binary data word.")
    exit()

# Get user input for divisor
divisor = input("Enter a binary divisor (CRC polynomial): ")
if not all(bit in '01' for bit in divisor):
    print("Invalid input. Please enter a binary divisor.")
    exit()

print("Original data word:", data_word)

# Encode the data word using CRC
encoded_data = crc_encode(data_word, divisor)
print("Encoded data word:", encoded_data)

# Decode the received data word using CRC
decoded_data = crc_decode(encoded_data, divisor)
if decoded_data is not None:
    print("Decoded data word:", decoded_data)
else:
    print("CRC check failed. Error detected in received data word.")
