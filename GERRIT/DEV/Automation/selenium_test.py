from selenium import webdriver


driver = webdriver.Firefox()
driver.get('https://youtube.com')
driver.implicitly_wait(30)
search_form = driver.find_element_by_name('search_query')
search_form.send_keys('Hello')
search_form.submit()

#href="/watch?=0hGGaVCCgPk"