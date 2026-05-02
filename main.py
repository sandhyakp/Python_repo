def calculate_bill(items, discount_percent=0, tax_percent=0):
    # Step 1: total nikalna
    total = sum(items)
    
    # Step 2: discount lagana (agar diya ho)
    discount = (total * discount_percent) / 100
    after_discount = total - discount
    
    # Step 3: tax lagana
    tax = (after_discount * tax_percent) / 100
    final_total = after_discount + tax
    
    return final_total


# Example items (prices)
items = [10, 30, 50]  # Pen + Notebook + Bag

# bill calculate karo
bill_amount = calculate_bill(items, discount_percent=10, tax_percent=5)

print("Final Bill:", bill_amount)
