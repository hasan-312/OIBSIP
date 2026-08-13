import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        height = float(entry_height.get())
        weight = float(entry_weight.get())

        if height <= 0 or weight <= 0:
            messagebox.showerror(
                "Input Error",
                "Height and weight must be positive numbers."
            )
            return

        # Calculate BMI
        bmi = weight / ((height / 100) ** 2)

        # Determine category
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        label_result.config(
            text=f"Your BMI is: {bmi:.2f}\nCategory: {category}"
        )

    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Please enter valid numbers for height and weight."
        )


# Main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x300")

# Height input
label_height = tk.Label(root, text="Enter your height (cm):")
label_height.pack(pady=5)

entry_height = tk.Entry(root)
entry_height.pack(pady=5)

# Weight input
label_weight = tk.Label(root, text="Enter your weight (kg):")
label_weight.pack(pady=5)

entry_weight = tk.Entry(root)
entry_weight.pack(pady=5)

# Calculate button
btn_calculate = tk.Button(
    root,
    text="Calculate BMI",
    command=calculate_bmi
)
btn_calculate.pack(pady=15)

# Result label
label_result = tk.Label(
    root,
    text="Your BMI will appear here",
    font=("Arial", 12)
)
label_result.pack(pady=10)

# Run application
root.mainloop()