from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager 

from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

from selenium.webdriver.common.by import By


navegador.get("https://mateus-crio.github.io/forna/")

navegador.implicitly_wait(3)


dados0 = navegador.find_element(By.CLASS_NAME, "nav_logo")
dados1 = navegador.find_elements(By.TAG_NAME, "legend")[0].text
dados2 = navegador.find_elements(By.CSS_SELECTOR, "div.inputBox")[3].text
dados3 = navegador.find_elements(By.ID,"header")[0].text
dados4 = navegador.find_elements(By.XPATH, "/html/body/main/div/form/fieldset/div[1]/label")[0].text
dados5 = navegador.find_elements(By.LINK_TEXT, "Tabela geral da empresa")[0].text
dados6 = navegador.find_elements(By.NAME, "CPF")[0].tag_name

print(dados0.get_attribute("outerHTML"))
print(dados1)
print(dados2)
print(dados3)
print(dados4)
print(dados5)
print(dados6)