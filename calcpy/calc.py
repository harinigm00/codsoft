import tkinter as tk

class Calculator(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("400x450")  # Adjusted for an additional row for the clear button

        self.result_var = tk.StringVar(self, "0")

        # Display
        display = tk.Entry(self, textvar=self.result_var, font=("Arial", 24), bd=10, insertwidth=4, width=14, justify='right')
        display.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'  # Clear button added
        ]

        row = 1
        col = 0

        for button in buttons:
            tk.Button(self, text=button, width=5, height=2, font=("Arial", 18), command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, char):
        current = self.result_var.get()

        if char == 'C':
            self.result_var.set("0")
        elif char in {'+', '-', '*', '/'}:
            if current[-1] in {'+', '-', '*', '/'}:  # avoid double operators
                return
            self.result_var.set(current + char)
        elif char == '=':
            try:
                self.result_var.set(str(eval(current)))  # calculate the expression
            except Exception as e:
                self.result_var.set("Error")
        elif char == '.':
            if current[-1] == '.':  # avoid double dots
                return
            self.result_var.set(current + char)
        else:
            if current == "0" or current == "Error":
                self.result_var.set(char)
            else:
                self.result_var.set(current + char)


if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
