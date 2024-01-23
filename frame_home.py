
import customtkinter
class Home(customtkinter.CTkFrame):
    def __init__(self, master, navigate_to_page):
        customtkinter.CTkFrame.__init__(self, master, fg_color='transparent')
        nome_user = customtkinter.CTkLabel(master, text="OLÁ MANUTENÇÃO", fg_color="transparent", font=("Arial Black", 70))
        nome_user.grid(row=1, column=0, sticky="w", pady=(50,10))
        versao_app = customtkinter.CTkLabel(master, text="V1.000.1-2/2024", fg_color="transparent", text_color="#A6A6A6", font=("Arial", 20, "bold"))
        versao_app.grid(row=2, column=0, sticky="w")
        titulo_tarefas = customtkinter.CTkLabel(master, text="TAREFAS", fg_color="transparent", font=("Arial Black", 50))
        titulo_tarefas.grid(row=3, column=0, sticky="w", pady=(70,10))
        buttons_cod=[["0405","0406","0407","0408","0403","0706"],["0502","0504","0505","0506","0404","0418"]]
        buttons_txt=[["Elétrico","Hidráulico","Mecânico","Pneumático","Análise","Liberar"],["Pre-Elétrico","Pre-Hidráulico","Pre-Mecânico","Pre-Pneumático","BCR","Ajus.Parâmetro"]]
        main_frame = customtkinter.CTkFrame(master, fg_color='transparent')
        main_frame.grid(row=4, column=0, sticky="w")
        for i in range(2):
            button_frame = customtkinter.CTkFrame(main_frame, fg_color='transparent')
            button_frame.pack()
            for c in range(len(buttons_cod[i])):
                button = customtkinter.CTkButton(button_frame, text=buttons_txt[i][c],command=lambda pag='pcf', cod=buttons_cod[i][c]: navigate_to_page(pag,cod), width=153, height=120, font=("Helvetica", 18, "bold"), fg_color='white',hover_color="#53D2FF", text_color="#363636")
                button.pack(side='left', padx=8, pady=8)

        button_frame = customtkinter.CTkFrame(main_frame, fg_color='transparent')
        button_frame.pack()
        button = customtkinter.CTkButton(button_frame, text="SISTEMA LOTTO", font=("Helvetica", 18, "bold"), width=660,command=lambda pag='lotto': navigate_to_page(pag, None), height=120, fg_color='white', hover_color="#53D2FF", text_color="#363636")
        button.pack(side='left', padx=8, pady=8)
        button = customtkinter.CTkButton(button_frame, text="BCR", font=("Helvetica", 18, "bold"), width=153, height=120, fg_color='white', hover_color="#53D2FF", text_color="#363636")
        button.pack(side='left', padx=8, pady=8)
        button = customtkinter.CTkButton(button_frame, text="LIMPEZA", font=("Helvetica", 18, "bold"), width=153, height=120, fg_color='white', hover_color="#53D2FF", text_color="#363636")
        button.pack(side='left', padx=8, pady=8)
        button_frame = customtkinter.CTkFrame(main_frame, fg_color='transparent')
        button_frame.pack()
        button = customtkinter.CTkButton(button_frame, text="PENDÊNCIAS DO TURNO", font=("Helvetica", 18, "bold"), width=995, height=120, fg_color='white', hover_color="#53D2FF", text_color="#363636")
        button.pack(side='left', padx=8, pady=8)
