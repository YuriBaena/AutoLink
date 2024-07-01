from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def linkedin(email, senha, x):
    global aba1
    try:
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

        post = aba1.find_element(By.XPATH, '//*[@id="ember48"]')
        post.click()

        time.sleep(5)

        campo_texto = aba1.switch_to.active_element
        campo_texto.send_keys(x)

        time.sleep(3)

        enviar = aba1.find_element(By.XPATH, '//*[@id="ember284"]')
        enviar.click()

        time.sleep(5)

        # Se postou sem erros, remover o post do arquivo
        with open('textos.txt', 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

        with open('textos.txt', 'w', encoding='utf-8') as arquivo:
            for linha in linhas:
                if linha.strip() != x:
                    arquivo.write(linha)

    except Exception as e:
        print(f"Erro ao processar o post: {x}")
        print(e)

    finally:
        if 'aba1' in locals():
            aba1.quit()


# Abra o arquivo 'textos.txt' em modo de leitura
with open('textos.txt', 'r', encoding='utf-8') as arquivo:
    # Leia todas as linhas do arquivo
    linhas = arquivo.readlines()

    email_linkedin = input("Diga o email do seu LinkedIn: ")
    senha_linkedin = input("Diga a senha do LinkeIn: ")

    # Para cada linha lida, faça:
    for linha in linhas:
        # Remova os espaços em branco no início e no final da linha
        post = linha.strip()

        linkedin(email_linkedin, senha_linkedin, post)
