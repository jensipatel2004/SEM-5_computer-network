# Cyclic Redundancy Check Error Detection Method
# EG - 10101010111101100001
# generator polynomial - 10101010101010101010101010101010

def xor(a, b):
    """Perform XOR operation for two binary strings."""
    result = []
    for i in range(1, len(b)):
        result.append("1" if a[i] != b[i] else "0")
    return "".join(result)


def mod2div(dividend, divisor):
    """Perform Modulo-2 division."""
    pick = len(divisor)
    tmp = dividend[0:pick]

    while pick < len(dividend):
        if tmp[0] == "1":
            tmp = xor(divisor, tmp) + dividend[pick]
        else:  # If leftmost bit is '0'
            tmp = xor("0" * pick, tmp) + dividend[pick]

        pick += 1

    # For the last step, perform XOR for remaining bits
    if tmp[0] == "1":
        tmp = xor(divisor, tmp)
    else:
        tmp = xor("0" * pick, tmp)

    return tmp


def encode_data(data, key):
    """Encode data by appending the CRC checksum."""
    key_len = len(key)
    appended_data = data + "0" * (key_len - 1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    return codeword


def decode_data(data, key):
    """Decode data and check for errors."""
    remainder = mod2div(data, key)
    return remainder


# Main function to demonstrate CRC
def simulate():
    print("--- CRC Error Detection ---")

    # Input binary data and divisor (generator polynomial:- 11100000)
    data = input("Enter binary data: ")
    # key = input("Enter generator polynomial (binary): 10101010101010101010101010101010")
    print("Enter generator polynomial (binary): 1001")
    key = "1001"

    print("\nEncoding data...")
    codeword = encode_data(data, key)
    print(f"Encoded Data (Codeword): {codeword}")

    print("\nSimulating data transmission...")
    received_data = input("Enter received data (simulate errors by changing bits): ")

    print("\nChecking for errors...")
    remainder = decode_data(received_data, key)
    if "1" in remainder:
        print(f"Error detected! Remainder: {remainder}")
    else:
        print("No error detected. Data received correctly.")