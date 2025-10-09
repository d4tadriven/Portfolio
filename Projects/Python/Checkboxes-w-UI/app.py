import customtkinter

class checkboxes(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.checkbox1 = customtkinter.CTkCheckBox(self, text="Checkbox 1")
        self.checkbox1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox2 = customtkinter.CTkCheckBox(self, text="Checkbox 2")
        self.checkbox2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox3 = customtkinter.CTkCheckBox(self, text="Checkbox 3")
        self.checkbox3.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")

    def get(self):
        checked_checkboxes = []
        if self.checkbox1.get() == 1:
            checked_checkboxes.append(self.checkbox1.cget("text"))
        if self.checkbox2.get() == 1:
            checked_checkboxes.append(self.checkbox2.cget("text"))
        if self.checkbox3.get() == 1:
            checked_checkboxes.append(self.checkbox3.cget("text"))
        return checked_checkboxes

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Stijn's app!")
        self.geometry("400x180")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.checkbox_frame = checkboxes(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")

        self.button = customtkinter.CTkButton(self, text = "Hi", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    def button_callback(self):
        print("checked checkboxes: ", self.checkbox_frame.get())

app = App()
app.mainloop()