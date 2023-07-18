import tkinter as tk

root = tk.Tk()

# Create an entry box
entry_box = tk.Entry(root)

# Set the validate command
entry_box.config(validate="key", validatecommand=lambda x: only_numbers(x))

# Pack the entry box
entry_box.pack()

def only_numbers(text):
  """
  Validates that the text entered is only numbers.

  Args:
    text: The text that was entered.

  Returns:
    True if the text is only numbers, False otherwise.
  """
  try:
    int(text)
    return True
  except ValueError:
    return False

root.mainloop()