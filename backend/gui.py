import os
import tkinter as tk

import FingerCounter as fc

file_path = "values.txt"


def save_values():
    # Function to get the values from the text boxes
    value1 = entry1.get()
    value2 = entry2.get()
    value3 = entry3.get()
    value4 = entry4.get()
    value5 = entry5.get()
    value6 = entry6.get()

    # Create or overwrite a text file to save the values
    with open("values.txt", "w") as file:
        file.write(f"{value1}\n")
        file.write(f"{value2}\n")
        file.write(f"{value3}\n")
        file.write(f"{value4}\n")
        file.write(f"{value5}\n")
        file.write(f"{value6}\n")

    # Display a message to indicate that values have been saved
    print("Values have been saved to values.txt")


def get_values():
    if os.path.exists(file_path):
        # Open the file in read mode
        with open(file_path, "r") as file:
            # Read all lines and collapse them into a single array
            all_lines = [line.strip() for line in file.readlines()]
        # Print the collapsed array
        return all_lines
    else:
        print(f"The file '{file_path}' does not exist.")


def load_values(entries):
    if os.path.exists(file_path):
        # Open the file in read mode
        with open(file_path, "r") as file:
            # Read and print each line
            for index, line in enumerate(file):
                entries[index].delete(0, tk.END)
                entries[index].insert(0, line.strip())
                # print(f"Line {index + 1}: {line.strip()}")
    else:
        print(f"The file '{file_path}' does not exist.")


# Create the main window
root = tk.Tk()
root.title("Text Box GUI")

# Create labels
label0 = tk.Label(root, text="Label 0:")
label1 = tk.Label(root, text="Label 1:")
label2 = tk.Label(root, text="Label 2:")
label3 = tk.Label(root, text="Label 3:")
label4 = tk.Label(root, text="Label 4:")
label5 = tk.Label(root, text="Label 5:")

# Position labels using the grid layout
label0.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
label1.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
label2.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
label3.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
label4.grid(row=4, column=0, padx=10, pady=5, sticky=tk.E)
label5.grid(row=5, column=0, padx=10, pady=5, sticky=tk.E)

# Create six entry widgets (text boxes)
entry1 = tk.Entry(root, width=30)
entry2 = tk.Entry(root, width=30)
entry3 = tk.Entry(root, width=30)
entry4 = tk.Entry(root, width=30)
entry5 = tk.Entry(root, width=30)
entry6 = tk.Entry(root, width=30)
entries = [entry1, entry2, entry3, entry4, entry5, entry6]

load_values(entries)

# Position the entry widgets using the grid layout
entry1.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
entry2.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
entry3.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)
entry4.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)
entry5.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)
entry6.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)

# Create a button to trigger the get_values function
button = tk.Button(root, text="Save Values", command=save_values)
button.grid(row=6, column=1, pady=10)

button = tk.Button(root, text="Launch Camera", command=fc.finger_tracker(get_values()))
button.grid(row=8, column=1, pady=10)

# Start the Tkinter event loop
root.mainloop()
