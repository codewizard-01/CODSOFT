import tkinter as tk


class Calculator:
    def __init__(self):
        self.digit = ""
        self.total = 0
        self.last_operation = None
        self.calc_main_window = tk.Tk()
        self.calc_main_window.geometry("260x260")
        self.calc_main_window.title("FastCalk")

        # Frames
        self.top_frame = tk.Frame(self.calc_main_window)
        self.first_row = tk.Frame(self.calc_main_window)
        self.second_row = tk.Frame(self.calc_main_window)
        self.third_row = tk.Frame(self.calc_main_window)
        self.fourth_row = tk.Frame(self.calc_main_window)
        self.message_frame = tk.Frame(self.calc_main_window)

        # Entries
        self.value = tk.StringVar()
        self.digit_display = tk.Entry(self.top_frame, width=30, textvariable=self.value)
        self.digit_display.pack(pady=10)

        # bottom part - buttons
        self.one = tk.Button(self.third_row, text="1", command=lambda: self.enter_digit("1"), width=5, height=2)
        self.two = tk.Button(self.third_row, text="2", command=lambda: self.enter_digit("2"), width=5, height=2)
        self.three = tk.Button(self.third_row, text="3", command=lambda: self.enter_digit("3"), width=5, height=2)
        self.four = tk.Button(self.second_row, text="4", command=lambda: self.enter_digit("4"), width=5, height=2)
        self.five = tk.Button(self.second_row, text="5", command=lambda: self.enter_digit("5"), width=5, height=2)
        self.six = tk.Button(self.second_row, text="6", command=lambda: self.enter_digit("6"), width=5, height=2)
        self.seven = tk.Button(self.first_row, text="7", command=lambda: self.enter_digit("7"), width=5, height=2)
        self.eight = tk.Button(self.first_row, text="8", command=lambda: self.enter_digit("8"), width=5, height=2)
        self.nine = tk.Button(self.first_row, text="9", command=lambda: self.enter_digit("9"), width=5, height=2)
        self.zero = tk.Button(self.fourth_row, text="0", command=lambda: self.enter_digit("0"), width=5, height=2)
        self.point = tk.Button(self.fourth_row, text="=", command=self.equal, width=5, height=2, bg="green")
        self.clean = tk.Button(self.fourth_row, text="C", command=self.clean, width=5, height=2, bg="red")
        self.sum = tk.Button(self.fourth_row, text="+", command=self.add, width=5, height=2)
        self.subtract = tk.Button(self.third_row, text="-", command=self.subtract, width=5, height=2)
        self.multiply = tk.Button(self.second_row, text="X", command=self.multiply, width=5, height=2)
        self.divide = tk.Button(self.first_row, text="/", command=self.divide, width=5, height=2)

        # Packing the buttons
        self.one.pack(side="left")
        self.two.pack(side="left")
        self.three.pack(side="left")
        self.four.pack(side="left")
        self.five.pack(side="left")
        self.six.pack(side="left")
        self.seven.pack(side="left")
        self.eight.pack(side="left")
        self.nine.pack(side="left")
        self.clean.pack(side="left")
        self.zero.pack(side="left")
        self.point.pack(side="left")
        self.sum.pack(side="left")
        self.subtract.pack(side="left")
        self.multiply.pack(side="left")
        self.divide.pack(side="left")

        # My message
        self.message = tk.Label(self.message_frame, text="Made with ❤ by Esmatullah.")
        self.message.pack(pady=10)

        # Pack Frames
        self.top_frame.pack()
        self.first_row.pack()
        self.second_row.pack()
        self.third_row.pack()
        self.fourth_row.pack()
        self.message_frame.pack()

        tk.mainloop()

    def enter_digit(self, digit):
        self.digit += digit
        self.value.set(self.digit)

    def one(self):
        self.digit += "1"
        self.value.set(str(self.digit))

    def two(self):
        self.digit += "2"
        self.value.set(str(self.digit))

    def three(self):
        self.digit += "3"
        self.value.set(str(self.digit))

    def four(self):
        self.digit += "4"
        self.value.set(str(self.digit))

    def five(self):
        self.digit += "5"
        self.value.set(str(self.digit))

    def six(self):
        self.digit += "6"
        self.value.set(str(self.digit))

    def seven(self):
        self.digit += "7"
        self.value.set(str(self.digit))

    def eight(self):
        self.digit += "8"
        self.value.set(str(self.digit))

    def nine(self):
        self.digit += "9"
        self.value.set(str(self.digit))

    def zero(self):
        self.digit += "0"
        self.value.set(str(self.digit))

    def point(self):
        pass

    def clean(self):
        self.digit = ""
        self.total = 0
        self.last_operation = None
        self.value.set("0")

    def add(self):
        num = float(self.digit)
        if self.last_operation is None:
            self.total = num
        else:
            self.perform_last_operation(num)
        self.last_operation = "add"
        self.digit = ""
        self.value.set(str(self.total))

    def subtract(self):
        num = float(self.digit)
        if self.last_operation is None:
            self.total = num
        else:
            self.perform_last_operation(num)
        self.last_operation = "subtract"
        self.digit = ""
        self.value.set(str(self.total))

    def multiply(self):
        num = float(self.digit)
        if self.last_operation is None:
            self.total = num
        else:
            self.perform_last_operation(num)
        self.last_operation = "multiply"
        self.digit = ""
        self.value.set(str(self.total))

    def divide(self):
        num = float(self.digit)
        if self.last_operation is None:
            self.total = num
        else:
            self.perform_last_operation(num)
        self.last_operation = "divide"
        self.digit = ""
        self.value.set(str(self.total))

    def perform_last_operation(self, num):
        if self.last_operation == "add":
            self.total += num
        elif self.last_operation == "subtract":
            self.total -= num
        elif self.last_operation == "multiply":
            self.total *= num
        elif self.last_operation == "divide":
            if num != 0:  # Avoid division by zero
                self.total /= num
            else:
                self.value.set("Error")
                self.total = 0

    def equal(self):
        if self.last_operation:
            num = int(self.digit)
            self.perform_last_operation(num)
            self.last_operation = None
        self.value.set(str(self.total))


if __name__ == "__main__":
    Calculator()