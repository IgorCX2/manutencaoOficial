import customtkinter
from frame_descanso import Descanso
from frame_home import Home
from frame_pcf import Pcf
from frame_carregando import Carregando
from frame_lotto import Lotto
from app_functions import *
from frame_menu import Menu
class Aplicativo(customtkinter.CTk):
    def __init__(self):
        customtkinter.CTk.__init__(self)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.pagina_ativa = None
        self.tempo_inativo = 0
        self.statusPFC = "Nada"
        self.temporizador_contador = 0
        self.bind("<Motion>", lambda event: reiniciar_temporizador(self, event))

        #Pagina Menu
        self.menu = Menu(self, self.navigate_to_page)

        #Paginas Configs
        self.pages_container = customtkinter.CTkScrollableFrame(self, corner_radius=0, fg_color="transparent")
        self.pages_container.grid_columnconfigure(0, weight=1)
        self.pages_container.grid(row=0, column=1, sticky="nsew", padx=(100,0))

        self.navigate_to_page("home", None)

    def Temporizador(self):
        self.after(1000, lambda: Temporizador(self))

    def navigate_to_page(self, page_name, cod):
        for widget in self.pages_container.winfo_children():
            widget.destroy()

        #Adicionar caminho das paginas
        self.pagina_ativa = page_name
        match page_name:
            case "home":
                self.page_name = Home(self.pages_container, self.navigate_to_page)
            case "descanso":
                self.page_name = Descanso(self.pages_container)
            case "lotto":
                self.page_name = Lotto(self.pages_container)
            case "pcf":
                self.page_name = Pcf(self.pages_container, self.navigate_to_page, cod)
            case "carregando":
                self.page_name = Carregando(self.pages_container)
            case _:
                self.page_name = Descanso(self.pages_container)
            
if __name__ == "__main__":
    app = Aplicativo()
    app.Temporizador()
    app.mainloop()
