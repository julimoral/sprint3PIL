import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome (executable_path='C:Users Admin Downloads chromedriver_win32') 
driver.maximize_window()
driver.get('https://shop.samsung.com/ar/login?returnUrl=%2Far%2Faccount')

time.sleep(3)

#cerrarventana
cerrarventana = webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
time.sleep(7)

#tipearemail
email = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/form/div[1]/label/div/input')
email.send_keys('culimoral@gmail.com')

#tipearpassw
password = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/form/div[2]/div/label/div/input')
password.send_keys('Juli1234')
time.sleep(3)

#loguearse
entrar = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/form/div[4]/div/button/div/span')
entrar.click()

time.sleep(20)

cerrarventana = webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

time.sleep(7)

#cerrarcookies
cookies = driver.find_element(By.ID, 'truste-consent-button')
cookies.click()

time.sleep(3)

#clickeardirecciones
direcciones = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/aside/nav/div[1]/div[2]/a')
direcciones.click()

time.sleep(5)

#añadirnuevadire
agregardireccion = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/section/header/div[2]/div/div[2]/div[2]/a/button/div')
agregardireccion.click()

time.sleep(5)

#ingresarCP
cp = driver.find_element(By.NAME, 'postalCode')
cp.send_keys('5189')

time.sleep(3)

#ingresarcalle
calle = driver.find_element(By.NAME, 'street')
calle.send_keys('25 de mayo')

time.sleep(1)

#ingresarnumeracion
numero = driver.find_element(By.NAME, 'number')
numero.send_keys('1375')

time.sleep(3)

#ingresarprovincia
provincia = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/section/main/div/article/main/div[2]/div[7]/div/label/div/select')
provincia.click()

time.sleep(3)

provincia = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/section/main/div/article/main/div[2]/div[7]/div/label/div/select/option[7]')
provincia.click()

time.sleep(3)

#ingresarciudad
ciudad = driver.find_element(By.NAME, 'city')
ciudad.click()

time.sleep(10)

ciudad = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/section/main/div/article/main/div[2]/div[8]/div/label/div/select/option[51]')
ciudad.click()

time.sleep(5)

requirement = ()     #Expected Result
labelObtained = ()      #Actual Result

def formulariodirecciones():
    if requirement in labelObtained:
        print("Pass")
    else:
        print("Fail")



direccion = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/section/main/div/article/main/div[2]/div[2]/label/div[1]/input')   
#Aquí identificamos el elemento

calle = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div/section/main/div/article/main/div[2]/div[2]/label/div[1]/input').text
#Aquí extraemos el texto dentro del elemento

labelObtained = 'Calle'

print(labelObtained)

requirement = '25 de mayo'

formulariodirecciones()

#nombredelapersonaquerecibe
personaquerecibe = driver.find_element(By.NAME, 'receiverName')
personaquerecibe.send_keys(Keys.CONTROL + "a")

personaquerecibe = driver.find_element(By.NAME, 'receiverName')
personaquerecibe.send_keys('Julieta Moral')

time.sleep(10)

driver.close()


