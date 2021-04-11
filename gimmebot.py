# coding=utf-8
import telepot
import requests
import config
from telepot.loop import MessageLoop
import urllib
import re
from bs4 import BeautifulSoup

"""#Questa roba serve per farlo funzionare su PythonEverywhere
proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
#Fine roba brutta, ugh"""

#Questa funzione serve per gestire un qualsiasi messaggio ricevuto
def on_chat_message(msg):
	# Link dal quale estraggo il cambio aggiornato
	#url = "https://prime.exchangerate-api.com/v5/"+config.getForex()+"/latest/USD"
	'''
	NUOVO SCRIPT PER IL NOSTRO CAMBIO DOLLARO EURO
	'''
	newurl = "https://transferwise.com/it/currency-converter/usd-to-eur-rate"
	newhtml = requests.get(newurl).text
	soup = BeautifulSoup(newhtml, 'html.parser')
	links = soup.findAll('span', {"class":"text-success"})
	finalmentegiustoconvert = str(links[0])[27:33]
	'''
	FINE SCRIPT
	'''
	# Contenitore dei tag
	alltags = "@Jack_96 @gotoxy @giuggi_lu @totina82 @Sopralapanca @Daniloat94 @niryasodd @sempronio18 @Fljku @Flank71 @fedabooks @CtrlAltCanc7 @Giuseppe09999 @claramant @Gojio @phasenite @testadalgh3 @Daxee @mhptsa @Davide5795 @Nallen1 @Erretr @Marty_na @supertramp88 @Gianmi17 @RealPuPpEt @The_Dude_82 @valebes"
	# Ricevo il json e estraggo in particolare la conversione DOLLAR/EUR, che è quella che mi serve
	#response = requests.get(url)
	#cambio = response.json()
	# dollar_to_eur = cambio["conversion_rates"]["EUR"]
	#dollar_to_eur = float(dollar_to_eur)

	content_type, chat_type, chat_id = telepot.glance(msg)
	if content_type == 'text':
		#In questo If schifoso aggiungo le parole chiave a cui il bot deve interagire
		if(msg["text"].startswith("!")):
			if("rosett" in msg["text"]):
				bot.sendPhoto(chat_id, "http://luiggi.altervista.org/pane.jpg")
			txtt = msg["text"]
			txtt = txtt.split('!')[1]
			lun = len(txtt)
			if(lun>128):
				lun = 128

			txtt = (txtt[0:lun]).upper()
			bot.sendMessage(chat_id, "SONO PRESENTI DEI TASK "+txtt+" \n\n"+alltags)
			if(msg["text"].startswith(config.getPower())):
				taxt = msg["text"]
				taxt = taxt.split(config.getPower())[1]
				taxt = taxt.upper()
				bot.sendMessage("-1001123977184",taxt)
			if(msg["text"]=="/help@reviubot"):
				bot.sendMessage(chat_id,"❔ Mi hanno aggiornato raga, finalmente la conversione funziona. Non vi dico più quella di Paypal però, tanto prima mentivo lol")
			if(msg["text"]=="/reviu@reviubot"):
				bot.sendMessage(chat_id,"🆘 SONO PRESENTI REVIU' \n\n"+alltags)
			if(msg["text"]=="/robadauno@reviubot"):
				bot.sendMessage(chat_id,"1️⃣ SONO PRESENTI ROBE DA 1 BRUTTE \n\n"+alltags)
			if(msg["text"]=="/robadadue@reviubot"):
				bot.sendMessage(chat_id,"2️⃣ SONO PRESENTI ROBE DA 2 BRUTTE \n\n"+alltags)
			if(msg["text"]=="/taskuo@reviubot"):
				bot.sendMessage(chat_id,"🔞 SONO PRESENTI UPSETTING/OFFENSIVE \n\n"+alltags)
			if(msg["text"]=="/images@reviubot"):
				bot.sendMessage(chat_id,"🌄 SONO PRESENTI IMAGE BELLISSIME \n\n"+alltags)
			if(msg["text"]=="/valuta@reviubot"):
				bot.sendMessage(chat_id,"💸 Attualmente, 1 dollaro = "+finalmentegiustoconvert+" euro.\n")



TOKEN = config.getToken()

bot = telepot.Bot(TOKEN)
bot.message_loop(on_chat_message)

print ('Listening ...')

import time
while 1:
	time.sleep(10)
