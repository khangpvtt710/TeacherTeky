from tkinter import *
from tkinter import ttk

# Create window
root = Tk()
root.geometry("800x600")
root.title("Quang Converter")

# Title
label = Label(root, text="Converter", font=("Arial", 40, "bold"))
label.pack()

# Input field
number_entry = Entry(root, font=("Arial", 20))
number_entry.pack()

# Unit selection
unit_library = ["mm", "cm", "dm", "m", "dam", "hm", "km", "µm", "nm", "inch", "feet", "yard", "mile"]
unit_from = ttk.Combobox(root, values=unit_library, font=("Arial", 15))
unit_from.pack(pady=10)
unit_from.set("Select unit")

unit_to = ttk.Combobox(root, values=unit_library, font=("Arial", 15))
unit_to.pack(pady=10)
unit_to.set("Convert to")

# Conversion logic
def convert():
    try:
        value = float(number_entry.get())
        from_unit = unit_from.get()
        to_unit = unit_to.get()
       
        # Conversion factors (basic example)
        conversions = {
            "m": 1,
            
            "cm": 100,
            "mm": 1000,
            "km": 0.001,
            "nm": 1000000000,
            
            "inch": 39.3701,
            "feet": 3.28084,
            "yard": 1.09361,
            "mile": 0.000621371
        }

        if from_unit in conversions and to_unit in conversions:
            result = value * (conversions[to_unit] / conversions[from_unit])
            result_label.config(text=f"Result: {result:.4f} {to_unit}")
        else:
            result_label.config(text="Invalid unit selection")
   
    except ValueError:
        result_label.config(text="Enter a valid number")

# Convert Button
convert_btn = Button(root, text="Convert", font=("Arial", 20), command=convert)
convert_btn.pack(pady=20)

# Result Label
result_label = Label(root, text="Result: ", font=("Arial", 20))
result_label.pack()

# Run application
root.mainloop()