import json
import requests
from bs4 import BeautifulSoup
import datetime

print("Starting at " + str(datetime.datetime.now()))

siteURL = "https://newmexicostateparks.reserveamerica.com/"
webhookURL = "https://hooks.slack.com/services/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"
old_banner = "In an effort to reduce the spread of COVID-19 and as directed by the Governor, the Energy, Minerals and Natural Resources Department (EMNRD) announces that Day Use will be available to NM residents only. All other reservable facilities, including campsites, yurts and group shelters, at all NM State Parks will remain closed through at least February 26, 2021. All reservations through February 26, 2021 will be canceled and camping or facility fees refunded. Please see our FAQ page on State Parks limited openings for day use. If you have additional questions about State Parks closures, please call 505-476-3355."

page = requests.get(siteURL)
page_content = BeautifulSoup(page.content, 'html.parser')
banner = page_content.find('font')

def post_to_slack(message):
  slack_data = {'text': message}
  response = requests.post(
    webhookURL,
    json = slack_data,
    headers = {'Content-Type': 'application/json'}
  )
  print("Finished post_to_slack at " + str(datetime.datetime.now()))
  print("Response code: " + str(response.status_code))
  print("Response text: " + response.text)

if banner:

  text_to_test = banner.text
  # text_to_test = "All campgrounds are open!"

  if text_to_test != old_banner:
    message = ":mega: The banner has changed! The new banner reads: \n\n" + "*" + text_to_test + "*"
    post_to_slack(message)

  elif text_to_test == old_banner:
    message = ":pensive: No word yet. The banner has not yet changed."
    post_to_slack(message)

else:

  message = ":warning: No banner found! Check the site for details: "
  post_to_slack(message)

# python nmsp-scraper.py

