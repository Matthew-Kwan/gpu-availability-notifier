from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from decouple import config
from twilio.rest import Client

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.droptracker.ca")

time.sleep(10)

while True:

  # reset the gpu_list every loop
  gpu_list = []

  # exclude the first element for the headers
  elems = driver.find_elements_by_tag_name('center')[1:]
  td = driver.find_elements_by_tag_name('td')

  for i,element in enumerate(elems):
    if element.text == 'Quantity Remaining':
      continue

    elif int(element.text) > 0:
      index = 0 + (i*4)
      gpu_list.append(td[index].text)

    else:
      continue

  if len(gpu_list) > 0:
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = config('TWILIO_ACCOUNT_SID')
    auth_token = config('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                  body="gpus dropped",
                                  from_='+13654008424',
                                  to='+14167383838'
                              )

    print(message.sid)
    time.sleep(300)

  else:
    time.sleep(5)
    continue
