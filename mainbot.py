# coding=utf-8
import telepot
import requests
import config
from telepot.loop import MessageLoop
import urllib
import re
from bs4 import BeautifulSoup
# leggo per la prima volta la lista degli iscritti e la carico nell'array alltags

filelista = open("listaiscritti.txt", "r")
listaiscritti = filelista.readlines()
alltags = ""
for line in listaiscritti:
    alltags = alltags + " " + line.strip()

# elimino i duplicati nel caso ci sia stato qualche furbone
def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist

alltags = ' '.join(unique_list(alltags.split()))

# funzione per aggiornare la lista iscritti
def updateUsers():
    global alltags
    alltags = ""
    filelista = open("listaiscritti.txt", "r")
    listaiscritti = filelista.readlines()
    for line in listaiscritti:
        alltags = alltags + " " + line.strip()
    alltags = ' '.join(unique_list(alltags.split()))

# inizializzo la roba per la valuta
url = "https://transferwise.com/it/currency-converter/usd-to-eur-rate"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")
links = soup.findAll('span', {'class':'text-success'})
converted = str(links[0])[27:31]

# messaggio dell'update (da aggiornare ogni volta)
helpMessage = "BELLA RAGA, SONO reviùbot! VI AIUTERÒ A NON PERDERE TRACCIA DEI TASK DISPONIBILI\n\nPer utilizzarmi, \
digita '!' seguito da un messaggio (ad esempio, !send) e ci penso io a taggare chi vuole essere taggato!\n\
Digita invece $aggiungi @tuonomeutente per aggiungerti agli iscritti, per essere taggato!\n \
Digita invece /valuta per conoscere il cambio dollaro-euro attuale\n\
Digita invece /glossario per conoscere i termini lavorativi\n\
Digita invece /help per rileggere questo!\n\n\
Grazie per l'attenzione, buon lavoro <3"

infoMessage = "SXS -> side by side\n\
SEND -> needs meeting senza sxs\n\
DEF -> quelle da 1 minuto con scritto in arancione di valutare solo lo scrb e non la landing page\n\
MET -> quelle simili alle def senza quella scritta con AET 1/3 minuti\n\
PSYCHO -> quelle da 1.5 o 2.5 minuti con commento obbligatorio\n\
VA -> virtual assistant 1 minuto\n\
AUDIO -> Cuffie\n\
LOCAL -> tipo sxs ma c'è scritto local in alto\n\
MAPS -> navigational intenet / business chain / other\n\
SNAPSHOT -> quelle che iniziano con i 3 screenshot lunghissimi dei siti di news\n\
ROSETTA -> quelle con una trentina di frasi da tradurre all'interno\n\
U/O -> upsetting offensive adult etc\n\
SCRB -> Special Content Result Block\n\
ATS -> About The Same\n\
NTR -> niente più task"
def on_chat_message(msg):
    global alltags
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == "text":
        if(msg["text"].startswith("!")):
            if("rosett" in msg["text"]): bot.sendPhoto(chat_id, "http://luiggi.altervista.org/pane.jpg")
            txtt = msg["text"]
            txtt = txtt.split('!')[1]
            lun = len(txtt)
            if(lun>128):
                    lun = 128

            txtt = (txtt[0:lun]).upper()
            bot.sendMessage(chat_id, "SONO PRESENTI DEI TASK " + txtt + "\n" + alltags)
        if(msg["text"].startswith(config.getPower())):
                        taxt = msg["text"]
                        taxt = taxt.split(config.getPower())[1]
                        taxt = taxt.upper()
                        bot.sendMessage("-1001123977184",taxt) # da cambiare l'id del gruppo
        if(msg["text"] == "/help" or msg["text"] == "/help@reviubot"):
            bot.sendMessage(chat_id, helpMessage)
        if(msg["text"].startswith("$aggiungi ")):
            user = msg["text"][10:]
            if(user[0] == "@"):
                user = "\n"+user
                f = open("listaiscritti.txt", "a")
                f.write(user)
                f.close()
                updateUsers()
                bot.sendMessage(chat_id, user + " aggiunto con successo!")
            else:
                bot.sendMessage(chat_id, "Mi spiace, non posso")
        if(msg["text"].startswith("$rimuovi ")):
            user = msg["text"][10:]
            nuser = "@"+user
            user = "\n"+user
            f = open("listaiscritti.txt", "r")
            listaiscritti = f.readlines()
            print(listaiscritti)
            print(nuser)
            if(nuser not in listaiscritti):
                nuser1 = nuser + "\n"
                listaiscritti.remove(nuser1)
                if(nuser1 not in listaiscritti):
                    nuser = " "+nuser
                    listaiscritti.remove(nuser)
            else:
                listaiscritti.remove(nuser)
            f = open("listaiscritti.txt", "w+")
            alltags = ""
            for line in listaiscritti:
                alltags = alltags + " " + line.strip()
            f.write(alltags)
            f.close()
            updateUsers()
            bot.sendMessage(chat_id, user + " rimosso con successo!")
        if(msg["text"] == "/valuta" or msg["text"] == "/valuta@reviubot"):
            bot.sendMessage(chat_id, "Attualmente, 1 dollaro = "+converted+" euro.")
        if(msg["text"] == "/glossario" or msg["text"] == "/glossario@reviubot"):
            bot.sendMessage(chat_id, infoMessage)

TOKEN = config.getToken()

bot = telepot.Bot(TOKEN)
bot.message_loop(on_chat_message)

print ('Listening ...')

import time
while 1:
        time.sleep(10)
