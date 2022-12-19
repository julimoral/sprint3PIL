import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome (executable_path='C:Users Admin Downloads chromedriver_win32') 
driver.maximize_window()
driver.get('https://shop.samsung.com/ar/login?returnUrl=%2Far%2Faccount')

time.sleep(3)

cerrarventana = webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

time.sleep(10)

email = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/form/div[1]/label/div/input')
email.send_keys('culimoral@gmail.com')

password = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/form/div[2]/div/label/div/input')
password.send_keys('Juli1234')

time.sleep(5)

entrar = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/form/div[4]/div/button/div/span')
entrar.click()

time.sleep(20)

cerrarventana = webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

time.sleep(5)

cookies = driver.find_element(By.ID, 'truste-consent-button')
cookies.click()

editardatos = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/section/main/main/div[1]/div/div/article/footer/button/div')
editardatos.click()

time.sleep(3)

nombre = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/section/main/div/div/article/main/form/div[1]/div[1]/label/div/input')
nombre.send_keys(Keys.CONTROL + "a")
time.sleep(5)

nombre = driver.find_element(By.NAME, 'firstName')
nombre.send_keys('Julieta')

time.sleep(2)

apellido = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/section/main/div/div/article/main/form/div[1]/div[2]/label/div/input')
apellido.send_keys(Keys.CONTROL + "a")

time.sleep(3)

apellido = driver.find_element(By.NAME, 'lastName')
apellido.send_keys('Moral')

time.sleep(10)

dni = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/section/main/div/div/article/main/form/div[1]/div[4]/label/div[1]/input')
dni.send_keys(Keys.CONTROL + "a")

dni = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/section/main/div/div/article/main/form/div[1]/div[4]/label/div[1]/input')
dni.send_keys(11)

telefono = driver.find_element(By.NAME, 'homePhone')
telefono.click()

time.sleep(5)

requirement = ()     #Expected Result
labelObtained = ()      #Actual Result

def dninovalido():
    if requirement in labelObtained:
        print("Pass")
    else:
        print("Fail")



documento = driver.find_element(By.NAME, 'document')   
#Aquí identificamos el elemento

documentodni = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/section/main/div/div/article/main/form/div[1]/div[4]/label/div[2]').text
#Aquí extraemos el texto dentro del elemento

labelObtained = documentodni

print(labelObtained)

requirement = 'Valor no válido.'

dninovalido()

time.sleep(10)

driver.close()






