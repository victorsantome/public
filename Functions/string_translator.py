from textblob import TextBlob

def translating(text_to_translate,from_lang,to):
    """
    Translating with Python

    inputs :
    text_to_translate : str : text to translate
    from_lang : str : from a language
    to : str : to this language

    outputs :
    return : str : text translated
    """

    translater_man = TextBlob(text_to_translate)

    return translater_man.translate(from_lang='en', to = 'pt')

# applying it to a dataframe column
# df['nationality'].apply(translating)

# Test for this function :
# from textblob import TextBlob # pip install TextBlob
# print(translating("I love pizza", "en", "pt")) # should print "eu amo pizza"