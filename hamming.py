def encode(message):
    # Calculate parity bits
    p1 = message[0] ^ message[1] ^ message[3]
    p2 = message[0] ^ message[2] ^ message[3]
    p3 = message[1] ^ message[2] ^ message[3]
    
    # Create codeword
    codeword = [p1, p2, message[0], p3, message[1], message[2], message[3]]
    
    return codeword

def decode(codeword):
    # Calculate syndrome bits
    s1 = codeword[0] ^ codeword[2] ^ codeword[4] ^ codeword[6]
    s2 = codeword[1] ^ codeword[2] ^ codeword[5] ^ codeword[6]
    s3 = codeword[3] ^ codeword[4] ^ codeword[5] ^ codeword[6]
    
    # Calculate error position
    error_pos = s3 * 4 + s2 * 2 + s1 - 1
    
    return error_pos

# Get user input for message
message = input("Enter a 4-bit binary message (e.g., 1011): ")
if len(message) != 4 or not all(bit in '01' for bit in message):
    print("Invalid input. Please enter a 4-bit binary message.")
    exit()

# Convert user input to list of integers
message = [int(bit) for bit in message]

print("Original message:", message)

# Encode the message
codeword = encode(message)
print("Generated Hamming code (r1, r2, m1, r3, m2, m3, m4):", codeword)

# Decode the received codeword
error_pos = decode(codeword)
print("Error position (if any):", error_pos)
