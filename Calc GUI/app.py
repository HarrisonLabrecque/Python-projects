from tkinter import *

class Calculator:
    def __init__(self, root):
        # Set up the main window
        self._root = root
        root.title("Calculator")              # Window title
        root.geometry('357x420')              # Fixed window size
        root.config(bg='gray')                # Background color
        root.resizable(False, False)          # Prevent resizing

        # Store the equation input and output
        self.equation = StringVar()
        self.entry_value = ''

        # Entry widget for displaying the equation/result
        Entry(root, width=17, bg='#fff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        # Define buttons: (label, x-coordinate, y-coordinate)
        buttons = [
            ('(', 0, 70), (')', 89, 70), ('%', 178, 70), ('/', 267, 70),
            ('7', 0, 140), ('8', 89, 140), ('9', 178, 140), ('*', 267, 140),
            ('4', 0, 210), ('5', 89, 210), ('6', 178, 210), ('-', 267, 210),
            ('1', 0, 280), ('2', 89, 280), ('3', 178, 280), ('+', 267, 280),
            ('0', 0, 350), ('.', 89, 350), ('C', 178, 350), ('=', 267, 350),
        ]

        # Create buttons and assign their actions
        for (text, x, y) in buttons:
            if text == 'C':
                command = self.clear  # Clear button
            elif text == '=':
                command = self.solve  # Equals button
            else:
                command = lambda val=text: self.show(val)  # Other input buttons
            # Create and place the button
            Button(
                root, width=11, height=4, text=text,
                relief='flat', bg='white', command=command
            ).place(x=x, y=y)

    def show(self, value):
        """Append the pressed button's value to the entry field."""
        self.entry_value += str(value)             # Add character to the input string
        self.equation.set(self.entry_value)        # Update display

    def clear(self):
        """Clear the entry field."""
        self.entry_value = ''                      # Reset input string
        self.equation.set(self.entry_value)        # Clear display

    def solve(self):
        """Evaluate the expression and display the result."""
        try:
            # Replace 'x' with '*' for multiplication, evaluate, and display the result
            result = str(eval(self.entry_value.replace('x', '*')))
            self.equation.set(result)              # Show result
            self.entry_value = result              # Update input with result for further operations
        except:
            self.equation.set("Error")             # Handle invalid input
            self.entry_value = ''                  # Reset on error

# Run the application
root = Tk()
calc = Calculator(root)
root.mainloop()
