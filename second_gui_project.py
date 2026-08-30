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
        

        #Километри
        self.kilo_entry = ctk.CTkEntry(self,placeholder_text="Километри",width=320)
        self.kilo_entry.pack(pady=5)

        #Бутон за конвертиране
        self.conv_btn = ctk.CTkButton(self,text = "Конвертирай",command= self.convert,width = 320)
        self.conv_btn.pack(pady=6)

        #Резултат
        self.result = ctk.CTkTextbox(self,width = 320,height = 80)
        self.result.pack(pady=5)

    def convert(self):
        raw_val = self.kilo_entry.get().strip()

        if not raw_val:
            messagebox.showerror("Грешка", "Моля, въведи километри!")
            return

        try:
            km = float(raw_val)
            miles = kilo_to_miles(km)

            self.result.delete("1.0","end")
            self.result.insert("1.0",f"{km} км = {miles:.2f} мили")
        except ValueError:
            messagebox.showerror("Грешка", "Въведената стойност трябва да е число!")


if __name__ == "__main__":
    app = converterToMilesApp()
    app.mainloop()