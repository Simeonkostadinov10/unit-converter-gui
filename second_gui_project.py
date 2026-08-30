import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

def kilo_to_miles(kilos):
    return kilos * 0.621371

def hours_to_time(hours):
    minutes = hours * 60
    seconds = hours * 3600
    return minutes, seconds


class converterToMilesApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Miles converter")
        self.geometry("520x450")
        self.resizable(False, False)


        #Заглавие
        self.title_label = ctk.CTkLabel(self,text="Miles converter",font = ("Arial",20,"bold"))
        self.title_label.pack(pady=20)
        # Падащо меню за избор на режим
        self.mode_option = ctk.CTkOptionMenu(
            self,
            values=["Км към Мили", "Часове към Мин/Сек"],
            command=self.update_placeholder,
            width=320
        )
        self.mode_option.pack(pady=10)

        #Километри
        self.entry = ctk.CTkEntry(self, placeholder_text="Въведи километри", width=320)
        self.entry.pack(pady=5)

        #Бутон за конвертиране
        self.conv_btn = ctk.CTkButton(self,text = "Конвертирай",command= self.convert,width = 320)
        self.conv_btn.pack(pady=6)

        #Резултат
        self.result = ctk.CTkTextbox(self,width = 320,height = 80)
        self.result.pack(pady=5)

    def update_placeholder(self, choice):
        if choice == "Км към Мили":
            self.entry.configure(placeholder_text="Въведи километри")
        else:
            self.entry.configure(placeholder_text="Въведи часове")

    def convert(self):
        raw_val = self.entry.get().strip()

        if not raw_val:
            messagebox.showerror("Грешка", "Моля, въведи стойност!")
            return

        try:
            val = float(raw_val)
            mode = self.mode_option.get()

            self.result.delete("1.0", "end")

            if mode == "Км към Мили":
                miles = kilo_to_miles(val)
                self.result.insert("1.0", f"{val} км = {miles:.2f} мили")
            else:
                mins, secs = hours_to_time(val)
                self.result.insert("1.0", f"{val} ч. = {mins:.0f} мин ({secs:.0f} сек)")

        except ValueError:
            messagebox.showerror("Грешка", "Въведената стойност трябва да е число!")

if __name__ == "__main__":
    app = converterToMilesApp()
    app.mainloop()