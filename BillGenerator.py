import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime


#To center Window
def centerWin(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    width = 500
    height = 350
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")


# Function to generate bill as PDF
def generate_bill():
    product = product_entry.get()
    quantity = quantity_entry.get()
    price = price_entry.get()
    customer = customer_entry.get()

    if not (product and quantity and price and customer):
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        quantity = int(quantity)
        price = float(price)
        total = quantity * price

        # Create a unique PDF filename using a timestamp
        timestamp = datetime.datetime.now()
        pdf_file = f"Bill_{customer}_{timestamp}.pdf"

        # Create PDF
        c = canvas.Canvas(pdf_file, pagesize=letter)

        c.drawString(100, 750, f"Customer: {customer}")
        c.drawString(100, 730, f"Product: {product}")
        c.drawString(100, 710, f"Quantity: {quantity}")
        c.drawString(100, 690, f"Price per Unit: ${price:.2f}")
        c.drawString(100, 670, f"Total Amount: ${total:.2f}")

        c.save()

        messagebox.showinfo("Success", f"Bill generated: {pdf_file}")

        # Clear form entries after generating the bill
        customer_entry.delete(0, tk.END)
        product_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Invalid quantity or price")

# Create GUI window

root = tk.Tk()
root.title("Billing Software")
root.geometry("500x500")
root.resizable(False,False)
centerWin(root)


# Labels and Entry fields(used help of chat gtp for paddings)
tk.Label(root, text="Customer Name:").pack(pady=5)
customer_entry = tk.Entry(root)
customer_entry.pack(pady=5)

tk.Label(root, text="Product Name:").pack(pady=5)
product_entry = tk.Entry(root)
product_entry.pack(pady=5)

tk.Label(root, text="Quantity:").pack(pady=5)
quantity_entry = tk.Entry(root)
quantity_entry.pack(pady=5)

tk.Label(root, text="Price per Unit:").pack(pady=5)
price_entry = tk.Entry(root)
price_entry.pack(pady=5)

# Submit Button
tk.Button(root, text="Generate Bill", command=generate_bill).pack(pady=20)

# Run the application
root.mainloop()
