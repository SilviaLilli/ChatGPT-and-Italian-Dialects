import requests
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction


        
#My translation as source

url_ref = "https://raw.githubusercontent.com/SilviaLilli/ChatGPT-and-Italian-Dialects/main/data/texts/Roman%20Dialect_Er%20principetto.txt"
url_hyp = "https://raw.githubusercontent.com/SilviaLilli/ChatGPT-and-Italian-Dialects/main/data/texts/ITA%20to%20Roman_ChatGPTs%20Translation_fromMyTransl.txt"

response_ref = requests.get(url_ref)
response_hyp = requests.get(url_hyp)

reference = response_ref.text.split()
hypotesis = response_hyp.text.split()
smooth = SmoothingFunction().method7
score = sentence_bleu([reference], hypotesis, smoothing_function=smooth)
print(score)



#Brigoli's translation as source

url_ref = "https://raw.githubusercontent.com/SilviaLilli/ChatGPT-and-Italian-Dialects/main/data/texts/Roman%20Dialect_Er%20principetto.txt"
url_hyp = "https://raw.githubusercontent.com/SilviaLilli/ChatGPT-and-Italian-Dialects/main/data/texts/ITA%20to%20Roman_ChatGPTs%20Translation_fromBrigoli.txt"

response_ref = requests.get(url_ref)
response_hyp = requests.get(url_hyp)
      

reference = response_ref.text.split()
hypotesis = response_hyp.text.split()
smooth = SmoothingFunction().method7
score = sentence_bleu([reference], hypotesis, smoothing_function=smooth)
print(score)
