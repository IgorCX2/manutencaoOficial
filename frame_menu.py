import customtkinter
import os
from PIL import Image
class Menu:
    def __init__(self, master, navigate_to_page):
        #Imagens
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Sistema/Img")
        #logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Logo.png")), size=(190, 25))
        usuario = customtkinter.CTkImage(Image.open(os.path.join(image_path, "usuario.png")), size=(70, 70))
        
        #Menu
        navigation_frame = customtkinter.CTkFrame(master, corner_radius=20, fg_color="white")
        navigation_frame.grid(row=0, column=0, sticky="nsew")
        navigation_frame.grid_rowconfigure(8, weight=1)

        #navigation_frame_label = customtkinter.CTkLabel(navigation_frame, image=logo_image, compound="left", text="")
        #navigation_frame_label.grid(row=0, column=0, padx=60, pady=(20,5))
        div = customtkinter.CTkFrame(navigation_frame, corner_radius=0, fg_color="#D9D9D9", height=2)
        div.grid(row=1, column=0, pady=(15,15), sticky="nsew")

        users_container = customtkinter.CTkFrame(navigation_frame, corner_radius=0, fg_color="transparent")
        users_container.grid(row=2, column=0, padx=10, pady=(25,50), sticky="nsew")
        users_container.grid_columnconfigure((0,1), weight=1)
        foto_perfil = customtkinter.CTkLabel(users_container, image=usuario, compound="left", text="")
        foto_perfil.grid(row=0, column=0)
        users_info = customtkinter.CTkFrame(users_container, corner_radius=0,fg_color="transparent")
        users_info.grid(row=0, column=1, padx=(1,4))
        users_info.grid_rowconfigure((0,1), weight=1)
        users_info.grid_columnconfigure(1, weight=1)
        nome_user = customtkinter.CTkLabel(users_info, text="MANUTENÇÃO", fg_color="transparent", font=("Arial Black", 20))
        nome_user.grid(row=0, column=0, sticky="w")
        posto_user = customtkinter.CTkLabel(users_info, text="FABRICA 1", fg_color="transparent", font=("Arial", 15))
        posto_user.grid(row=1, column=0, sticky="w")

        buttonTitle=["home","mensagens","pendencias","maquinas","dashboard"]
        for row, buttom in enumerate(buttonTitle, start=3):
            menu = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, buttom+".png")),dark_image=Image.open(os.path.join(image_path, buttom+".png")), size=(20, 20))
            home_button = customtkinter.CTkButton(navigation_frame, corner_radius=0, height=40, command=lambda a=buttom: navigate_to_page(a, None), border_spacing=10, font=("Arial", 17, "bold"), text=buttom.capitalize(), fg_color="transparent", text_color="#999999", hover_color="#C9F1FF", image=menu, anchor="w")
            home_button.grid(row=row, column=0, sticky="ew", pady=2 ,padx=16)

        appearance_mode_menu = customtkinter.CTkSwitch(navigation_frame,  text="Microfone", font=("Arial", 15))
        appearance_mode_menu.grid(row=10, column=0, pady=20, sticky="s")
