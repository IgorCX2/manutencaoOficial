import time
import requests
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from functions_share import carregar_maquina, buscar_maquina_nome
import webbrowser
import tempfile
import os
from threading import Thread
from datetime import datetime
import pyautogui
import tempfile
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def reiniciar_temporizador(app, event):
    app.tempo_inativo = time.time()

def criar_html(maquina, descricao, solicitacao, ordem,dataAtual, CC,dataOrdem, descricaoMaquina,local,equipe):
    html_content = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: 'Helvetica', sans-serif;
                font-size: 14px;
            }}
            h1, h2 {{
                font-weight: bold;
            }}
        </style>
    </head>
    <body style="overflow-y: hidden;width: 100vw">
        <div>
            <p;">------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------</p>
            <div style="display: flex; justify-content: space-between;padding: 0px 15px 0px 0px; font-size: 18px; margin-top: -29px;">
                <p>( SISTEMANUTENCAO )</p>
                <p>Solicitacao de Servico - Manutencao Corretiva e Permissao de Trabalho</p>
                <p>Pagina.:      01</p>
            </div>  
            <div style="display: flex; justify-content: space-between;padding: 0px 15px 0px 0px; font-size: 18px; margin-top: -29px;">
                <p> Manut. tipo: ( )Corr. ( )Prev. ( )Outra: _____________   Pessoal :( )Inter ( )Exter Fixo</p>
                <p>Data.:  {dataAtual}</p>
            </div>
            <p style="margin-top: -15px;">------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------</p>                           
        </div>
        <div style="margin-top: -18px;">
            <div style="display: flex; justify-content: space-between;padding: 0px 15px 0px 0px; font-size: 18px">
                <p>NR.Solicit.: {solicitacao}  {descricao}</p>
                <p>Prioridade: 000</p>
            </div> 
            <div style="display: flex; justify-content: space-between;padding: 0px 15px 0px 0px; font-size: 18px; margin-top: -8px;">
                <div>
                    <p> TAG: {maquina}</p>
                    <p style="margin-top: -10px;">Ord.Manuten:  {ordem} </p>
                </div>
                <div>
                    <p>C.C.: {CC}</p>
                    <p style="margin-top: -10px;">Data Início: {dataOrdem}</p>
                </div>
                <div>
                    <p>{descricaoMaquina}</p>
                    <p style="margin-top: -10px;">Local: {local}</p>
                </div>
            </div> 
            <div style="display: flex; justify-content: space-between;padding: 0px 30px 0px 15px; font-size: 18px; margin-top: -3px;">
                <div>
                    <p>Manutenção:</p>
                    <p style="margin-top: -15px;">Causa:</p>
                </div>
                <div>
                    <p>## manutencao desconhecida</p>
                    <p style="margin-top: -15px;">*nao encontrado*</p>
                </div>
                <div>
                    <p>Equipe:</p>
                    <p style="margin-top: -15px;">Interv:</p>
                    <p style="margin-top: -15px;">APU(Solic:)</p>
                </div>
                <div>
                    <p>{equipe}</p>
                    <p style="margin-top: -15px;">          -</p>
                    <p style="margin-top: -15px;">mi-cortez     -  Igor Cortez - F1</p>
                </div>
            </div>
            <div style="margin-top: 15px; display: flex;flex-direction: column;font-size: 18px; width: 100%; ">
                <p >Ativ. de Risco: ( ) Não - Ok - Atividade.Liberada: ______________ Obs: usar EPI's determinados para a realizaacao da atividade</p>
                <p style="margin-top: -12px; text-align: right">( ) Sim - Qual?: ( )Altura ( )Solda ( )Loto AT ( )Mov.Carga ( )Esp.Confinado ( )Escavação PTE Nr:_______________</p>
                <p style="margin-top: -2px;">Supervisor: __________________ Equipe Trabalho: ____________________ Liberação HSE: ________________</p>
            </div>
            <div style="display: flex; width:100%; gap: 9px; margin-top: 10px;">
                <div>
                    <p style="font-size: 15px;">Tarefas</p>
                    <p style="margin-top: -20px">__________________________________________________</p>
                    <p>__________________________________________________</p>
                    <p>__________________________________________________</p>
                    <p>__________________________________________________</p>
                    <p>__________________________________________________</p>
                    <p>__________________________________________________</p>
                    <p>__________________________________________________</p>
                    <p>__________________________________________________</p>
                    <p>__________________________________________________</p>
                    <p>__________________________________________________</p>
                    <p>__________________________________________________</p>
                    <p>__________________________________________________</p>
                    <p>__________________________________________________</p>
                </div>
                <div>
                    <p style="font-size: 15px;">Data</p>
                    <p style="margin-top: -20px">_____________</p>
                    <p>_____________</p>
                    <p>_____________</p>
                    <p>_____________</p>
                    <p>_____________</p>
                    <p>_____________</p>
                    <p>_____________</p>
                    <p>_____________</p>
                    <p>_____________</p>
                    <p>_____________</p>
                    <p>_____________</p>
                    <p>_____________</p>
                    <p>_____________</p>
                </div>
                <div>
                    <p style="font-size: 15px;">Funcio</p>
                    <p style="margin-top: -20px">___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                </div>
                <div>
                    <p style="font-size: 15px;">Inicio</p>
                    <p style="margin-top: -20px">___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                </div>
                <div>
                    <p style="font-size: 15px;">Termino</p>
                    <p style="margin-top: -20px">___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                    <p>___________</p>
                </div>
                <div>
                    <p style="font-size: 15px;">Obs/Visto</p>
                    <p style="margin-top: -20px">_________________</p>
                    <p>_________________</p>
                    <p>_________________</p>
                    <p>_________________</p>
                    <p>_________________</p>
                    <p>_________________</p>
                    <p>_________________</p>
                    <p>_________________</p>
                    <p>_________________</p>
                    <p>_________________</p>
                    <p>_________________</p>
                    <p>_________________</p>
                    <p>_________________</p>
                </div>   
            </div>
            <div style="display: flex; width:100%; gap: 9px; margin-top: 10px;">
                <div>
                    <p style="font-size: 15px;">Componentes</p> 
                    <p style="margin-top: -20px">__________________________________________________</p>
                    <p>__________________________________________________</p>
                    <p>__________________________________________________</p>
                    <p>__________________________________________________</p>
                    <p>__________________________________________________</p>
                    <p>__________________________________________________</p>
                    <p>__________________________________________________</p>
                </div>
                <div>
                    <p style="font-size: 15px;">Quantidade</p> 
                    <p style="margin-top: -20px">_____________</p>
                    <p>_____________</p>
                    <p>_____________</p>
                    <p>_____________</p>
                    <p>_____________</p>
                    <p>_____________</p>
                    <p>_____________</p>
                </div>
                <div>
                    <p style="font-size: 15px;">Marca</p> 
                    <p style="margin-top: -20px">________________________</p>
                    <p>________________________</p>
                    <p>________________________</p>
                    <p>________________________</p>
                    <p>________________________</p>
                    <p>________________________</p>
                    <p>________________________</p>
                </div>
                <div>
                    <p style="font-size: 15px;">Modelo</p> 
                    <p style="margin-top: -20px">_____________________________</p>
                    <p>_____________________________</p>
                    <p>_____________________________</p>
                    <p>_____________________________</p>
                    <p>_____________________________</p>
                    <p>_____________________________</p>
                    <p>_____________________________</p>
                </div>
            </div>
        </div>
        <p style="font-size: 14px; text-align: center;">* SE DETECTADO SITUACAO DE RISCO GRAVE E EMINENTE NESTA SOLICITACAO DE TRABALHO,NAO EXECUTAR A TAREFA ATE REGULARIZACAO.</p>
        <p style="position: absolute; bottom: 0;">-------------------------------------------------------------------------------------------------- HBA - Hutchinson Brasil Automotive     - SISTEMANUTENCAO</p>
    </body>
    </html>
    """
    return html_content

def salvar_html_temporario(html_content):
    temp_html_path = tempfile.mktemp(suffix=".html", prefix="solicitacao_", dir=tempfile.gettempdir())
    with open(temp_html_path, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

    return temp_html_path


def acessar_pcFactory():
    print("ACESSAR API")
    maquinaLista = carregar_maquina()
    url = "http://10.36.216.25:9095/maps/v1"
    response = requests.get(url)

    if response.status_code == 200:
        dados_api = response.json()
        resultados = []

        for item in dados_api:
            local = item.get("name")
            for maquinas in item["resources"]:
                maquina = maquinas.get("code")
                cod = maquinas.get("statusCode")
                if cod == "0409":
                    resultados.append(buscar_maquina_nome(maquina, maquinaLista)) 
        
        return resultados
    else:
        print(f"Falha na requisição. Código de status: {response.status_code}")

def abrirChamado(app, resultados):
    try:
        comentarios = []
        statusSalvar = []
        abrirOrdem = []
        abrirSolicitacao= []
        if len(resultados) != 0:
            servico = webdriver.ChromeService()
            navegador = webdriver.Chrome(service=servico)
            navegador.get("http://10.36.216.25:9097") #entrar no site
            WebDriverWait(navegador, 120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="user"]')) #escrever no login
            ).send_keys('31231')
            WebDriverWait(navegador, 120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')) #escrever no login
            ).send_keys('31231')
            WebDriverWait(navegador, 120).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-authentication/div/div/div/div[2]/form/app-button[1]/button'))
            ).click()
            time.sleep(10)
            for abrirOrdens in resultados:
                navegador.get("http://10.36.216.25:9097/screens/A0028")
                WebDriverWait(navegador, 120).until(
                    EC.visibility_of_element_located((By.XPATH, '//*[@id="resource-status"]')) #escrever no login
                ).send_keys(abrirOrdens['maquina'])
                WebDriverWait(navegador, 120).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="desktop"]/div/div[1]/div/span'))
                ).click()
                WebDriverWait(navegador, 120).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="desktop"]/div/div[2]/app-input-date-picker/div/form/div/app-button/button'))
                ).click()
                WebDriverWait(navegador, 120).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="desktop"]/div/div[2]/app-input-date-picker/div/form/lib-angular-mydatepicker-calendar/div/div/lib-footer-bar/div/button'))
                ).click()
                WebDriverWait(navegador, 120).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="btn-filter"]/button'))
                ).click()
                element = WebDriverWait(navegador, 120).until(
                    EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/app-home/div/main/app-screens-page/app-dyn-page/app-a0028/div/app-a0028-edit-status-resource/div[3]'))
                )
                entries = element.find_elements(By.XPATH, './div')
                if entries:
                    last_entry = entries[-1]
                    last_entry_text = last_entry.find_element(By.XPATH, './div/div[2]/div[3]/ppi-field/div/div').text
                    comentarios.append(last_entry_text)
                else:
                    print("Nenhuma entrada encontrada")
            if len(comentarios) != len(resultados):
                print("Orden nao estao batendo com a quantidade de comentarios")
                return 0
            navegador.get("http://10.36.216.203:8080/totvs-login/loginForm") #entrar no site
            WebDriverWait(navegador, 120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="txtUsername"]')) #escrever no login
            ).send_keys('mi-cortez')
            WebDriverWait(navegador, 120).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="txtPassword"]')) #escrever no login
            ).send_keys('09012024')
            WebDriverWait(navegador, 120).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div[2]/div/div[3]/button'))
            ).click()
            time.sleep(6)
            #fazer a verificação de ordens
            navegador.get("http://10.36.216.203:8080/totvs-menu/#/dts/mmi/servicerequest/")
            time.sleep(2)
            WebDriverWait(navegador, 120).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-view"]/ui-view/totvs-page/div/div[1]/div/div[2]/totvs-page-header-operation-filter/div/div/div[1]/form/div/span/button[2]'))
            ).click()
            WebDriverWait(navegador, 120).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-view"]/ui-view/totvs-page/div/div[1]/div/div[2]/totvs-page-header-operation-filter/div/div/div[2]/a'))
            ).click()
            WebDriverWait(navegador, 120).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[2]/div/form/accordion/div/div[1]/div[2]/div/div/totvs-field/div/div/div[1]/span[1]/span/input'))
            ).click()
            WebDriverWait(navegador, 120).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div[2]/div/form/accordion/div/div[1]/div[2]/div/div/totvs-field/div/div/div[1]/span[1]/span/input')) #escrever no login
            ).send_keys('12/01/2024')
            WebDriverWait(navegador, 120).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[2]/div/form/accordion/div/div[3]/div[1]/h4/a'))
            ).click()
            for i in range(len(comentarios)):
                time.sleep(1)
                if i != 0:
                    xpath = f'/html/body/div[{7 + 2 * (i-1)}]/div/div/div[2]/div/form/accordion/div/div[3]/div[2]/div/div[1]/field[2]/div/div/div/span/button'
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-view"]/ui-view/totvs-page/div/div[1]/div/div[2]/totvs-page-header-operation-filter/div/div/div[2]/a'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, xpath))
                    ).click()
                else:
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[2]/div/form/accordion/div/div[1]/div[2]/div/div/totvs-field/div/div/div[1]/span[3]/span/input'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div[2]/div/form/accordion/div/div[1]/div[2]/div/div/totvs-field/div/div/div[1]/span[3]/span/input')) #escrever no login
                    ).send_keys('17/01/2024')
                print(resultados[i]['maquina'])
                xpathMaquina = f'/html/body/div[{5 + 2 * i}]/div/div/div[2]/div/form/accordion/div/div[3]/div[2]/div/div[1]/field[2]/div/div/div/input'
                xpathButton = f'/html/body/div[{5 + 2 * i}]/div/div/div[3]/button[2]'
                xpathUser = f'/html/body/div[{5 + 2 * i}]/div/div/div[2]/div/form/accordion/div/div[3]/div[2]/div/div[4]/field/div/div/div/span/button'
                WebDriverWait(navegador, 120).until(
                    EC.visibility_of_element_located((By.XPATH, xpathMaquina))
                ).send_keys(resultados[i]['maquina'])
                WebDriverWait(navegador, 120).until(
                    EC.element_to_be_clickable((By.XPATH, xpathUser))
                ).click()
                WebDriverWait(navegador, 120).until(
                    EC.element_to_be_clickable((By.XPATH, xpathButton))
                ).click()
                time.sleep(1)
                quantidadeOrdens = WebDriverWait(navegador, 120).until(
                    EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/ui-view/totvs-page/div/div[1]/div/div[1]/div/h2'))
                ).text
                print(quantidadeOrdens)
                if quantidadeOrdens[24] == "0":
                    abrirOrdem.append({"maquina":resultados[i]['maquina'], "codigo": resultados[i]['codigo'], "comentario": comentarios[i]})
                else:
                    abrirSolicitacao.append({"maquina":resultados[i]['maquina'], "codigo": resultados[i]['codigo'], "comentario": comentarios[i]})

            print("ordem Abrir")
            print(abrirOrdem)
            print("Solicitacao")
            print(abrirSolicitacao)
            if len(abrirOrdem) > 0:
                print("AbrirOrdem")
                navegador.get("http://10.36.216.203:8080/totvs-menu/#/dts/mmi/order/")
                time.sleep(5)
                WebDriverWait(navegador, 120).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/ui-view/totvs-page/div/div[1]/div/div/totvs-page-header-operation-action/div/div/a[1]'))
                ).click()
                for i in range(len(abrirOrdem)):
                    
                    print(abrirOrdem[i])
                    time.sleep(10)
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div/div[2]/div/form/fieldset/div/div[1]/totvs-field[1]/div/div/div[1]/span[2]/button[2]'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[16]/div/div/div[2]/div/div[1]/div/div[1]/field/div/div/div/div'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[16]/div/div/div[2]/div/div[1]/div/div[1]/field/div/div/div/div/ul/li/div[6]'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.visibility_of_element_located((By.XPATH, '/html/body/div[16]/div/div/div[2]/div/div[1]/div/div[2]/field/div/div/div/input')) #maquina
                    ).send_keys(abrirOrdem[i]['maquina'])

                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[16]/div/div/div[2]/div/div[1]/div/div[3]/button'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[16]/div/div/div[2]/div/div[3]/totvs-table/div/div/table/tbody/tr[1]'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[16]/div/div/div[3]/div/button[2]'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div/div[2]/div/form/fieldset/div/div[3]/totvs-field[1]/div/div/div[1]/span[2]/button[2]'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.visibility_of_element_located((By.XPATH, '/html/body/div[16]/div/div/div[2]/div/div[1]/div/div[2]/field/div/div/div/input'))
                    ).send_keys('7')
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[16]/div/div/div[2]/div/div[1]/div/div[3]/button'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[16]/div/div/div[2]/div/div[2]/totvs-table/div/div/table/tbody/tr'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[16]/div/div/div[3]/div/button[2]'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div/div[2]/div/form/fieldset/div/div[3]/totvs-field[2]/div/div/div[1]/span[2]/button[2]'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[16]/div/div/div[2]/div/div[1]/div/div[3]/button'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[16]/div/div/div[2]/div/div[2]/totvs-table/div/div/table/tbody/tr[1]'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[16]/div/div/div[3]/div/button[2]'))
                    ).click()
                    
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div/div[2]/div/form/fieldset/div/div[4]/totvs-field[2]/div/div/div[1]/span[2]/button[2]'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.visibility_of_element_located((By.XPATH, '/html/body/div[16]/div/div/div[2]/div/div[1]/div/div[2]/field/div/div/div/input'))
                    ).send_keys(str(comentarios[i])[len(comentarios[i])-1])#Mudar eletrico
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[16]/div/div/div[2]/div/div[1]/div/div[3]/button'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[16]/div/div/div[2]/div/div[2]/totvs-table/div/div/table/tbody/tr[1]'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[16]/div/div/div[3]/div/button[2]'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.visibility_of_element_located((By.XPATH, '/html/body/div[7]/div/div/div[2]/div/form/fieldset/div/div[6]/field/div/div/div/input')) #comentario
                    ).send_keys(abrirOrdem[i]['comentario'])
                    print(i)
                    print(len(abrirOrdem))
                    if i+1 == len(abrirOrdem):
                        WebDriverWait(navegador, 120).until(
                            EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div/div[3]/button[3]'))
                        ).click()
                    else:
                        WebDriverWait(navegador, 120).until(
                            EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div/div[3]/button[2]'))
                        ).click()
                    abrirSolicitacao.append(abrirOrdem[i])

            print(abrirSolicitacao)
            time.sleep(10)
            print("ver abrindo um por uma")
            for i in range(len(abrirSolicitacao)):
                time.sleep(2)
                navegador.get("http://10.36.216.203:8080/totvs-menu/#/dts/mmi/servicerequest/")
                time.sleep(5)
                WebDriverWait(navegador, 120).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/ui-view/totvs-page/div/div[1]/div/div[2]/totvs-page-header-operation-action/div/div/a'))
                ).click()
                if len(abrirOrdem) > 0:
                    print(abrirSolicitacao[i]['maquina'])
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[15]/div/div/div[2]/div/form/fieldset/div/div[1]/totvs-field[2]/div/div/div[1]/span[2]/button[2]'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.visibility_of_element_located((By.XPATH, '/html/body/div[21]/div/div/div[2]/div/div[1]/div/div[2]/field/div/div/div/input')) #escrever no login
                    ).send_keys(abrirSolicitacao[i]['maquina'])
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[21]/div/div/div[2]/div/div[1]/div/div[3]/button'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[21]/div/div/div[2]/div/div[2]/totvs-table/div/div/table/tbody/tr[1]'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[21]/div/div/div[3]/div/button[2]'))
                    ).click()
                    time.sleep(1)
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[15]/div/div/div[2]/div/form/fieldset/div/div[2]/totvs-field[2]/div/div/div[1]/span[2]/button[2]'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[21]/div/div/div[2]/div/div[2]/totvs-table/div/div/table/tbody/tr[1]'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[21]/div/div/div[3]/div/button[2]'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[15]/div/div/div[2]/div/form/fieldset/div/div[2]/totvs-field[3]/div/div/div[1]/span[2]/button[2]'))
                    ).click()
                    time.sleep(1)
                    WebDriverWait(navegador, 120).until(
                        EC.visibility_of_element_located((By.XPATH, '/html/body/div[21]/div/div/div[2]/div/div[1]/div/div[2]/field/div/div/div/input')) #escrever equipe
                    ).send_keys(str(comentarios[i])[len(comentarios[i])-1])
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[21]/div/div/div[2]/div/div[1]/div/div[3]/button'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[21]/div/div/div[2]/div/div[2]/totvs-table/div/div/table/tbody/tr[1]'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[21]/div/div/div[3]/div/button[2]'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.visibility_of_element_located((By.XPATH, '/html/body/div[15]/div/div/div[2]/div/form/fieldset/div/div[3]/field/div/div/div/input')) #escrever equipe
                    ).send_keys(abrirSolicitacao[i]['comentario']) #comentario
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[15]/div/div/div[3]/button[3]'))
                    ).click()
                else:
                    print(abrirSolicitacao[i]['maquina'])
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div/div[2]/div/form/fieldset/div/div[1]/totvs-field[2]/div/div/div[1]/span[2]/button[2]'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.visibility_of_element_located((By.XPATH, '/html/body/div[13]/div/div/div[2]/div/div[1]/div/div[2]/field/div/div/div/input')) #escrever no login
                    ).send_keys(abrirSolicitacao[i]['maquina'])
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[13]/div/div/div[2]/div/div[1]/div/div[3]/button'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[13]/div/div/div[2]/div/div[2]/totvs-table/div/div/table/tbody/tr[1]'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[13]/div/div/div[3]/div/button[2]'))
                    ).click()
                    time.sleep(1)
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div/div[2]/div/form/fieldset/div/div[2]/totvs-field[2]/div/div/div[1]/span[2]/button[2]'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[13]/div/div/div[2]/div/div[2]/totvs-table/div/div/table/tbody/tr[1]'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[13]/div/div/div[3]/div/button[2]'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div/div[2]/div/form/fieldset/div/div[2]/totvs-field[3]/div/div/div[1]/span[2]/button[2]'))
                    ).click()
                    time.sleep(1)
                    WebDriverWait(navegador, 120).until(
                        EC.visibility_of_element_located((By.XPATH, '/html/body/div[13]/div/div/div[2]/div/div[1]/div/div[2]/field/div/div/div/input')) #escrever equipe
                    ).send_keys(str(comentarios[i])[len(comentarios[i])-1])
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[13]/div/div/div[2]/div/div[1]/div/div[3]/button'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[13]/div/div/div[2]/div/div[2]/totvs-table/div/div/table/tbody/tr[1]'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[13]/div/div/div[3]/div/button[2]'))
                    ).click()
                    WebDriverWait(navegador, 120).until(
                        EC.visibility_of_element_located((By.XPATH, '/html/body/div[7]/div/div/div[2]/div/form/fieldset/div/div[3]/field/div/div/div/input')) #escrever equipe
                    ).send_keys(abrirSolicitacao[i]['comentario']) #comentario
                    WebDriverWait(navegador, 120).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div/div[3]/button[3]'))
                    ).click()

                time.sleep(15)
                print("pegaSS")
                pegaSS = WebDriverWait(navegador, 120).until(
                    EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/ui-view/totvs-page/div/div[1]/div/div[1]/div/h2'))
                ).text
                print("pegaOrdem")
                pegaOrdem = WebDriverWait(navegador, 120).until(
                    EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/ui-view/totvs-page/div/div[2]/div/div/div[6]/div[3]'))
                ).text
                CentC = WebDriverWait(navegador, 120).until(
                    EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/ui-view/totvs-page/div/div[2]/div/div/div[4]/div[1]/div[2]/span'))
                ).text
                descMaquina = WebDriverWait(navegador, 120).until(
                    EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/ui-view/totvs-page/div/div[2]/div/div/div[3]/div[1]/div[2]/span'))
                ).text
                equipeOrdem = WebDriverWait(navegador, 120).until(
                    EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/ui-view/totvs-page/div/div[2]/div/div/div[3]/div[3]/div[2]/span'))
                ).text
                numero_ordem_manutencao = pegaOrdem.split("Ordem de Manutenção")[1]
                print(numero_ordem_manutencao)
                print(pegaOrdem)
                print(pegaSS[:9])
                statusSalvar.append({"maquina": abrirSolicitacao[i]['maquina'], "Descricao": abrirSolicitacao[i]['comentario'],"codigo": abrirSolicitacao[i]['codigo'],"Solicitacao": pegaSS[:10], "Ordem":str(numero_ordem_manutencao[:10])})
                print(statusSalvar)
                data_e_hora_atuais = datetime.now().strftime("%Y%m%d%H%M%S")
                ordem = {"Ordem": numero_ordem_manutencao[:10], "Solicitacao": pegaSS[:10], "Maquina": abrirSolicitacao[i]['maquina'],"ProblemaRelatado": abrirSolicitacao[i]['comentario']}
                caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Sistema', 'Bd', 'ordens', 'historico.json')
                with open(caminho_arquivo, "r") as f:
                    ordens = json.load(f)
                ordens.append(ordem)

                with open(caminho_arquivo, "w") as f:
                    json.dump(ordens, f, indent=2)
                html_content = criar_html(abrirSolicitacao[i]['maquina'], abrirSolicitacao[i]['comentario'], pegaSS[:10],numero_ordem_manutencao[:10],data_e_hora_atuais.strftime("%d/%m/%Y %H:%M"),CentC,data_e_hora_atuais.strftime("%d/%m/%Y"),descMaquina,resultados[i]['local'],equipeOrdem)
                temp_file_path = salvar_html_temporario(html_content)
                navegador.get(temp_file_path)
                #file_path = 'teste.pdf'            
                #impressora_padrao = win32print.GetDefaultPrinter()
                #teste = r"C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe"
                #subprocess.run([teste, "/t", file_path, "Lexmark MS415dn"], shell=True)
                time.sleep(1)
                pyautogui.leftClick(x=120,y=120)
                pyautogui.hotkey('ctrl', 'p')
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(2)
                
            for i in range(len(statusSalvar)):
                print("letsGo")
                time.sleep(5)
                navegador.get("http://10.36.216.25:9097/work-station-details/"+statusSalvar[i]["codigo"])
                WebDriverWait(navegador, 120).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-home/div/main/app-work-station-details/app-grid/app-grid-layout/div/gridster/gridster-item[3]/app-dyn-component/app-list-quick-access-button/gridster/gridster-item[1]/app-quick-access-button/button'))
                ).click()
                WebDriverWait(navegador, 120).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/ngb-modal-window/div/div/app-a0714modal/div[2]/app-a0714-resource-status/app-panel-resource-status/div/ul/li[6]'))
                ).click()
                time.sleep(1)
                WebDriverWait(navegador, 120).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/ngb-modal-window/div/div/app-a0714modal/div[2]/app-a0714-resource-status/app-panel-resource-status/div/div[2]/div/app-list-mini-card-comment/div[2]/div[17]/div/app-button/button'))
                ).click()
                comentarioSalvar = "SS:"+statusSalvar[i]["Solicitacao"]+ "->"+statusSalvar[i]["Descricao"]
                WebDriverWait(navegador, 120).until(
                    EC.visibility_of_element_located((By.XPATH, '/html/body/ngb-modal-window[2]/div/div/app-modal-status-details-comments/div[2]/div/div/textarea'))
                ).send_keys(comentarioSalvar)
                WebDriverWait(navegador, 120).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/ngb-modal-window[2]/div/div/app-modal-status-details-comments/div[3]/app-button[2]/button'))
                ).click()

    finally:
        app.statusPFC = "Nada"

def Temporizador(app):
    app.after(1000, lambda: Temporizador(app))
    app.temporizador_contador+=1
    if(app.temporizador_contador == 15):
        #print(app.statusPFC)
        #if app.pagina_ativa == "descanso" and app.statusPFC != "Abrindo":
            #dadosPcF = acessar_pcFactory()
            #print(dadosPcF)
            #if len(dadosPcF) > 0:
                #print("abrir chamdo")
                #app.statusPFC = "Abrindo"
                #thread = Thread(target=abrirChamado, args=(app, dadosPcF))
                #thread.start()
        app.temporizador_contador=0
    if time.time() - app.tempo_inativo > 5:
        if(app.pagina_ativa == "descanso"):
            return 0
        app.navigate_to_page("descanso", None)
        return 0
    elif app.pagina_ativa != "descanso":
        return 0
    else:
        app.navigate_to_page("home", None)
        return 0
