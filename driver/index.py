from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time 

service = Service("driver/chromedriver.exe")
bot = webdriver.Chrome(service = service)

bot.maximize_window()
time.sleep(5)

bot.get("https://www.viajesexito.com")
time.sleep(6)

publicidad = bot.find_element(By.XPATH, '/html/body/div/div/div/div[1]/svg/path')
time.sleep(5)
publicidad.click()
time.sleep(6)

paquete = bot.find_element(By.XPATH, '/html/body/form/header/div[2]/div/div/nav/div[4]/a')
time.sleep(5)
paquete.click()
time.sleep(6)

origen = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
origen.click()
origen.send_keys("Aeropuerto José María Cordova (MDE)")
time.sleep(5)

destino = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
destino.click()
destino.send_keys("Punta Cana, Republica Dominicana (PUJ)")
time.sleep(5)

fecha_ida = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div/div[1]')
fecha_ida.click()
time.sleep(5)

fecha_ida_dia = bot.find_element(By.XPATH, '/html/body/div[11]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[6]')
fecha_ida_dia.click()
time.sleep(5)

fecha_ida_aceptar = bot.find_element(By.XPATH, '/html/body/div[11]/div[2]/div[2]/div[3]/button[2]')
fecha_ida_aceptar.click()
time.sleep(5)

fecha_vuelta = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]')
fecha_vuelta.click()
time.sleep(5)

fecha_vuelta_dia = bot.find_element(By.XPATH, '/html/body/div[11]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[2]/div[2]/div[1]')
fecha_vuelta_dia.click()
time.sleep(5)

fecha_vuelta_aceptar = bot.find_element(By.XPATH, '/html/body/div[11]/div[2]/div[2]/div[3]/button[2]')
fecha_vuelta_aceptar.click()
time.sleep(5)

habitacion = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[3]/div/div/div/div/p')
habitacion.click()
time.sleep(5)

habitaciones =bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[1]/div[2]')
habitaciones.click()
time.sleep(5)

habitaciones_aceptar = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[2]/button')
habitaciones.click()
time.sleep(5)



