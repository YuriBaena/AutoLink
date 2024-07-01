from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def linkedin(email, senha, chave):
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

    pesquisa = aba1.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
    pesquisa.send_keys(chave)
    pesquisa.send_keys(Keys.ENTER)

    time.sleep(5)

    pessoas = aba1.find_element(By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[4]/button')
    pessoas.click()

    time.sleep(3)


email_linkedin = input("Diga o email do seu LinkedIn: ")
senha_linkedin = input("Diga a senha do LinkeIn: ")

conectar = input("Diga algo que remeta a pessoas que deseja se conectar: ")

linkedin(email_linkedin, senha_linkedin, conectar)
