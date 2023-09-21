import requests
from nltk.tokenize import sent_tokenize
from comet import download_model, load_from_checkpoint

def evaluate_comet(url_src, url_mt, url_ref):
    response_src = requests.get(url_src)
    response_mt = requests.get(url_mt)
    response_ref = requests.get(url_ref)
    
    source_sentences = sent_tokenize(response_src.text)
    met_sentences = sent_tokenize(response_mt.text)
    refer_sentences = sent_tokenize(response_ref.text)

    if len(source_sentences) == len(met_sentences) == len(refer_sentences):
        data = [{"src": src, "mt": mt, "ref": ref} for src, mt, ref in zip(source_sentences, met_sentences, refer_sentences)]
        model_output = model.predict(data, batch_size=8, gpus=1)
        print(model_output)
    else:
        print("The number of sentences in source, mt and ref files are not equal.")

if __name__ == '__main__':
    model_path = download_model("Unbabel/wmt22-comet-da")
    model = load_from_checkpoint(model_path)
    
    #My translation as source
    url_src = "https://raw.githubusercontent.com/SilviaLilli/ChatGPT-and-Italian-Dialects/main/data/texts/Milanese%20to%20Italian_mytranslation.txt"
    url_mt = "https://raw.githubusercontent.com/SilviaLilli/ChatGPT-and-Italian-Dialects/main/data/texts/ITA%20to%20Milanese_ChatGPTs%20Translation_fromMyTransl.txt"
    url_ref = ""https://raw.githubusercontent.com/SilviaLilli/ChatGPT-and-Italian-Dialects/main/data/texts/Milanese_El%20Princip%20Piscinin.txt""
    evaluate_comet(url_src, url_mt, url_ref)

    #Brigoli's translation as source
    url_src = "https://raw.githubusercontent.com/SilviaLilli/ChatGPT-and-Italian-Dialects/main/data/texts/Italian_Il%20Piccolo%20Principe_BompianiBrigoli"
    url_mt = "https://raw.githubusercontent.com/SilviaLilli/ChatGPT-and-Italian-Dialects/main/data/texts/ITA%20to%20Milanese_ChatGPTs%20Translation_fromBrigoli.txt"
    url_ref = "https://raw.githubusercontent.com/SilviaLilli/ChatGPT-and-Italian-Dialects/main/data/texts/Milanese_El%20Princip%20Piscinin.txt"
    evaluate_comet(url_src, url_mt, url_ref)

  
