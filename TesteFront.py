from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time
import platform
import os
import subprocess

# Gerar timestamp para nome do arquivo
data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
nome_arquivo_html = f"relatorio_teste_{data_hora}.html"

# Função para abrir arquivo automaticamente
def abrir_arquivo(nome_arquivo):
    sistema = platform.system()
    if sistema == "Windows":
        os.startfile(nome_arquivo)
    elif sistema == "Darwin":  # macOS
        subprocess.call(["open", nome_arquivo])
    elif sistema == "Linux":
        subprocess.call(["xdg-open", nome_arquivo])

# Iniciar relatório HTML
html = open(nome_arquivo_html, "w", encoding="utf-8")
html.write(f"""
<html>
<head><meta charset="utf-8">
<title>Relatório de Testes</title>
<style>
  body {{ font-family: Arial; margin: 20px; }}
  table {{ border-collapse: collapse; width: 100%; }}
  th, td {{ border: 1px solid #999; padding: 8px; text-align: left; }}
  th {{ background-color: #eee; }}
  .OK {{ background-color: #d4edda; }}
  .Erro {{ background-color: #f8d7da; }}
</style>
</head>
<body>
<h2>Relatório de Testes - {data_hora}</h2>
<table>
<tr><th>Etapa</th><th>Status</th><th>Mensagem</th><th>Duração (s)</th></tr>
""")

# Função para registrar etapa no HTML
def registrar(etapa, status, mensagem, duracao=""):
    html.write(f"<tr class='{status}'><td>{etapa}</td><td>{status}</td><td>{mensagem}</td><td>{duracao}</td></tr>\n")

# Testes
try:
    driver = webdriver.Chrome()
    inicio = time.time()
    driver.get("https://aspect-frontend-y7zo.vercel.app/dashboard")
    driver.implicitly_wait(10)
    registrar("Abrir site", "OK", "Página carregada com sucesso", round(time.time() - inicio, 2))

    # Login
    inicio = time.time()
    driver.find_element(By.ID, "email").send_keys("ana.silva@exemplo.com")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Entrar')]").click()
    time.sleep(5)
    registrar("Login", "OK", "Login executado com sucesso", round(time.time() - inicio, 2))

    # Botões principais
    botoes = ["Crianças", "Sessões", "Relatórios", "Atividades", "Dashboard"]
    for texto in botoes:
        inicio = time.time()
        try:
            botao = driver.find_element(By.XPATH, f"//*[contains(text(), '{texto}')]")
            botao.click()
            time.sleep(2)
            registrar(f"Clique em '{texto}'", "OK", f"Botão '{texto}' funcionou", round(time.time() - inicio, 2))
        except Exception as e:
            nome_print = f"erro_{texto}_{data_hora}.png"
            driver.save_screenshot(nome_print)
            registrar(f"Clique em '{texto}'", "Erro", f"{str(e)} - Print: {nome_print}", round(time.time() - inicio, 2))

except Exception as erro_geral:
    nome_print = f"erro_geral_{data_hora}.png"
    driver.save_screenshot(nome_print)
    registrar("Execução Geral", "Erro", f"{str(erro_geral)} - Print: {nome_print}")

finally:
    driver.quit()
    html.write("</table></body></html>")
    html.close()
    abrir_arquivo(nome_arquivo_html)
