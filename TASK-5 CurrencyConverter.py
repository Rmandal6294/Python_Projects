# ================================== Currency Converter =======================================
import tkinter as tk
from tkinter import messagebox
import requests

def convert_currency(amount, fromCurrency, toCurrency):
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{fromCurrency.upper()}"
        response = requests.get(url)
        data = response.json()
        
        if "rates" not in data:
            messagebox.showerror("Error", "⚠️ Flailed to Fetching Exchange Rates or Invalid Currency")
            return
        rates = data["rates"]
        if toCurrency.upper() not in rates:
            messagebox.showerror("Error", "⚠️ Invalid Currency.")
            return 
        
        rate = rates[toCurrency.upper()]
        converted_amount = amount * rate
        result =f"{amount} {fromCurrency.upper()} = {converted_amount:.2f} {toCurrency.upper()}"
        return result
        
    except ValueError:
        messagebox.showwarning("Input Error", "⚠️ Please enter a valid number.")
        
    except Exception as e:
        messagebox.showerror("Error ⚠️", e)

c = convert_currency(100, "usd", "Inr")
print(c)

def on_convert():
    try:
        amountValue = float(amount.get())     
    except ValueError:
        messagebox.showwarning("Input Error", "⚠️ Please enter a valid number.")
        return
    result = convert_currency(amountValue, fromCurrency.get(), toCurrency.get())
    if result:
        result_label.config(text=result)


root = tk.Tk()
root.title("Currency Converter")
root.geometry("410x520")
root.config(bg = "#0f1117")

title = tk.Label(root, text = " 💱 Currency Converter ",font=("Georgia", 20, "bold"), bg="#394142", fg="#f0c040", width=40)
title.pack(pady=20)
tk.Label(root, text = "Enter Your Amount:", font=("Georgia", 10, "bold"), bg="#0f1117", fg="#f0c040",).pack()
amount = tk.Entry(root, font=("Courier", 13), bg="#252836", fg="#f0f0f0",)
amount.pack(pady=10)
tk.Label(root, text = "From Currency (ex: USD):", font=("Georgia", 10, "bold"), bg="#0f1117", fg="#f0c040",).pack()
fromCurrency = tk.Entry(root, font=("Courier", 13), bg="#252836", fg="#f0f0f0",)
fromCurrency.pack(pady=10)
tk.Label(root, text = "To Currency (ex: INR):", font=("Georgia", 10, "bold"), bg="#0f1117", fg="#f0c040",).pack()
toCurrency = tk.Entry(root, font=("Courier", 13), bg="#252836", fg="#f0f0f0",)
toCurrency.pack(pady=10)
convert_btn = tk.Button(root, text="Convert ->", font=("Georgia", 13, "bold"), bg="#f0c040", fg="#0f1117", command=lambda: on_convert(),)
convert_btn.pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 12),bg="#0d2b1e", fg="#44cc88", bd = 2, width=30)
result_label.pack(pady=10)

root.mainloop()
