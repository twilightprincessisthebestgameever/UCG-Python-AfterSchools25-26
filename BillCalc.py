# 📝 Restaurant Bill Splitter
# This program calculates the total bill with tax & tip,
# then splits the cost among a group of friends.

# Step 1: Ask the user for the bill amount
bill = float(input("Enter the total bill amount: $"))

# Step 2: Ask how many people are splitting the bill
people = int(input("How many people are sharing the bill? "))

# Step 3: Define tax and tip rates
tax_rate = 0.0825   # 8.25% sales tax
tip_rate = 0.15     # 15% tip

# Step 4: Calculate tax, tip, and total
tax = bill * tax_rate
tip = bill * tip_rate
total = bill + tax + tip

# Step 5: Calculate how much each person pays
per_person = total / people

# Step 6: Print results with clear formatting
print("\n💵 Restaurant Bill Splitter 💵")
print("-----------------------------")
print(f"Original Bill: ${bill:.2f}")
print(f"Sales Tax (8.25%): ${tax:.2f}")
print(f"Tip (15%): ${tip:.2f}")
print(f"Total Bill: ${total:.2f}")
print(f"Each Person Pays: ${per_person:.2f}")
print("-----------------------------")
