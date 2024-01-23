import customtkinter
class Descanso(customtkinter.CTkFrame):
    def __init__(self, master):
        customtkinter.CTkFrame.__init__(self, master, fg_color='transparent')
        title_label = customtkinter.CTkLabel(master, text="Descans", font=("Helvetica", 70, "bold"), fg_color='transparent', text_color='white')
        title_label.grid()