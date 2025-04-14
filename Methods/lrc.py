def calculate_lrc(data):
    """
    Calculate the Longitudinal Redundancy Check (LRC) for the given data.
    
    :param data: A list of data bytes (each byte should be an integer between 0-255)
    :return: The LRC checksum byte
    """
    lrc = 0  # Initialize LRC as 0
    for byte in data:
        lrc ^= byte  # XOR each byte with the current LRC value
    
    return lrc

def encode_data_with_lrc(data):
    """
    Encode the data by appending the LRC checksum byte.
    
    :param data: A list of data bytes (each byte should be an integer between 0-255)
    :return: The data with the LRC byte appended
    """
    lrc_checksum = calculate_lrc(data)  # Calculate LRC
    return data + [lrc_checksum]  # Append LRC to the original data

def detect_error_in_lrc(data_with_lrc):
    """
    Detect if there is an error in the data using the LRC method.
    
    :param data_with_lrc: The data with the LRC checksum appended.
    :return: True if an error is detected, False otherwise.
    """
    data = data_with_lrc[:-1]  # All data except the last byte (LRC)
    received_lrc = data_with_lrc[-1]  # The LRC checksum
    
    # Recalculate the LRC for the data
    calculated_lrc = calculate_lrc(data)
    
    # Compare the calculated LRC with the received LRC
    return calculated_lrc != received_lrc  # If they differ, there's an error


def simulate():
    # Example usage
    # [231, 221, 170, 169]
    data1=input("Enter data 1: ")
    int1=int(data1)
    data2=input("Enter data 2: ")
    int2=int(data2)
    data3=input("Enter data 3: ")
    int3=int(data3)
    data4=input("Enter data 4: ")
    int4=int(data4)

    data = [int1,int2,int3,int4]  # Example data (list of bytes)
    print("Original Data:", data)
    data_binary1 = format(data[0],'08b') # Format the last byte in 8-bit binary form
    data_binary2 = format(data[1],'08b') 
    data_binary3 = format(data[2],'08b') 
    data_binary4 = format(data[3],'08b') 
    data_binary=[data_binary1,data_binary2,data_binary3,data_binary4]
    
    ['11100111', '11011101', '10101010', '10101001']
    print("Encoded Data (in binary):", data_binary[:])

    # Encode data with LRC
    #  [231, 221, 170, 169, 57]
    encoded_data = encode_data_with_lrc(data)
    print("Encoded Data with LRC:", encoded_data)
    
    # Convert the LRC checksum (last byte) to binary and print the result
    lrc_binary = format(encoded_data[-1],'08b')  # Format the last byte in 8-bit binary form
    
    ['11100111', '11011101', '10101010', '10101001', '00111001']
    print("Encoded Data with LRC (in binary):", data_binary[:] + [lrc_binary]) 

    print("\nError Detection:")
    error_detected = detect_error_in_lrc(encoded_data)
    if error_detected:
        print("Error detected in the received data.")
    else:
        print("No error detected in the received data.")