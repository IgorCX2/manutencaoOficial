import customtkinter
import tkinter as tk
from tkinter import messagebox
from functions_share import mostrar_usuarios, buscar_pessoa_registro, carregar_maquina, buscar_maquina_nome
from PIL import Image
from globals import nomeSelecionado
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import tkinter as tk
from threading import Thread
from selenium.webdriver.chrome.options import Options
import json
import os
from datetime import datetime

def resetarCoresBotoes(janela):
    for widget_pai in janela.winfo_children():
        for widget in widget_pai.winfo_children():
            if isinstance(widget_pai,customtkinter.CTkButton):
                widget_pai.configure(fg_color="white")

def mudarPessoa(pessoa, janela, frame_1):
    global nomeSelecionado
    nomeSelecionado = pessoa
    resetarCoresBotoes(frame_1)
    janela.configure(fg_color="blue")

class ToplevelWindow(customtkinter.CTkToplevel):#Desativado
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x150")
        self.attributes('-topmost', True)
        self.label = customtkinter.CTkLabel(self, text="..CARREGANDO..",font=("Arial Black", 50, "bold"))
        self.label.pack(padx=20, pady=20)
        self.progressbar = customtkinter.CTkProgressBar(self, orientation="horizontal", width=500)
        self.progressbar.pack()
        self.progressbar.configure(mode="indeterminnate")
        self.progressbar.start()


