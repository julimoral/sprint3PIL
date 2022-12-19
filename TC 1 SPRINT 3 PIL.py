import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()
driver.get('https://shop.samsung.com/ar/')
time.sleep(10)

time.sleep(3)
#cierropopup
cerrarventana = webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
#time.sleep(3)

#aceptocookies
#driver.find_element(By.ID, 'truste-consent-button').click()
time.sleep(10)

#Inicio sesión
inicioDeSesion = driver.find_element(By.XPATH, '//*[@id="headerSamsung"]/div[2]/div/div/div[2]/div/div[2]/ul[2]/li[2]')
inicioDeSesion.click()
time.sleep(20)

#cierropopup
cerrarventana = webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

#crearcuenta
crearcuenta = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/form/div[5]/a')
crearcuenta.click()
time.sleep(10)

#escribiremail
input_User = driver.find_element(By.NAME, 'email')
input_User.send_keys('culimoral@gmail.com')
time.sleep(5)

#enviartoken
enviar = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/form/div[2]/div[2]/button/div')
enviar.click()

time.sleep(20)

#INGRESO EL TOKEN MANUALMENTE

#creounacontraseña
input_contraseña = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/form/div[2]/div/label/div/input')
input_contraseña.send_keys('Juli1234')

#confirmocontraseña
input_confirmarcontraseña = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/form/div[3]/label/div/input')
input_confirmarcontraseña.send_keys('Juli1234')

time.sleep(5)

#aceptocookies
driver.find_element(By.ID, 'truste-consent-button').click()
time.sleep(10)

#terminodecrearlacuenta - validando el mail y pass - 
crear = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/form/div[4]/div[2]/button/div/span')
crear.click()

time.sleep(5)

requirement = ()     #Expected Result
labelObtained = ()      #Actual Result

def crearcuenta():
    if requirement in labelObtained:
        print("Pass")
    else:
        print("Fail")



validarcorreo = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/form/div[4]/div[2]/button/div')   
#Aquí identificamos el elemento

crearnuevacuenta = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/form/div[4]/div[2]/button/div').text
#Aquí extraemos el texto dentro del elemento

labelObtained = crearcuenta

print(labelObtained)

requirement = 'crearnuevacuenta'

crearcuenta()

time.sleep(10)

#cierropopup
popup = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div/section/div[1]/button")
popup.click()

time.sleep(5)

driver.close()

