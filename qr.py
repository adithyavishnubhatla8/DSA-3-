import qrcode

def generate_link_qr(url, filename="acm.png"):
    # Configure the QR code parameters
    qr = qrcode.QRCode(
        version=1, # Controls the size of the QR Code (1 is smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L, # About 7% error correction
        box_size=10, # Pixels per QR code box
        border=4, # Thickness of the border
    )
    
    # Add your target link
    qr.add_data(url)
    qr.make(fit=True)

    # Generate and save the image file
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"Success! QR code saved as '{filename}'")

# Example usage
generate_link_qr("https://t.me/+3-X6B3wji1ZiYTk1")
