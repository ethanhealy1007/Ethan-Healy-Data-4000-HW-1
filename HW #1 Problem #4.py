# Exercise 4: Tax Bracket Determiner


def get_tax_bracket(income):
    if income < 0:
        return "Invalid income."
    elif income < 50000:
        return "Low (10%)"
    elif income < 100000:
        return "Medium (20%)"
    else:
        return "High (30%)"


answer = input("What's your annual income? ").strip()

if not answer.startswith("$"):
    print("Please include a dollar sign, e.g. $75000")
else:
    income = float(answer.strip("$"))  # remove the $ before converting
    bracket = get_tax_bracket(income)

    if income < 0:
        print(bracket)
    else:
        rate = 0.10 if income < 50000 else 0.20 if income < 100000 else 0.30
        print(f"Your bracket: {bracket}. Estimated tax: ${round(income * rate, 2)}")