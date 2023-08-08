import qrcode
import tkinter as tk
from tkinter import filedialog

def save_qr_code(img):
    save_path = filedialog.asksaveasfilename(
        defaultextension=".png", #Selecting the file extension
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
        title="Save QR Code"
    )
    
    if save_path:
        img.save(save_path)
        print("QR code saved successfully at:", save_path)
    else:
        print("QR code not saved.")

def main():
    choice = input("What do you want to encode: ")
    data = choice

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')

    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window

    name = input("What name would you like to give this file?: ")
    save_qr_code(img)

if __name__ == "__main__":
    main()
