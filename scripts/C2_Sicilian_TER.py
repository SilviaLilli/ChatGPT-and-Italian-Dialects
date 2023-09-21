import requests
import pyter

#My traslation as source

url_ref = "https://raw.githubusercontent.com/SilviaLilli/ChatGPT-and-Italian-Dialects/main/data/texts/Sicilian_U%20principinu.txt"
url_hyp = "https://raw.githubusercontent.com/SilviaLilli/ChatGPT-and-Italian-Dialects/main/data/texts/ITA%20to%20Sicilian_ChatGPTs%20Translation_fromMyTransl.txt"

response_ref = requests.get(url_ref)
response_hyp = requests.get(url_hyp)

reference = response_ref.text.split()
hypotesis = response_hyp.text.split()
score = pyter.ter(hypotesis, reference)
print(score)

#Brigoli's translation as source

url_ref = "https://raw.githubusercontent.com/SilviaLilli/ChatGPT-and-Italian-Dialects/main/data/texts/Sicilian_U%20principinu.txt"
url_hyp = "https://raw.githubusercontent.com/SilviaLilli/ChatGPT-and-Italian-Dialects/main/data/texts/ITA%20to%20Sicilian_ChatGPTs%20Translation_fromBrigoli.txt"

response_ref = requests.get(url_ref)
response_hyp = requests.get(url_hyp)

reference = response_ref.text.split()
hypotesis = response_hyp.text.split()
score = pyter.ter(hypotesis, reference)
print(score)
