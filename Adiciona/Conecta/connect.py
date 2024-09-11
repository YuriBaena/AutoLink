from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def main(mail, psw, topico):
    def entrar(aba1, email, senha):
        aba1.get("https://br.linkedin.com/?original_referer=https%3A%2F%2Fwww.google.com%2F")

        time.sleep(5)

        try:
            logar(aba1, email, senha)
        except Exception as e:
            log_email = aba1.find_element(By.XPATH, '/html/body/main/section[1]/div/div/a')
            log_email.click()

            time.sleep(5)

            logar(aba1, email, senha)

    def logar(aba1, email, senha):
        try:
            # Encontrar o campo de e-mail e preenchê-lo
            email_input = aba1.find_element(By.XPATH, '//*[@id="session_key"]')
            email_input.send_keys(email)

            # Encontrar o campo de senha e preenchê-lo
            password_input = aba1.find_element(By.XPATH, '//*[@id="session_password"]')
            password_input.send_keys(senha)

            # Enviar o formulário (pressionar Enter)
            password_input.send_keys(Keys.ENTER)

            time.sleep(5)
        except Exception:
            # Encontrar o campo de e-mail e preenchê-lo
            email_input = aba1.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[1]/input')
            email_input.send_keys(email)

            # Encontrar o campo de senha e preenchê-lo
            password_input = aba1.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[2]/input')
            password_input.send_keys(senha)

            # Enviar o formulário (pressionar Enter)
            password_input.send_keys(Keys.ENTER)

            time.sleep(5)

    def encontrar_pessoas(aba1, chave):
        pesquisa = aba1.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
        pesquisa.send_keys(chave)
        pesquisa.send_keys(Keys.ENTER)

        time.sleep(5)

        for i in range(1, 7):
            pessoas = aba1.find_element(By.XPATH,
                                        f'/html/body/div[5]/div[3]/div[2]/section/div/nav/div/ul/li[{i}]/button')
            nome = pessoas.text.strip()
            if nome == "People":
                break

        if nome == "People":
            pessoas.click()
            return 0
        else:
            return 1

        time.sleep(3)

    def conectar_com_msg(aba1):
        for i in range(1, 6):
            try:
                conectar = aba1.find_element(By.XPATH,
                                             f'/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li[{i}]/div/div/div/div[3]/div/button')
                conectar.click()
                time.sleep(3)

                texto = "I'm a Computer Science student at UERJ and I'm looking to connect with people in the TECH field. If you also work or are interested in technology, let's connect!"

                add_texto = aba1.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[1]')
                add_texto.click()

                time.sleep(2)

                area_de_texto = aba1.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/div[1]/textarea')
                area_de_texto.send_keys(texto)

                time.sleep(3)

                send = aba1.find_element(By.XPATH, '/html/body/div[3]/div/div/div[4]/button[2]')
                send.click()

                time.sleep(3)

            except Exception:
                pass

    def conectar_sem_msg(aba1):
        for i in range(5):
            try:
                conectar = aba1.find_element(By.XPATH,
                                             f'/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li[{i}]/div/div/div/div[3]/div/button')
                conectar.click()
                time.sleep(3)

                send = aba1.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]')
                send.click()

                time.sleep(3)

            except Exception:
                pass

    def linkedin(email, senha, chave):
        aba1 = webdriver.Chrome()

        entrar(aba1, email, senha)

        certo = encontrar_pessoas(aba1, chave)

        if certo == 0:
            # conectar_com_msg(aba1)

            for pag in range(2, 10):

                #conectar_sem_msg(aba1)

                time.sleep(5)

        else:
            print("Pessoas nao encontradas")

    chave = topico

    linkedin(mail, psw, chave)


email = "yuribaena@hotmail.com"  # input("Diga o email do seu LinkedIn: ")
senha = "Mayy2016!"  # input("Diga a senha do LinkeIn: ")


with open("topicos.txt", "r") as arq:
    topicos = arq.readlines()
    for topico in topicos:
        time.sleep(2)
        main(email, senha, topico[:-2])
