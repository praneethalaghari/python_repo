from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from cryptography.fernet import Fernet


import pyttsx3
import time


def password():
	#key = Fernet.generate_key()
	key = b'XpQu2hhMOyDhKs222X_CX5dfyLBUPWaoX93t_3-fkS8='   # Selected one of the key and generated below encrypt value

	f = Fernet(key)

	#encrypt_value = f.encrypt(b"<password here>")
	encrypt_value = b'gAAAAABeGLw8mHQBdvh5jDZyDzaigWMwyaMSSZSoabBKytVo4CvWwzFd7XI50JAcb-3W6l3KSofNVxyx8XaWcXTKQpyVH4zBUA==' #Selected one of encrypt_value

	decrypt_value = f.decrypt(encrypt_value)

	return decrypt_value.decode('utf-8')  # THis is to convert from byte stream to string i.e b'string' to 'string'

	
def run():

	engine = pyttsx3.init()

	driver = webdriver.Firefox()
	to_website = 'freecharge'
	driver.get('https://www.' + to_website + '.com')

	driver.implicitly_wait(30)
		
	login_button = driver.find_element_by_class_name('_3mvx0')
	login_button.click()

	print(driver.current_url)
	driver.get(driver.current_url)

	driver.implicitly_wait(30)

	mobile_num_field = driver.find_element_by_name('checkUsername')
	mobile_num_field.send_keys('9573340942')


	delay = 5
	try:
		WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.NAME, "password")))
		print("Element available!")
		time.sleep(5)
		password_field = driver.find_element_by_name("password")
		password_field.send_keys(password())
		password_field.submit()
		time.sleep(3)
		engine.say("Freecharge Login succesful")
		engine.runAndWait()
	except TimeoutException:
		engine.say("Unable to open website.Please try again")
		engine.runAndWait()


if __name__ == "__main__":
	run()
