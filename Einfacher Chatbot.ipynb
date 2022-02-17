# Word2Vec Chatbot mit nur einem Wort als Input und fertigem Modell
# 
# Infos: https://rare-technologies.com/word2vec-tutorial/
# Dokumentation gensim: https://radimrehurek.com/gensim/models/keyedvectors.html
# Modell von hier: https://devmount.github.io/GermanWordEmbeddings/#download ==> als german.model downloaden

print('WILLKOMMEN ZUM CHATBOT')
print(' ')
print('Einlesen der Dateien... (dauert ein paar Sekunden)...')

# import modules & set up logging
import gensim
import string

# Einlesen bestehendes deutsches (!) Modell (dauert ca. 15 Sekunden
model = gensim.models.KeyedVectors.load_word2vec_format('german.model', binary=True)

# print(model)   # Eingelesen
# print(dir(model))  # Komponenten
# print(model.most_similar('Mann')) # o.k.

# Hier die Intents und Antworten des Bots
intent_answers = []
intent_answers.append(['Hallo', 'Hey, magst Du mir Fragen zu Karlsruhe stellen'])
intent_answers.append(['Wetter', 'Das Wetter ist meist sonnig'])
intent_answers.append(['Baden','In Karlsruhe gibt es viele Badeseen'])
intent_answers.append(['Studium','In Karlsruhe gibt es 5 Hochschulen mit vielen Angeboten'])
intent_answers.append(['Verbrechen','Karlsruhe ist eine sehr sichere Stadt'])
intent_answers.append(['Zoo','Karlsruhe hat einen sehr schönen Zoo mit Stadtpark'])
intent_answers.append(['Essen','Karlsruhe ist eine Studentenstadt - mit viel Currywurst (und etwas Döner)'])
intent_answers.append(['Wohnen','Karlsruhe ist sehr beliebt; Wohnen ist nicht immer einfach'])
intent_answers.append(['kuschelig','Die Katze ist am verschmusten'])
intent_answers.append(['Politik','Karlsruhe ist CDU-Land'])



# Aufsplitten in 2 Vektoren
intents = [item[0] for item in intent_answers]
answers = [item[1] for item in intent_answers]

print('Einlesen beendet!')

# Prüfen ob alle Intents im Modell enthalten sind
for intent in intents:
  if not(intent in model):
    print('ACHTUNG:', intent, 'ist nicht in Modell enthalten! Bitte Abbrechen und ändern!')

# Chat-Bot als Schleife
exit_list = ['stop', 'stopp', 'ende', 'break', 'quit', 'exit'] # alle kleingeschrieben!
print('--------------------------------------------------------------------------------------')
print('Hallo ich bin ein einfacher Chatbot...')
print('Ich kann aber nur auf Fragen mit einem Wort antworten...')
print('Bitte gebe einfach ein Wort zu einem Thema ein, welches Dich zu Karlsruhe interessiert')
print('Zum Aufhören bitte einfach -> stop <- tippen')
    
while(True):
  user_input = input()
  if user_input.lower() in exit_list:
    print('KA-Bot: Danke! Auf Wiedersehen')
    break
  if (user_input in model) == False:
      print('KA-Bot: Sorry, dieses Wort kenne ich nicht')
  else:
    intent = model.most_similar_to_given(user_input,intents) # sucht den nächsten passenden intent
    answer = answers[intents.index(intent)] # sucht die zugehörige Antwort
    print('KA-Bot: Deine Frage:', user_input, '... ist sehr ähnlich zu...', intent) # evtl. didaktisch relevant
    print('KA-Bot:', round(model.similarity(user_input,intent)*100), 'Prozent Übereinstimmung') # evtl. didaktisch relevant
    print('KA-Bot:', answer)
