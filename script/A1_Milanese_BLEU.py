from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

with open (r"https://raw.githubusercontent.com/SilviaLilli/ChatGPT-and-Italian-Dialects/main/data/texts/Milanese%20to%20Italian_mytranslation.txt", "r") as ref:
    with open (r"https://raw.githubusercontent.com/SilviaLilli/ChatGPT-and-Italian-Dialects/main/data/texts/Milanese_ChatGPTs%20Translation_DefTemp.txt", "r") as hyp:
        

        reference = ref.read().split()
        hypotesis = hyp.read().split()
        smooth = SmoothingFunction().method7
        score = sentence_bleu([reference], hypotesis, smoothing_function=smooth)
        print(score)

        


with open (r"https://raw.githubusercontent.com/SilviaLilli/ChatGPT-and-Italian-Dialects/main/data/texts/Milanese%20to%20Italian_mytranslation.txt", "r") as ref:
    with open (r"https://raw.githubusercontent.com/SilviaLilli/ChatGPT-and-Italian-Dialects/main/data/texts/Milanese_ChatGPTs%20Translation_LowTemp.txt", "r") as hyp:
        

        reference = ref.read().split()
        hypotesis = hyp.read().split()
        smooth = SmoothingFunction().method7
        score = sentence_bleu([reference], hypotesis, smoothing_function=smooth)
        print(score)

        


with open (r"https://raw.githubusercontent.com/SilviaLilli/ChatGPT-and-Italian-Dialects/main/data/texts/Milanese%20to%20Italian_mytranslation.txt", "r") as ref:
    with open (r"https://raw.githubusercontent.com/SilviaLilli/ChatGPT-and-Italian-Dialects/main/data/texts/Milanese_ChatGPTs%20Translation_LowTemp.txt", "r") as hyp:
        

        reference = ref.read().split()
        hypotesis = hyp.read().split()
        smooth = SmoothingFunction().method7
        score = sentence_bleu([reference], hypotesis, smoothing_function=smooth)
        print(score)