class Pcf(customtkinter.CTkFrame):
    def __init__(self, master, navigate_to_page, cod=None):
        self.maquinaLista = carregar_maquina()
        list_pcf={
            None: "",
            "0405": "Elétrico",
            "0406": "Hidráulico",
            "0407": "Mecânico",
            "0408": "Pneumático",
            "0403": "Análise",
            "0706": "Liberar",
            "0502": "Pre-Elétrico",
            "0504": "Pre-Hidráulico",
            "0505": "Pre-Mecânico",
            "0506": "Pre-Pneumático",
            "0404": "BCR",
            "0418": "Ajus.Parâmetro",
        }
        customtkinter.CTkFrame.__init__(self, master, fg_color='transparent')
        title_label = customtkinter.CTkLabel(master, text=str(list_pcf[cod]).upper(), font=("Arial Black", 70, "bold"), fg_color='transparent')
        title_label.pack(pady=50)

        frame_total = customtkinter.CTkFrame(master,fg_color='transparent',width=501)
        frame_total.pack()

        user_frame = customtkinter.CTkFrame(frame_total, fg_color='transparent')
        user_frame.pack()
        userbox_frame = customtkinter.CTkFrame(user_frame, fg_color='transparent')
        userbox_frame.pack()
        default_frame = userbox_frame
        userbox_novo_frame = None
        usuario_carregados = mostrar_usuarios(cod)
        if usuario_carregados:
            for i in range(len(usuario_carregados)):
                if usuario_carregados[i]["Nome"] != None: 
                    if(i == 6):
                        userbox_novo_frame = customtkinter.CTkFrame(user_frame, fg_color='transparent',width=950)
                        userbox_novo_frame.pack()
                        default_frame = userbox_novo_frame
                    caminho_imagem = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Sistema', 'Img', 'users', usuario_carregados[i]["Imagem"])
                    my_image = customtkinter.CTkImage(light_image=Image.open(caminho_imagem), dark_image=Image.open(caminho_imagem), size=(90, 90))
                    button_user = customtkinter.CTkButton(default_frame, image=my_image, compound="top", text=usuario_carregados[i]["Nome"].split(" ")[0],font=("Helvetica", 18, "bold"), fg_color='white',hover_color="#C9F1FF", text_color='black')
                    button_user.configure(command=lambda arg1=usuario_carregados[i]["Registro"], arg2=button_user, arg3=userbox_frame: mudarPessoa(arg1, arg2, arg3))
                    button_user.pack(side='left', padx=8, pady=5)

        digitMaquina_frame = customtkinter.CTkFrame(frame_total, fg_color='transparent')
        digitMaquina_frame.pack(pady=5)
        if cod != '0706':
            text = "Maquina"
        else:
            text = "Solicitação"
        maquinatitle_label = customtkinter.CTkLabel(digitMaquina_frame, justify="left", text=text, font=("Helvetica", 20, "bold"), fg_color='transparent', width=950, anchor="w", text_color='black')
        maquinatitle_label.pack(pady=8)
        if cod != '0706':
            self.digt_maquina = customtkinter.CTkEntry(digitMaquina_frame, border_width=0,fg_color='white', placeholder_text="Inserir Maquina", width=950, height=35, font=("Helvetica", 20))
            self.digt_maquina.pack()
            self.digt_maquina.bind("<KeyRelease>", self.sugestao_maquina)
            self.maquinasugestao_label = customtkinter.CTkFrame(digitMaquina_frame, width=950,height=5,fg_color='transparent')
            self.maquinasugestao_label.pack(side='left')

        digitComment_frame = customtkinter.CTkFrame(frame_total, fg_color='transparent')
        digitComment_frame.pack(pady=14)

        if cod == '0706':
            self.digt_maquina = customtkinter.CTkEntry(digitMaquina_frame, border_width=0,fg_color='white', placeholder_text="Inserir Solicitacao", width=950, height=35, font=("Helvetica", 20))
            self.digt_maquina.pack()
            self.digt_maquina.bind("<KeyRelease>", self.buscar_solicitacao)
            self.maquinasugestao_label = customtkinter.CTkFrame(digitMaquina_frame, width=950,height=5,fg_color='transparent')
            self.maquinasugestao_label.pack(side='left')
            bloco_sintoma = customtkinter.CTkFrame(digitComment_frame, fg_color='transparent')
            bloco_sintoma.pack(side="left")
            sintomatitle_label = customtkinter.CTkLabel(bloco_sintoma, justify="left", text="Problema encontrado", font=("Helvetica", 20, "bold"),width=315, anchor="w", text_color='black')
            sintomatitle_label.pack(pady=10, padx=2)
            self.digt_sintoma = customtkinter.CTkTextbox(bloco_sintoma, width=300, font=("Helvetica", 20))
            self.digt_sintoma.pack()

            bloco_causa = customtkinter.CTkFrame(digitComment_frame, fg_color='transparent')
            bloco_causa.pack(side="left")
            causatitle_label = customtkinter.CTkLabel(bloco_causa, justify="left", text="Diagnostico", font=("Helvetica", 20, "bold"), width=315, anchor="w", text_color='black')
            causatitle_label.pack(pady=10, padx=2)
            self.digt_causa = customtkinter.CTkTextbox(bloco_causa, width=300, font=("Helvetica", 20))
            self.digt_causa.pack()

            bloco_solucao = customtkinter.CTkFrame(digitComment_frame, fg_color='transparent')
            bloco_solucao.pack(side="left")
            solucaotitle_label = customtkinter.CTkLabel(bloco_solucao, justify="left", text="Solução", font=("Helvetica", 20, "bold"), width=315, anchor="w", text_color='black')
            solucaotitle_label.pack(pady=10, padx=2)
            self.digt_solucao = customtkinter.CTkTextbox(bloco_solucao, width=300, font=("Helvetica", 20))
            self.digt_solucao.pack()       
        else:    
            comentariotitle_label = customtkinter.CTkLabel(digitComment_frame, justify="left", text="Comentario", font=("Helvetica", 20, "bold"), width=950, anchor="w", text_color='black')
            comentariotitle_label.pack(pady=10)
            self.digt_comentario = customtkinter.CTkTextbox(digitComment_frame, width=950, font=("Helvetica", 20))
            self.digt_comentario.insert("0.0", "Verificando") 
            self.digt_comentario.focus_set()
            self.digt_comentario.pack()
            
        buttonSave_frame = customtkinter.CTkFrame(frame_total, fg_color='transparent')
        buttonSave_frame.pack(pady=20)
        button = customtkinter.CTkButton(buttonSave_frame, text="SALVAR",font=("Helvetica", 18, "bold"), fg_color='#6aa84f', text_color='black', width=850,height=40, command=lambda arg=cod, master=master:self.lancar_pcf(arg,master))
        button.pack(side='left', padx=8, pady=8)
        button = customtkinter.CTkButton(buttonSave_frame, text="LOTTO",font=("Helvetica", 18, "bold"), command=lambda arg="Modal": self.ir_para_lotto(arg), fg_color='#1155cc', text_color='black', width=80,height=40)
        button.pack(side='left', padx=8, pady=8)
        self.erros_label = customtkinter.CTkLabel(frame_total, text="", font=("Helvetica", 20), fg_color='transparent', text_color='black')
        self.erros_label.pack(pady=5)
        self.carregando_label = customtkinter.CTkFrame(frame_total, fg_color='transparent')

    def inserir_maquina(self, maquina):
        self.digt_maquina.delete(0, 'end')
        self.digt_maquina.insert(0, maquina)
        for widget in self.maquinasugestao_label.winfo_children():
                widget.destroy()

    def buscar_solicitacao(self, event):
        caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Sistema', 'Bd', 'ordens', 'historico.json')
        numero_digitado = self.digt_maquina.get().lower()
        for widget in self.maquinasugestao_label.winfo_children():
            widget.destroy()
        if len(numero_digitado) > 3 :
            with open(caminho_arquivo, 'r') as f:
                dados = json.load(f)
            resultados = []
            for item in dados:
                if item["Solicitacao"].startswith(numero_digitado):
                    resultados.append(item)

            for i in resultados:
                button = customtkinter.CTkButton(self.maquinasugestao_label, text=i["Solicitacao"],font=("Helvetica", 18), command=lambda arg=i["Solicitacao"]: self.inserir_maquina(arg), fg_color='#1155cc', text_color='white', width=80,height=20)
                button.pack(padx=2, pady=3, side='left')
            if len(resultados) > 0:
                self.digt_sintoma.delete("0.0", "end")
                self.digt_sintoma.insert("0.0", resultados[0]['ProblemaRelatado'])
    
    def sugestao_maquina(self,event):
        entrada = self.digt_maquina.get().lower()
        for widget in self.maquinasugestao_label.winfo_children():
            widget.destroy()
        if len(entrada) > 3 :
            sugestoes = [d["maquina"] for d in self.maquinaLista if entrada in d["maquina"].lower()]
            for i in sugestoes:
                button = customtkinter.CTkButton(self.maquinasugestao_label, text=i,font=("Helvetica", 18), command=lambda arg=i: self.inserir_maquina(arg), fg_color='#1155cc', text_color='white', width=80,height=20)
                button.pack(padx=2, pady=3, side='left')

    def lancar_pcf(self, cod, janela):
        print('kkkkkkkkkkkkkk')
        maquina=self.digt_maquina.get().upper()
        maquinaInfos = buscar_maquina_nome(maquina, self.maquinaLista)

        if maquinaInfos is None:
            self.erros_label.configure(text="Maquina não encontrada", )
            return 0
        if nomeSelecionado == "" or maquina == "" or maquina == "":
            self.erros_label.configure(text="Você deve preencher todos os campos")
            return 0
        usuario = buscar_pessoa_registro(nomeSelecionado)
        if usuario == None:
            self.erros_label.configure(text="registro informado não existe")
            return 0
        if cod == "0706":
            sintoma = self.digt_sintoma.get("0.0", "end")
            causa = self.digt_causa.get("0.0", "end")
            solucao = self.digt_solucao.get("0.0", "end")
            if solucao == "" or causa == "" or  sintoma == "":
                self.erros_label.configure(text="Você deve preencher todos os campos")
                return 0
            caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Sistema', 'Bd', 'ordens', 'historico.json')
            with open(caminho_arquivo, "r") as f:
                ordens = json.load(f)

            for ordem in ordens:
                if ordem["Solicitacao"] == maquina:
                    ordens.remove(ordem)
                    ordem["DataLiberacao"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    ordem["ProblemaEncontrado"] = "teste"
                    ordem["Solucao"]="teste"
                    ordem["CausaRaiz"]="teste"
                    with open(caminho_arquivo, "w") as f:
                        json.dump(ordens, f, indent=2)

                    historico_file_path = f"{ordem['Maquina']}_historico.json"
                    caminho_arquivo_maquina = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Sistema', 'Bd', 'maquina', historico_file_path)
                    try:
                        with open(caminho_arquivo_maquina, "r") as historico_file:
                            historico = json.load(historico_file)
                    except FileNotFoundError:
                        historico = []

                    historico.append(ordem)
                    with open(caminho_arquivo_maquina, "w") as historico_file:
                        json.dump(historico, historico_file, indent=2)

                    print("Ordem Liberada", f"A ordem {maquina} foi liberada com sucesso!")
                    return

            print("Erro", f"A ordem {maquina} não foi encontrada em aberto!")
            comentario = solucao.replace('\n', '')+" | "+causa.replace('\n', '')+" | "+sintoma.replace('\n', '')
        else:
            comentario = self.digt_comentario.get("0.0", "end")
            if comentario =="" :
                self.erros_label.configure(text="Você deve preencher todos os campos")
                return 0  

        loading_window = ToplevelWindow(self)
        thread = Thread(target=self.executar_lancar_pcf, args=(cod, maquinaInfos, comentario,usuario, loading_window))
        thread.start()
        
    def executar_lancar_pcf(self, cod, maquinaInfos, comentario,usuario,loading_window):
        try:
            diretorio_atual = os.path.dirname(os.path.abspath(__file__))
            caminho_do_webdriver = os.path.join(diretorio_atual, 'Sistema', 'Drives', 'chromedriver.exe')
            chrome_options = Options()
            chrome_options.add_argument('--headless') # Executa em segundo plano
            caminho_do_webdriver = os.path.join(diretorio_atual, 'Sistema', 'Drives', 'chromedriver.exe')
            servico = webdriver.chrome.service.Service(caminho_do_webdriver)
            navegador = webdriver.Chrome(service=servico)
            navegador.get("http://10.36.216.25:9097")
            WebDriverWait(navegador, 120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="user"]')) #escrever no login
            ).send_keys('31231')
            WebDriverWait(navegador, 120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')) #escrever no login
            ).send_keys('31231')
            WebDriverWait(navegador, 120).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-authentication/div/div/div/div[2]/form/app-button[1]/button'))
            ).click()
            time.sleep(1)
            navegador.get("http://10.36.216.25:9097/work-station-details/"+maquinaInfos["codigo"])
            WebDriverWait(navegador, 120).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-home/div/main/app-work-station-details/app-grid/app-grid-layout/div/gridster/gridster-item[3]/app-dyn-component/app-list-quick-access-button/gridster/gridster-item[1]/app-quick-access-button/button'))
            ).click()
            if cod[1] == "4":
                WebDriverWait(navegador, 120).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/ngb-modal-window/div/div/app-a0714modal/div[2]/app-a0714-resource-status/app-panel-resource-status/div/ul/li[6]'))
                ).click()
            if cod[1] == "7":
                WebDriverWait(navegador, 120).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/ngb-modal-window/div/div/app-a0714modal/div[2]/app-a0714-resource-status/app-panel-resource-status/div/ul/li[9]'))
                ).click()
            if cod[1] == "5":
                WebDriverWait(navegador, 120).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/ngb-modal-window/div/div/app-a0714modal/div[2]/app-a0714-resource-status/app-panel-resource-status/div/ul/li[7]'))
                ).click()

            caminho_status={
                None: "",
                "0405": '//*[@id="ngb-nav-10-panel"]/app-list-mini-card-comment/div[2]/div[2]/div',
                "0406": '//*[@id="ngb-nav-10-panel"]/app-list-mini-card-comment/div[2]/div[3]/div',
                "0407": '//*[@id="ngb-nav-10-panel"]/app-list-mini-card-comment/div[2]/div[4]/div',
                "0408": '//*[@id="ngb-nav-10-panel"]/app-list-mini-card-comment/div[2]/div[5]/div',
                "0403": '//*[@id="ngb-nav-10-panel"]/app-list-mini-card-comment/div[2]/div[7]/div',
                "0706": '//*[@id="ngb-nav-13-panel"]/app-list-mini-card-comment/div[2]/div[7]/div',
                "0502": '//*[@id="ngb-nav-70-panel"]/app-list-mini-card-comment/div[2]/div[1]/div',
                "0504": '//*[@id="ngb-nav-70-panel"]/app-list-mini-card-comment/div[2]/div[3]/div',
                "0505": '//*[@id="ngb-nav-70-panel"]/app-list-mini-card-comment/div[2]/div[4]/div',
                "0506": '//*[@id="ngb-nav-70-panel"]/app-list-mini-card-comment/div[2]/div[5]/div',
                "0404": '//*[@id="ngb-nav-10-panel"]/app-list-mini-card-comment/div[2]/div[1]/div',
                "0418": '//*[@id="ngb-nav-10-panel"]/app-list-mini-card-comment/div[2]/div[20]/div',
            }
            time.sleep(1)
            WebDriverWait(navegador, 120).until(
                EC.element_to_be_clickable((By.XPATH, caminho_status[cod]))
            ).click()
            WebDriverWait(navegador, 120).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/ngb-modal-window[2]/div/div/app-modal-status-details-comments/div[2]/div/div/textarea')) #escrever no login
            ).send_keys(comentario)
            WebDriverWait(navegador, 120).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/ngb-modal-window[2]/div/div/app-modal-status-details-comments/div[3]/app-button[2]/button'))
            ).click()
        finally:
            self.master.after(0, lambda: self.fechar_janela(loading_window))

    def fechar_janela(self, window):
        window.destroy()

    def verificar_thread(self, thread, loading_window):
        if thread.is_alive():
            self.master.after(100, self.verificar_thread, thread, loading_window)
        else:
            self.fechar_janela(loading_window)
