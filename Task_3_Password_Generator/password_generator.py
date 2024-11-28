import customtkinter
from tkinter import messagebox
from random import randint

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("SuperPassword")
        self.geometry("700x230")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.display_frame = customtkinter.CTkFrame(self)
        self.display_frame.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="new")
        self.password_frame = customtkinter.CTkFrame(self.display_frame, height=30)
        self.password_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=(10, 10), sticky="ew")

        self.label = customtkinter.CTkLabel(self.display_frame, text="Generate a password",
                                                   font=("Arial", 14, "bold"))
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.slider_label = customtkinter.CTkLabel(self.display_frame, text="Characters", font=("Arial", 14))
        self.slider_label.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="w")

        self.slider = customtkinter.CTkSlider(self.display_frame, from_=0, to=100, command=self.update_number)
        self.slider.set(0)
        self.slider.grid(row=1, column=1, padx=10, pady=5)

        self.number_entry = customtkinter.CTkEntry(self.display_frame, width=50, font=("Arial", 14))
        self.number_entry.grid(row=1, column=2, padx=10, pady=5)

        # Checkbox frame with its content
        self.checkbox_frame = customtkinter.CTkFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        self.checkbox_1 = customtkinter.CTkCheckBox(self.checkbox_frame, text="Letters")
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_2 = customtkinter.CTkCheckBox(self.checkbox_frame, text="Numbers")
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_3 = customtkinter.CTkCheckBox(self.checkbox_frame, text="signs")
        self.checkbox_3.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")

        # Generate password button
        self.button = customtkinter.CTkButton(self.display_frame, text="Generate Password",
                                              command=self.generate_password)
        self.button.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

    def show_error(self):
        messagebox.showerror("Error", "Please choose the length of your password.")

    def update_number(self, value):
        # Update the entry with the value of the slider
        self.number_entry.delete(0, customtkinter.END)
        self.number_entry.insert(0, str(int(float(value))))

    def generate_password(self):
        # Generate and display the password
        if self.number_entry.get():
            characters_count = int(self.number_entry.get())
            generated_password = ""
            while len(generated_password) < characters_count:
                generated_password += chr(randint(33, 127))

            # Display the Generated Password
            for widget in self.password_frame.winfo_children():
                widget.destroy()
            display_password = customtkinter.CTkLabel(self.password_frame, text=generated_password,
                                            font=("Arial", 14))
            display_password.pack(pady=10)
        else:
            self.show_error()


app = App()
app.mainloop()