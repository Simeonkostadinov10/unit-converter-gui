import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

def kilo_to_miles(kilos):
    return kilos * 0.621371

def miles_to_kilos(miles):
    return miles / 0.621371

def minutes_to_time(minutes):
    hours = minutes / 60
    seconds = minutes * 60
    return hours, seconds

def hours_to_time(hours):
    minutes = hours * 60
    seconds = hours * 3600
    return minutes, seconds

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32



class converterToMilesApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Miles converter")
        self.geometry("450x400")
        self.resizable(False, False)


        #Заглавие
        self.title_label = ctk.CTkLabel(self,text="Miles converter",font = ("Arial",20,"bold"))
        self.title_label.pack(pady=20)
        # Падащо меню за избор на режим
        self.mode_option = ctk.CTkOptionMenu(
            self,
            values=["Км към Мили", "Часове към Мин/Сек","Фаренхайт към Целзий"],
            command=self.update_placeholder,
            width=320
        )
        self.mode_option.pack(pady=10)

        self.is_reversed = False


        #Километри
        self.entry = ctk.CTkEntry(self, placeholder_text="Въведи километри", width=320)
        self.entry.pack(pady=5)

        #Бутон за конвертиране
        self.conv_btn = ctk.CTkButton(self,text = "Конвертирай",command= self.convert,width = 320)
        self.conv_btn.pack(pady=6)

        #Бутон за размяна
        self.swap_btn = ctk.CTkButton(
            self,
            text="⇄ Размени посоката",
            command=self.toggle_direction,
            width=320,
        )
        self.swap_btn.pack(pady=5)

        #Резултат
        self.result = ctk.CTkTextbox(self,width = 320,height = 80)
        self.result.pack(pady=5)

        self.bind("<Return>", lambda event: self.convert())

    def update_placeholder(self, choice):
        if self.is_reversed is False:
            if choice == "Км към Мили":
                self.entry.configure(placeholder_text="Въведи километри")
            elif choice == "Часове към Мин/Сек":
                self.entry.configure(placeholder_text="Въведи часове")
            elif choice == "Фаренхайт към Целзий":
                self.entry.configure(placeholder_text="Въведи градуси (°F)")
        else:
            if choice == "Км към Мили":
                self.entry.configure(placeholder_text="Въведи мили")
            elif choice  == "Часове към Мин/Сек":
                self.entry.configure(placeholder_text="Въведи Мин/Сек")
            elif choice == "Фаренхайт към Целзий":
                self.entry.configure(placeholder_text="Целзий към километри")

    def toggle_direction(self):
        self.is_reversed = not self.is_reversed
        self.update_placeholder(self.mode_option.get())

    def convert(self):
        raw_val = self.entry.get().strip()

        # 1. Проверка за празно поле
        if not raw_val:
            messagebox.showerror("Грешка", "Моля, въведи стойност!")
            return

        # 2. Валидация и изчисления
        try:
            val = float(raw_val)
            mode = self.mode_option.get()

            # Изчистване на текстовото поле
            self.result.delete("1.0", "end")

            # --- Километри <-> Мили ---
            if mode == "Км към Мили":
                if not self.is_reversed:
                    miles = kilo_to_miles(val)
                    self.result.insert("1.0", f"{val} км = {miles:.2f} мили")
                else:
                    km = miles_to_kilos(val)
                    self.result.insert("1.0", f"{val} мили = {km:.2f} км")

            # --- Часове <-> Минути/Секунди ---
            elif mode == "Часове към Мин/Сек":
                if not self.is_reversed:
                    mins, secs = hours_to_time(val)
                    self.result.insert(
                        "1.0", f"{val} ч. = {mins:.0f} мин ({secs:.0f} сек)"
                    )
                else:
                    hours, secs = minutes_to_time(val)
                    self.result.insert(
                        "1.0", f"{val} мин = {hours:.2f} ч. ({secs:.0f} сек)"
                    )

            # --- Градуси (Фаренхайт <-> Целзий) ---
            elif mode == "Фаренхайт към Целзий":
                if not self.is_reversed:
                    celsius = fahrenheit_to_celsius(val)
                    self.result.insert("1.0", f"{val}°F = {celsius:.2f}°C")
                else:
                    fahr = celsius_to_fahrenheit(val)
                    self.result.insert("1.0", f"{val}°C = {fahr:.2f}°F")

        except ValueError:
            messagebox.showerror(
                "Грешка", "Въведената стойност трябва да е число!"
            )

if __name__ == "__main__":
    app = converterToMilesApp()
    app.mainloop()