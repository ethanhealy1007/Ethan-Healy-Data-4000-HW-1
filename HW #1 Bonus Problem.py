# Bonus Challenge: Integrated Decision Tool
# Concepts: multiple functions, bool return values, conditionals, match-case


def is_profitable(revenue, cost):
    """Return True if revenue exceeds cost."""
    return revenue > cost


def get_category(product):
    """Return the margin category for a product name using match-case."""
    match product:
        case "electronics" | "gadget":
            return "High Margin"
        case _ if product.startswith("tech"):
            return "High Margin"
        case "clothing" | "apparel":
            return "Medium Margin"
        case "food" | "grocery":
            return "Low Margin"
        case _:
            return "Uncategorized - Review Needed"


def get_suggestion(category):
    """Return an investment suggestion based on margin category."""
    match category:
        case "High Margin":
            return "Reinvest"
        case "Medium Margin":
            return "Hold and optimize costs"
        case "Low Margin":
            return "Focus on volume"
        case _:
            return "Review before investing"


def main():
    revenue = float(input("What's the revenue? "))
    cost = float(input("What's the cost? "))
    product = input("What's the product category? ").strip().lower()

    category = get_category(product)

    if is_profitable(revenue, cost):
        profit = revenue - cost
        print(f"Profit: ${profit:,.2f} | Category: {category}")
        print(f"Suggestion: {get_suggestion(category)}")
    else:
        print(f"Not profitable (loss of ${cost - revenue:,.2f}). Suggestion: Cut costs before investing.")


main()