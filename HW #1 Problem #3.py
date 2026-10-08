# Exercise 3: Customer Greeting Formatter


def format_greeting(name, title="Customer"):
    name = name.strip().title()  # strip removes spaces, title capitalizes
    if name == "":
        return "Hello, Valued Customer!"
    first_name = name.split()[0]  # split separates words, [0] is the first name
    return f"Hello, {first_name} ({title})!"


full_name = input("What's your full name? ")
print(format_greeting(full_name))