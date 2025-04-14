def calculate_vrc(data):
    """
    Calculate the Vertical Redundancy Check (VRC) for the given data.

    :param data: A list of binary strings (each representing a byte)
    :return: The VRC parity bit for each column
    """
    # Transpose the data to get columns
    columns = zip(*data)
    vrc = []

    for column in columns:
        count_ones = sum(int(bit) for bit in column)
        parity_bit = "1" if count_ones % 2 != 0 else "0"
        vrc.append(parity_bit)

    return "".join(vrc)

def simulate():
    """Simulate VRC error detection."""
    print("--- VRC Error Detection ---")

    # Input binary data
    num_data = int(input("Enter the number of data bytes: "))
    data = []
    for i in range(num_data):
        byte = input(f"Enter binary data byte {i + 1} (8 bits): ")
        while len(byte) != 8 or not all(bit in "01" for bit in byte):
            print("Invalid input. Please enter exactly 8 bits (0 or 1).")
            byte = input(f"Enter binary data byte {i + 1} (8 bits): ")
        data.append(byte)

    print("\nOriginal Data:", data)

    # Calculate VRC
    vrc = calculate_vrc(data)
    print("Generated VRC (parity bits):", vrc)

    # Simulate transmission and check for errors
    print("\nSimulating data transmission...")
    received_data = []
    for i in range(num_data):
        byte = input(f"Enter received data byte {i + 1} (simulate errors by changing bits): ")
        while len(byte) != 8 or not all(bit in "01" for bit in byte):
            print("Invalid input. Please enter exactly 8 bits (0 or 1).")
            byte = input(f"Enter received data byte {i + 1} (simulate errors by changing bits): ")
        received_data.append(byte)

    received_vrc = calculate_vrc(received_data)
    print("\nReceived VRC (parity bits):", received_vrc)

    # Check for errors
    if vrc == received_vrc:
        print("No error detected. Data received correctly.")
    else:
        print("Error detected in the received data!")