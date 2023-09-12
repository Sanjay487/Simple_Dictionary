from django.shortcuts import render
from PyDictionary import PyDictionary
from nltk.corpus import wordnet

# Create your views here.
def index(request):
    return render(request, 'index.html')

def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    synonyms, antonyms = synonym_antonym_extractor(search)
    context ={
        'meaning' :  getMeaning(meaning),
        'synonyms': synonyms,
        'antonyms': antonyms
       }
    return render(request, 'word.html', context)

def getMeaning(meaning):
    if "Noun" in meaning :
        if len(meaning["Noun"]) > 0 : return meaning["Noun"][0]
    return "Noun not found for this word"

def synonym_antonym_extractor(phrase):
    
    synonyms = []
    antonyms = []

    for syn in wordnet.synsets(phrase):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    
    return [synonyms, antonyms];



