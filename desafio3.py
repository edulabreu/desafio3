import json
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ==========================
# LOAD DATA
# ==========================

with open("data.json", encoding="utf-8") as f:
    dados = json.load(f)


# ==========================
# DRIVER
# ==========================
options = webdriver.ChromeOptions()

options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

navegador = webdriver.Chrome(options=options)
wait = WebDriverWait(navegador, 10)

navegador.get("https://demoqa.com/automation-practice-form")


# remove banners fixos que atrapalham clique
navegador.execute_script("""
document.querySelector('#fixedban')?.remove();
document.querySelector('footer')?.remove();
""")

# NOME

wait.until(EC.presence_of_element_located((By.ID, "firstName"))).send_keys(dados["nome"])

navegador.find_element(By.ID, "lastName").send_keys(dados["sobrenome"])
navegador.find_element(By.ID, "userEmail").send_keys(dados["email"])


# GENERO

navegador.find_element(By.XPATH, f"//label[text()='{dados['genero']}']").click()

# TELEFONE

navegador.find_element(By.ID, "userNumber").send_keys(dados["telefone"])

# DATA NASCIMENTO

date_input = navegador.find_element(By.ID, "dateOfBirthInput")

navegador.execute_script("arguments[0].scrollIntoView({block:'center'});", date_input)
navegador.execute_script("arguments[0].click();", date_input)

date_input.send_keys(Keys.CONTROL + "a")
date_input.send_keys(dados["data_nascimento"])
date_input.send_keys(Keys.ENTER)

# ASSUNTOS

subject_input = navegador.find_element(By.ID, "subjectsInput")

for subject in dados["subjects"]:
    subject_input.send_keys(subject)
    subject_input.send_keys(Keys.ENTER)

# HOBBIES

for hobby in dados["hobbies"]:
    navegador.find_element(By.XPATH, f"//label[text()='{hobby}']").click()


# UPLOAD

caminho_imagem = os.path.abspath(dados["arquivo"])

navegador.find_element(By.ID, "uploadPicture").send_keys(caminho_imagem)


# ENDEREÇO

navegador.find_element(By.ID, "currentAddress").send_keys(dados["address"])


# ESTADO

state_input = navegador.find_element(By.ID, "react-select-3-input")
state_input.send_keys(dados["state"])
state_input.send_keys(Keys.ENTER)


# CIDADE

city_input = navegador.find_element(By.ID, "react-select-4-input")
city_input.send_keys(dados["city"])
city_input.send_keys(Keys.ENTER)


# SUBMIT

navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")

submit = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
navegador.execute_script("arguments[0].click();", submit)


# MODAL VALIDATION

modal_title = wait.until(
    EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
)

assert "Thanks for submitting the form" in modal_title.text

modal_body = navegador.find_element(By.CLASS_NAME, "modal-body").text

assert dados["nome"] in modal_body
assert dados["email"] in modal_body
assert dados["telefone"] in modal_body

print("✓ Formulário enviado com sucesso")


# ==========================
# SCREENSHOT
# ==========================
navegador.save_screenshot("confirmation.png")

print("✓ Screenshot salva")


navegador.quit()