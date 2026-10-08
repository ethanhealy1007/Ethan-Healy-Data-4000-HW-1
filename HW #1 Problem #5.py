# Exercise 5: Product Category Matcher

name = input("What's the product name? ").strip().lower()

match name:
    case "electronics" | "gadget":
        category = "High Margin"
    case _ if name.startswith("tech"):
        category = "High Margin"
    case "clothing" | "apparel":
        category = "Medium Margin"
    case "food" | "grocery":
        category = "Low Margin"
    case _:
        category = "Uncategorized - Review Needed"

print(f"Product: {name} | Category: {category}")