"""
The program generates a qr code for any given link or data
"""

import qrcode

def generate_qr():
    """
    Saves a qr code in the same file as this program based on user input
    """
    while True: #Determine QR code size
        try:
            version_temp = int(input("Enter the QR Code matrix size (integer from 1 to 40): "))
            if version_temp >= 1 and version_temp <= 40:
                break
            else:
                print("Only integers from 1 to 40 are accepted.")
        except ValueError:
            print("Only integers from 1 to 40 are accepted.")
    
    while True: #Determine error correction
        print("There are 4 types of error corrections:")
        print("L: corrects 7% or less errors")
        print("M: corrects 15% or less errors")
        print("Q: corrects 25% or less errors")
        print("H: corrects 30% or less errors")
        error_temp = input("Please enter a correction type (L,M,Q,H): ").strip().lower()
        if error_temp == "l":
            error_temp = qrcode.constants.ERROR_CORRECT_L
            break
        elif error_temp == "m":
            error_temp = qrcode.constants.ERROR_CORRECT_M
            break
        elif error_temp == "q":
            error_temp = qrcode.constants.ERROR_CORRECT_Q
            break
        elif error_temp == "h":
            error_temp = qrcode.constants.ERROR_CORRECT_H
            break
        else:
            print("That is not an accepted value. Try again.")

    while True: #Determine box size
        try:
            size_temp = int(input("Enter the QR Code size: "))
            break
        except ValueError:
            print("Only integers are accepted.")
    
    while True: #Determine border size
        try:
            border_temp = int(input("Enter the border size: "))
            break
        except ValueError:
            print("Only integers are accepted.")

    qr = qrcode.QRCode(
        version = version_temp,
        error_correction = error_temp,
        box_size = size_temp,
        border = border_temp,
    )

    qr.add_data(input("Enter the data you would like to turn into a qr code: "))
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg.png")

#starts program
generate_qr()
