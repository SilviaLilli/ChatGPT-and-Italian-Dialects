from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

with open (r"data/texts/Milanese to Italian_mytranslation.txt", "r") as ref:
    with open (r"", "r") as hyp:
        

        reference = ref.read().split()
        hypotesis = hyp.read().split()
        smooth = SmoothingFunction().method7
        score = sentence_bleu([reference], hypotesis, smoothing_function=smooth)
        print(score)

        


with open (r"", "r") as ref:
    with open (r"", "r") as hyp:
        

        reference = ref.read().split()
        hypotesis = hyp.read().split()
        smooth = SmoothingFunction().method7
        score = sentence_bleu([reference], hypotesis, smoothing_function=smooth)
        print(score)

        


with open (r"", "r") as ref:
    with open (r"", "r") as hyp:
        

        reference = ref.read().split()
        hypotesis = hyp.read().split()
        smooth = SmoothingFunction().method7
        score = sentence_bleu([reference], hypotesis, smoothing_function=smooth)
        print(score)


