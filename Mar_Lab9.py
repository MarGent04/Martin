def encode(password):
    if not password.isdigit() or len(password) != 8:
        raise ValueError("Password should be an 8-digit string containing only integers.")

    encoded_password = ''
    for i in range(len(password)):
        encoded_digit = str((int(password[i]) + 3) % 10)  # Shift each digit up by 3 numbers
        encoded_password += encoded_digit

    return encoded_password

## This is Parth Patel's Part of this project

def decode(encoded_password):
    if not encoded_password.isdigit() or len(encoded_password) != 8:
        raise ValueError("Encoded password should be an 8-digit string containing only integers.")

    decoded_password = ''
    for i in range(len(encoded_password)):
        decoded_digit = str((int(encoded_password[i]) - 3) % 10)  # Shift each digit down by 3 numbers
        decoded_password += decoded_digit

    return decoded_password



if __name__ == '__main__':
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            password = input("Enter the 8-digit password to encode: ")
            try:
                encoded_password = encode(password)
                print(f"Encoded password: {encoded_password}")
            except ValueError:
                print("Error: Password must be an 8-digit string containing only integers.")


        elif choice == '3':
            print("Exiting...")
            break
            

        else:
            print("Invalid choice. Please enter a valid option.")