from pathlib import Path
from selenium import webdriver # config do selenium
from selenium.webdriver.chrome.service import Service # config do selenium
from selenium.webdriver.common.by import By # importando o comando BY ( por )
from selenium.webdriver.common.keys import Keys  # importando o comando Keys ( Teclas )
from selenium.webdriver.support.wait import WebDriverWait # importa um comando para esperar carregar o q c quer
from selenium.webdriver.support import expected_conditions as EC
import time
# Caminho para o chrome driver
ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXEC = ROOT_FOLDER / "Drivers" / "chromedriver.exe"
TIME_TO_WAIT = 60

# Settings que você precisa usar
chrome_options = webdriver.ChromeOptions() # Opções que iremos passar
chrome_service = Service(executable_path=CHROMEDRIVER_EXEC) # Qual seviço vai usar o chrome driver
chrome_browser = webdriver.Chrome(
    service=chrome_service,
    options=chrome_options,
) # aqui é o navegador em si, essas são as configurações basicas para o usar o selenium em QUALQUER COISA

# a partir daqui começa os codigos, acima temos apenas configs basicas

chrome_browser.get("https://www.google.com.br/?hl=pt-BR") # abre qualquer link que eu passar 

#o codigo abaixo vai esperar até que o elemento que eu encontrei (name " q"), seja carregado para executar
achar_input = WebDriverWait(chrome_browser,TIME_TO_WAIT ).until(
    EC.presence_of_element_located((By.NAME, 'q'))
)

achar_site = WebDriverWait(chrome_browser,TIME_TO_WAIT).until(
    EC.presence_of_element_located(By.CLASS_NAME,"LC20lb MBeuO DKV0Md")
)

achar_input.send_keys("como conquistar a minha namorada") # caso ele ACHE o meu elemento que é o inpiut, ele ira digitar hello world
time.sleep(5)
achar_input.send_keys(Keys.ENTER)


# coisas que você deve achar no html para identificar o que você quer alcançar no codigo
# ID, NAME, as vezes CLASS

time.sleep(TIME_TO_WAIT)