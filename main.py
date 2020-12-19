from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings('ignore')           # never print matching warnings

#Downlaod the punkt package
nltk.download('punkt',quiet=True)

# My article on corana crisis

article = Article('http://www.emro.who.int/health-topics/corona-virus/questions-and-answers.html')
article.download()
article.parse()
article.nlp()
articleText = article.text # it will take all text from article and put it into my variable
# print(articleText)

# Tokenization
text = articleText
sentence_list = nltk.sent_tokenize(text) # A list of sentences
# print(sentence_list)

def Response(text):
    text = text.lower()

    # Bots greeting Response
    bot_greeting  = ['howdy','hi','hey','HI']

    # user greeting Response
    user_greeting = ['hi','hey','hola','greeting','wass up dude','how are you bot']

    for word in text.split():
        if word in user_greeting:
            return random.choice(bot_greeting)

def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0,length))

    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]]>x[list_index[j]]:
                #swap
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
                #swap
    return list_index

################ (index_sort) it will give us the index of highest similarity Score ############


# Creating Bot Response
def bot_Response(user_input):
    user_input =  user_input.lower()
    sentence_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(sentence_list)  # count Matrix
    similarity_score = cosine_similarity(cm[-1],cm) # cm[-1] is last element in count matrix and comparing with all matrix element
    similarity_score_list = similarity_score.flatten()
    index = index_sort(similarity_score_list)
    index = index[1:]
    response_flag = 0
    # to check if any response back to the user #

    j = 0
    for i in range(len(index)):
        if similarity_score_list[index[i]]>0.0:
            bot_response = bot_response + ' ' + sentence_list[index[i]]
            response_flag = 1
            j = j+1
        if j>2:
             break
# edge case if i put wrong input
    if response_flag == 0 :
        bot_response = bot_response + ' ' + "I aplogize,I don't understand what ur command "

    sentence_list.remove(user_input)

    return bot_response
# ***************************

# Start the program
print('This is Harsh Samoliya Bot : Tells u about coroana diseases : To Exit Type ->exit ')
exit_list = ['exit','see u later','bye buddy','quiting ','break']
while (True):
    user_input = input()
    if user_input.lower() in exit_list:
        print('Harsh Bot : Nice Chatting you ')
        break
    else:
        if Response(user_input) != None:
            print('HarshBot : ' + Response(user_input))
        else:
            print('HarshBot : ' + bot_Response(user_input))



