import random
import string
import tkinter as tk


# Step 1: Password generator function
def generate_password(length=12, uppercase=True, lowercase=True, digits=True, special_chars=True):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not characters:
        print("Error: At least one character must be selected.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Step 2: Tkinter GUI
def display_password():
    try:
        # Get the length from the input field
        password_length = int(length_entry.get())
    except ValueError:
        result_text.config(state="normal")
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Please enter a valid number for length.")
        result_text.config(state="disabled")
        return

    # Get the state of the checkboxes
    include_uppercase = uppercase_var.get()
    include_lowercase = lowercase_var.get()
    include_digits = digits_var.get()
    include_special_chars = special_chars_var.get()

    # Generate the password using the function
    generated_password = generate_password(
        length=password_length,
        uppercase=include_uppercase,
        lowercase=include_lowercase,
        digits=include_digits,
        special_chars=include_special_chars
    )

    # Display the generated password in the result_text widget
    result_text.config(state="normal")
    result_text.delete("1.0", tk.END)
    if generated_password:
        result_text.insert(tk.END, generated_password)
    else:
        result_text.insert(tk.END, "Password generation failed.")
    result_text.config(state="disabled")


# Step 3: GUI Setup
root = tk.Tk()
root.title("Password Generator")

# Set initial size of the window
root.geometry("400x400")

# Label and entry for password length
length_label = tk.Label(root, text="Enter password length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

# Checkboxes for password options
uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_chars_var = tk.BooleanVar(value=True)

uppercase_checkbox = tk.Checkbutton(root, text="Include Uppercase", variable=uppercase_var)
uppercase_checkbox.pack()

lowercase_checkbox = tk.Checkbutton(root, text="Include Lowercase", variable=lowercase_var)
lowercase_checkbox.pack()

digits_checkbox = tk.Checkbutton(root, text="Include Digits", variable=digits_var)
digits_checkbox.pack()

special_chars_checkbox = tk.Checkbutton(root, text="Include Special Characters", variable=special_chars_var)
special_chars_checkbox.pack()

# Button to generate the password
generate_button = tk.Button(root, text="Generate Password", command=display_password)
generate_button.pack()

# Text widget to display the generated password
result_text = tk.Text(root, height=5, state="disabled")
result_text.pack()

# Run the main loop to keep the window open
root.mainloop()
