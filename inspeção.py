from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager 

from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

from selenium.webdriver.common.by import By


navegador.get("file:///C:/Users/casa/Downloads/Senai/empresa.html")

navegador.implicitly_wait(3)


dados0 = navegador.find_element(By.TAG_NAME, "h1")[0].text
#dados1 = navegador.find_elements(By.TAG_NAME, "h1")[1].text
#dados2 = navegador.find_elements(By.CSS_SELECTOR, "container")[0].text
#dados3 = navegador.find_elements(By.LINK_TEXT, "index.html")[0].text
#dados4 = navegador.find_elements(By.CLASS_NAME, "value")[2].text

print(dados0)
#print(dados1)
#print(dados2)
#print(dados3)
#print(dados4)
