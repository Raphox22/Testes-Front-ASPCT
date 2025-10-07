from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Configurações para navegador OperaGX
opera_path = r"C:\Users\User\AppData\Local\Programs\Opera GX"

options = Options()
options.binary_location = opera_path

driver = webdriver.Chrome(options=options)
driver.get("https://v0-aspct-software-frontend.vercel.app/login")
driver.implicitly_wait(10)

# Login
campo_email = driver.find_element(By.ID, "email")
campo_email.send_keys("carlos@exemplo.com")

campo_senha = driver.find_element(By.ID, "password")
campo_senha.send_keys("123456")

# Botao de login
botao_login = driver.find_element(By.XPATH, "//button[contains(text(), 'Entrar')]")
botao_login.click()

# Aguardar tempo de login
time.sleep(5)

# Botões principais
botoes = ["Progresso", "Meus Filhos"]

for texto in botoes:
    botao = driver.find_element(By.XPATH, f"//*[contains(text(), '{texto}')]")
    botao.click()
    time.sleep(5)

# Encerra
driver.quit()
