import requests
import json
from win10toast import ToastNotifier

url = "http://api.openweathermap.org/data/2.5/weather?appid=fa2536ab2699a5077d09902716acddc2&q="
city = 'Hyderabad'

concat_url = url + city

response = requests.get(concat_url)
data = response.json()

temp = data['main']['temp'] - 273.15  # Converting recieved Kelvins into C
rounded_temp = "%.1f" % round(temp,2)

toaster = ToastNotifier()
toaster.show_toast('Wanna know weather!! its :', str(rounded_temp) + 'C')

