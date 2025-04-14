from Methods import crc
from Methods import lrc
from Methods import vrc
from Methods import checksum

while True:
    print("Error Detection Methods")
    print("1. CRC (Cyclic Redundancy Check)")
    print("2. LRC (Longitudinal Redundancy Check)")
    print("3. VRC (Vertical Redundancy Check)")
    print("4. Checksum")
    print("5 Exit")
    choice = input("Choose a method (1-5): ")
    if choice == "1":
        crc.simulate()
    elif choice == "2":
        lrc.simulate()
        pass
    elif choice == "3":
        vrc.simulate()
        pass
    elif choice == "4":
        checksum.simulate()
        pass
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please select a valid option.")