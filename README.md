# 🚀 Testes de Front-End para a Plataforma ASPCT

Este repositório contém a suíte de **testes de Interface do Usuário (UI)** para a aplicação **ASPCT Software Frontend** (disponível em `https://v0-aspct-software-frontend.vercel.app/login`).

Os testes são desenvolvidos em **Python** usando o **Selenium WebDriver** e visam verificar o fluxo de **Login** e a **Navegação** dos diferentes perfis de usuário (`Psicólogo` e `Pai`).

---

## 💻 Tecnologias e Dependências

Os testes foram desenvolvidos utilizando as seguintes ferramentas:

* **Linguagem:** **[Python](https://docs.python.org/3.11)** ($\ge$ 3.8) 
* **Framework de Automação:** **[Selenium WebDriver](https://www.selenium.dev/documentation/webdriver)**
* **Gerenciador de Browser:** **[Selenium Manager](https://www.selenium.dev/documentation/selenium_manager)** (usado por padrão no Selenium 4+, não requer download manual de drivers)
* **Browsers Suportados:** Google Chrome e Opera GX.

### Instalação das Dependências

1.  **Instale o Selenium:**

    ```bash
    pip install selenium
    ```

---

## ▶️ Perfis de Teste e Execução

O projeto está organizado para executar testes em diferentes perfis de usuário. Escolha o arquivo de acordo com o perfil que deseja testar:

| Arquivo de Teste | Perfil Testado | Resumo do Fluxo |
| :--- | :--- | :--- |
| **`SeleniumPsicologo.py`** | Psicólogo | Faz login com `ana.silva@exemplo.com` e navega por: **Crianças**, **Relatórios**, **Atividades** e **Dashboard**. |
| **`SeleniumPai.py`** | Pai/Responsável | Faz login com `carlos@exemplo.com` e navega por: **Progresso** e **Meus Filhos**. |
| **`from selenium import webdriver.py`** | Psicólogo **(Relatório)** | Executa os mesmos testes do Psicólogo, gerando um **Relatório HTML** detalhado com *logs* e *screenshots*. |

### Comandos de Execução

Para executar um teste, use o interpretador Python na raiz do projeto:

```bash
# Executa o teste do perfil Psicólogo
python SeleniumPsicologo.py

# Executa o teste do perfil Pai/Responsável
python SeleniumPai.py

# Executa o teste do Psicólogo com Geração de Relatório
python "from selenium import webdriver.py"
