import requests
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

#Default Temperature Setting

url_ref = "https://raw.githubusercontent.com/SilviaLilli/ChatGPT-and-Italian-Dialects/main/data/texts/Sicilian%20to%20Italian_mytranslation.txt"
url_hyp = "https://raw.githubusercontent.com/SilviaLilli/ChatGPT-and-Italian-Dialects/main/data/texts/Sicilian_ChatGPTs%20Translation_DefTemp.txt"

response_ref = requests.get(url_ref)
response_hyp = requests.get(url_hyp)
      

reference = response_ref.text.split()
hypotesis = response_hyp.text.split()
smooth = SmoothingFunction().method7
score = sentence_bleu([reference], hypotesis, smoothing_function=smooth)
print(score)

        
#Low Temperature Setting

url_ref = "https://raw.githubusercontent.com/SilviaLilli/ChatGPT-and-Italian-Dialects/main/data/texts/Sicilian%20to%20Italian_mytranslation.txt"
url_hyp = "https://raw.githubusercontent.com/SilviaLilli/ChatGPT-and-Italian-Dialects/main/data/texts/Sicilian_ChatGPTs%20Translation_LowTemp.txt"

response_ref = requests.get(url_ref)
response_hyp = requests.get(url_hyp)

reference = response_ref.text.split()
hypotesis = response_hyp.text.split()
smooth = SmoothingFunction().method7
score = sentence_bleu([reference], hypotesis, smoothing_function=smooth)
print(score)


#High Temperature Setting

url_ref = "https://raw.githubusercontent.com/SilviaLilli/ChatGPT-and-Italian-Dialects/main/data/texts/Sicilian%20to%20Italian_mytranslation.txt"
url_hyp = "https://raw.githubusercontent.com/SilviaLilli/ChatGPT-and-Italian-Dialects/main/data/texts/Sicilian_ChatGPTs%20Translation_HiTemp.txt"

response_ref = requests.get(url_ref)
response_hyp = requests.get(url_hyp)

reference = response_ref.text.split()
hypotesis = response_hyp.text.split()
smooth = SmoothingFunction().method7
score = sentence_bleu([reference], hypotesis, smoothing_function=smooth)
print(score)
