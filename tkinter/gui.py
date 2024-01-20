import tkinter as tk

def submit():
    # Clear the data.txt file
    with open("tkinter/data.txt", "w") as file:
        pass  # This will clear the file

    # Add your submit logic here
    for entry, label in zip(entries, labels):
        text = entry.get().strip()
        if text:  # Check if the text is non-empty
            with open("tkinter/data.txt", "a") as file:
                file.write(f"{text}\n")
            print(text)

    # Clear the entry widgets after submitting
    clear_entries()

    # Update entry widgets with data from the file
    load_data_into_entries()

def clear_entries():
    for entry in entries:
        entry.delete(0, tk.END)

def read_data_from_file():
    try:
        with open("tkinter/data.txt", "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found. No data available."

def load_data_into_entries():
    data_content = read_data_from_file().split('\n')
    for entry, label_text in zip(entries, data_content):
        entry.delete(0, tk.END)
        entry.insert(0, label_text)

# Create the main window
root = tk.Tk()
root.title("Submit Form")

# Set the window size to a larger size
root.geometry("800x800")

root.configure(bg="black")  # Set the background color to black

# Create and place six entry boxes with corresponding labels on the left
entries = []
labels = []
for i in range(6):
    label = tk.Label(root, text=f"Label {i+1}", bg="black", fg="white", font=("Arial", 12))
    label.grid(row=i, column=0, pady=10, padx=10, sticky="w")

    entry = tk.Entry(root, bg="white", fg="black", font=("Arial", 12))
    entry.grid(row=i, column=1, pady=10, padx=10, ipady=5, ipadx=10, sticky="ew")

    labels.append(label)
    entries.append(entry)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=submit, bg="white", fg="black", font=("Arial", 12))
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipady=5, ipadx=10, sticky="ew")

# Load data from file into entries when the application starts
load_data_into_entries()

# Run the Tkinter event loop
root.mainloop()
