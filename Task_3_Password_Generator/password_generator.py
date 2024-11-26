from random import randint
import customtkinter as ctk
from tkinter import messagebox


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x420")
        self.title("JuiceHackers")
        self.root_color = self.cget("fg_color")

        # Frames
        self.password_frame = ctk.CTkFrame(self, fg_color=self.root_color)
        self.second_frame = ctk.CTkFrame(self, fg_color=self.root_color)
        self.third_frame = ctk.CTkFrame(self, fg_color=self.root_color)

        # Widgets
        self.title_label = ctk.CTkLabel(self, text="Password Generator",
                                        font=("Arial", 22, "bold"))
        self.title_label.pack(pady=10)

        # Slider and Entry
        self.slider_label = ctk.CTkLabel(self.second_frame, text="Password Length", font=("Arial", 14))
        self.slider_label.grid(row=0, column=0, padx=5, pady=5)

        self.slider = ctk.CTkSlider(self.second_frame, from_=0, to=100, command=self.update_number)
        self.slider.set(0)
        self.slider.grid(row=0, column=1, padx=10, pady=5)

        self.number_entry = ctk.CTkEntry(self.second_frame, width=50, font=("Arial", 14))
        self.number_entry.grid(row=0, column=2, padx=10, pady=5)

        # Button
        self.generate_button = ctk.CTkButton(self.third_frame, text="Generate Password", command=self.generate_password,
                                             font=("Arial", 16), height=36)
        self.generate_button.pack(pady=15)

        self.message = ctk.CTkLabel(self, text="Made with ❤ by Esmat.", font=("sans-serif", 9))
        self.message.pack(side="bottom")
        # Pack the Frames
        self.second_frame.pack(pady=10)
        self.third_frame.pack(pady=10)
        self.password_frame.pack()

    def show_error(self):
        messagebox.showerror("Error", "Please choose the length of your password.")

    def update_number(self, value):
        # Update the entry with the value of the slider
        self.number_entry.delete(0, ctk.END)
        self.number_entry.insert(0, str(int(float(value))))

    def generate_password(self):
        # Generate and display the password
        if self.number_entry.get():
            characters_count = int(self.number_entry.get())
            generated_password = ""
            while len(generated_password) < characters_count:
                generated_password += chr(randint(33, 127))

            # Display the Generated Password
            display_password = ctk.CTkLabel(self.password_frame, text=generated_password,
                                            font=("Arial", 14))
            display_password.pack(pady=10)
        else:
            self.show_error()


if __name__ == "__main__":
    app = App()
    app.mainloop()
