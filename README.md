# 🧾 Smart Billing System using Python

A simple and beginner-friendly billing system built using Python.  
This project demonstrates how basic programming concepts like functions, return, and user input can be used to solve real-world billing problems.

---

## 🚀 Features

- ➕ Add multiple item prices
- 💰 Automatic total calculation
- 🎁 Discount support (optional)
- 🧾 Tax calculation
- 🖥️ Simple console-based interface
- 🔁 Reusable function-based design

---

## 🧠 How It Works

1. User enters item prices
2. System calculates total bill
3. Discount is applied (if provided)
4. Tax is added
5. Final bill is displayed

---

## 💻 Code Example

```python
def calculate_bill(items, discount_percent=0, tax_percent=0):
    total = sum(items)
    
    discount = (total * discount_percent) / 100
    after_discount = total - discount
    
    tax = (after_discount * tax_percent) / 100
    final_total = after_discount + tax
    
    return final_total


items = [10, 30, 50]

bill = calculate_bill(items, discount_percent=10, tax_percent=5)

print("Final Bill:", bill)
