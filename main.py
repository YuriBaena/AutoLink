from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import pyperclip
import re

import time


def linkedin(email, senha, conectar):

    aba1 = webdriver.Chrome()

    aba1.get("https://br.linkedin.com/?original_referer=https%3A%2F%2Fwww.google.com%2F")

    time.sleep(5)

    # Encontrar o campo de e-mail e preenchê-lo
    email_input = aba1.find_element(By.XPATH, '//*[@id="session_key"]')
    email_input.send_keys(email)

    # Encontrar o campo de senha e preenchê-lo
    password_input = aba1.find_element(By.XPATH, '//*[@id="session_password"]')
    password_input.send_keys(senha)

    # Enviar o formulário (pressionar Enter)
    password_input.send_keys(Keys.ENTER)

    time.sleep(5)

    '''Se precisar'''
    #codigo = pega_codigo_do_email()
    #print(codigo)

    pesquisa = aba1.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
    pesquisa.send_keys(conectar)
    pesquisa.send_keys(Keys.ENTER)

    time.sleep(5)

    pessoas = aba1.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[2]/div/div[1]/div/div/div/section/ul/li[4]/button')
    pessoas.click()

    time.sleep(5)

def pega_codigo_do_email():
    global codigo
    aba2 = webdriver.Chrome()

    #Abre outra aba para email
    aba2.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=154&ct=1719844956&rver=7.0.6738.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26RpsCsrfState%3d70262033-e4ce-d0f1-ba33-4b9af451ca2f&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c")

    time.sleep(2)

    #Encontra campo de email e preenche
    email_input = aba2.find_element(By.XPATH, '//*[@id="i0116"]')
    email_input.send_keys("yuribaena@hotmail.com")

    # Enviar o formulário (pressionar Enter)
    email_input.send_keys(Keys.ENTER)

    time.sleep(2)

    # Encontrar o campo de senha e preenchê-lo
    password_input = aba2.find_element(By.XPATH, '//*[@id="i0118"]')
    password_input.send_keys("ybdn1407")

    # Enviar o formulário (pressionar Enter)
    password_input.send_keys(Keys.ENTER)

    time.sleep(2)

    #Nao continuar conectado
    botao = aba2.find_element(By.XPATH, '//*[@id="declineButton"]')
    botao.click()

    time.sleep(6)

    # Maximizar a janela do navegador
    aba2.maximize_window()

    pesquisa = aba2.find_element(By.XPATH, '//*[@id="topSearchInput"]')
    pesquisa.send_keys("LinkedIn")
    pesquisa.send_keys(Keys.ENTER)

    time.sleep(3)

    ajeita = aba2.find_element(By.XPATH, '//*[@id="groupHeaderPrincipais resultados"]/div')
    ajeita.click()

    time.sleep(3)

    # Instanciar ActionChains
    actions = ActionChains(aba2)

    # Mover o mouse para uma posição específica na tela (exemplo: coordenadas x=100, y=200)
    actions.move_by_offset(500, 300)

    # Realizar um clique
    actions.click()

    # Executar as ações
    actions.perform()

    time.sleep(5)

    # Mover o mouse para as coordenadas iniciais do texto a ser selecionado
    pyautogui.moveTo(600, 300)

    # Simular o clique do mouse (botão esquerdo pressionado)
    pyautogui.mouseDown()

    # Mover o mouse para as coordenadas finais do texto a ser selecionado
    pyautogui.moveTo(800, 800)

    # Simular a liberação do botão esquerdo do mouse (texto está selecionado)
    pyautogui.mouseUp()

    # Aguardar um momento para garantir que o texto seja selecionado
    time.sleep(3)

    # Simular o pressionamento de Cmd + C para copiar o texto selecionado
    pyautogui.keyDown("command")
    pyautogui.keyDown("a")

    pyautogui.keyUp("command")
    pyautogui.keyUp("a")

    pyautogui.keyDown("command")
    pyautogui.keyDown("c")

    pyautogui.keyUp("command")
    pyautogui.keyUp("c")

    texto = pyperclip.paste()

    # Usando regex para encontrar sequências de 6 dígitos
    padrao = r'\b\d{6}\b'  # \b é uma âncora de limite de palavra

    # Encontrar todos os padrões na variável texto
    matches = re.findall(padrao, texto)

    # Acha codigo
    for match in matches:
        codigo = match

    return codigo


email_linkedin = input("Diga o email do seu LinkedIn: ")
senha_linkedin = input("Diga a senha do LinkeIn: ")

conectar = input("Diga algo que remeta a pessoas que deseja se conectar: ")

linkedin(email_linkedin, senha_linkedin, conectar)
