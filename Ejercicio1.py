from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# ABRE EL NAVEGADOR
driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/index.html")
sleep(1)

# ABRIR FORMULARIO REGISTRO
registrar = driver.find_element(By.XPATH, "//*[@id='signin2']")
registrar.click()
sleep(1)

# RELLENAR FORMULARIO DE REGISTRO Y ENVIAR
usuario = driver.find_element(By.XPATH, "//*[@id='sign-username']")
usuario.send_keys("DayannaMacayITSQMET1")
sleep(1)
contraseña = driver.find_element(By.XPATH, "//*[@id='sign-password']")
contraseña.send_keys("123456")
sleep(1)
singup = driver.find_element(By.XPATH, "//*[@id='signInModal']/div/div/div[3]/button[2]")
singup.click()
sleep(1)
alert = driver.switch_to.alert 
alert.accept()
sleep(1)

# ABRIR FORMULARIO LOGIN
loguear = driver.find_element(By.XPATH, "//*[@id='login2']")
loguear.click()
sleep(1)

# RELLENAR FORMULARIO DE LOGIN Y ENVIAR
usuario = driver.find_element(By.XPATH, "//*[@id='loginusername']")
usuario.send_keys("DayannaMacayITSQMET1")
sleep(1)
contraseña = driver.find_element(By.XPATH, "//*[@id='loginpassword']")
contraseña.send_keys("123456")
sleep(1)
login = driver.find_element(By.XPATH, "//*[@id='logInModal']/div/div/div[3]/button[2]")
login.click()
sleep(1)

## DESLIZAR MEDIANTE SCROLL
mover = 1.5
scroll_height = driver.execute_script("return document.body.scrollHeight")
pixels_to_scroll = int(scroll_height * (mover / 10))
driver.execute_script(f"window.scrollBy(0, {pixels_to_scroll})")
sleep(1)

# SELECCIONAR PRODUCTOS
producto1 = driver.find_element(By.XPATH, "//*[@id='tbodyid']/div[4]/div/a/img")
producto1.click()
sleep(1)
addcard = driver.find_element(By.CLASS_NAME, "btn-success")
addcard.click()
sleep(1)
alert1 = driver.switch_to.alert 
alert1.accept()
sleep(1)
driver.get("https://www.demoblaze.com/index.html")
sleep(1)

producto2 = driver.find_element(By.XPATH, "//*[@id='tbodyid']/div[3]/div/div/h4/a")
producto2.click()
sleep(1)
addcard1 = driver.find_element(By.XPATH, "//*[@id='tbodyid']/div[2]/div/a")
addcard1.click()
sleep(1)
alert2 = driver.switch_to.alert 
alert2.accept()
sleep(1)

# IR AL CARRITO 
carrito = driver.find_element(By.XPATH, "//*[@id='cartur']")
carrito.click()
sleep(2)

# REALIZAR ORDEN
placeOrder = driver.find_element(By.CLASS_NAME, "btn-success")
placeOrder.click()
sleep(1)

nombre = driver.find_element(By.XPATH, "//*[@id='name']")
nombre.send_keys("Dayanna Macay")
sleep(1)
pais = driver.find_element(By.XPATH, "//*[@id='country']")
pais.send_keys("Ecuador")
sleep(1)
ciudad = driver.find_element(By.XPATH, "//*[@id='city']") 
ciudad.send_keys("Quito")
sleep(1)
tarjeta = driver.find_element(By.XPATH, "//*[@id='card']")
tarjeta.send_keys("458726981000")
sleep(1)
mes = driver.find_element(By.XPATH, "//*[@id='month']")
mes.send_keys("05")
sleep(1)
año = driver.find_element(By.XPATH, "//*[@id='year']")
año.send_keys("2028")
sleep(1)
purchase = driver.find_element(By.XPATH, "//*[@id='orderModal']/div/div/div[3]/button[2]")
purchase.click()
sleep(2)

ok = driver.find_element(By.XPATH, "/html/body/div[10]/div[7]/div/button")
ok.click()
sleep(1)

# CERRAR SESIÓN
logout = driver.find_element(By.XPATH, "//*[@id='logout2']")
logout.click()
sleep(3)