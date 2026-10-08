# Exercise 1: Profit Margin Calculator
# Concepts: input, float variables, arithmetic, f-string formatting

# Get revenue and cost from the user and convert them to floats
revenue = float(input("What's the revenue? "))
cost = float(input("What's the cost? "))

# Profit is revenue minus cost
profit = revenue - cost

# Only calculate margin if revenue is positive (avoids dividing by zero)
if revenue > 0:
    margin = (profit / revenue) * 100
    # :,.2f adds thousands separators and rounds to 2 decimals
    print(f"Profit: ${profit:,.2f} | Margin: {margin:.2f}%")
else:
    print("Invalid revenue.")