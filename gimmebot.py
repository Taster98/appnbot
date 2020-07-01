# coding=utf-8
import telepot
import requests
import config
from telepot.loop import MessageLoop
#import urllib3

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
        url = "https://prime.exchangerate-api.com/v5/"+config.getForex()+"/latest/USD"
        
        # Ricevo il json e estraggo in particolare la conversione DOLLAR/EUR, che è quella che mi serve
        response = requests.get(url)
        cambio = response.json()
        dollar_to_eur = cambio["conversion_rates"]["EUR"]
        dollar_to_eur = float(dollar_to_eur)
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
                #In questo If schifoso aggiungo le parole chiave a cui il bot deve interagire
                if(msg["text"].startswith("!")):
                        txtt = msg["text"]
                        txtt = txtt.split('!')[1]
                        lun = len(txtt)
                        if(lun>128):
                                lun = 128

                        txtt = (txtt[0:lun]).upper()
                        bot.sendMessage(chat_id, "SONO PRESENTI DEI TASK "+txtt+" \n\n@Jack_96 @gotoxy @Sopralapanca @Daniloat94 @niryasodd @sempronio18 @Fljku @Flank71 @fedabooks @DavideCoccomini @CtrlAltCanc7 @Giuseppe09999 @claramant @Gojio @phasenite @testadalgh3")
                if(msg["text"].startswith(config.getPower())):
                        taxt = msg["text"]
                        taxt = taxt.split(config.getPower())[1]
                        taxt = taxt.upper()
                        bot.sendMessage("-1001123977184",taxt)
                if(msg["text"]=="/help@reviubot"):
                        bot.sendMessage(chat_id,"❔ Mi hanno aggiornato raga, ora il tasso euro dollaro funge perfettamente, e ho dei bottoni stupe.")
                if(msg["text"]=="/reviu@reviubot"):
                        bot.sendMessage(chat_id,"🆘 SONO PRESENTI REVIU' \n\n@Jack_96 @gotoxy @Sopralapanca @Daniloat94 @niryasodd @sempronio18 @Fljku @Flank71 @fedabooks @DavideCoccomini @CtrlAltCanc7 @Giuseppe09999 @claramant @Gojio @phasenite @testadalgh3")
		if(msg["text"]=="/robadauno@reviubot"):
                        bot.sendMessage(chat_id,"1️⃣ SONO PRESENTI ROBE DA 1 BRUTTE \n\n@Jack_96 @gotoxy @Sopralapanca @Daniloat94 @niryasodd @sempronio18 @Fljku @Flank71 @fedabooks @DavideCoccomini @CtrlAltCanc7 @Giuseppe09999 @claramant @Gojio @phasenite @testadalgh3")
		if(msg["text"]=="/robadadue@reviubot"):
                        bot.sendMessage(chat_id,"2️⃣ SONO PRESENTI ROBE DA 2 BRUTTE \n\n@Jack_96 @gotoxy @Sopralapanca @Daniloat94 @niryasodd @sempronio18 @Fljku @Flank71 @fedabooks @DavideCoccomini @CtrlAltCanc7 @Giuseppe09999 @claramant @Gojio @phasenite @testadalgh3")
		if(msg["text"]=="/taskuo@reviubot"):
                        bot.sendMessage(chat_id,"🔞 SONO PRESENTI UPSETTING/OFFENSIVE \n\n@Jack_96 @gotoxy @Sopralapanca @Daniloat94 @niryasodd @sempronio18 @Fljku @Flank71 @fedabooks @DavideCoccomini @CtrlAltCanc7 @Giuseppe09999 @claramant @Gojio @phasenite @testadalgh3")
		if(msg["text"]=="/images@reviubot"):
                        bot.sendMessage(chat_id,"🌄 SONO PRESENTI IMAGE BELLISSIME \n\n@Jack_96 @gotoxy @Sopralapanca @Daniloat94 @niryasodd @sempronio18 @Fljku @Flank71 @fedabooks @DavideCoccomini @CtrlAltCanc7 @Giuseppe09999 @claramant @Gojio @phasenite @testadalgh3")
		if(msg["text"]=="/valuta@reviubot"):
			bot.sendMessage(chat_id,"💸 Attualmente, 1 dollaro = "+str("%0.2f" % dollar_to_eur)+" euro.\nPer PayPal invece, da bravo monellone, \n1 dollaro = "+str("%0.2f" % (dollar_to_eur-(dollar_to_eur*2.5)/100))+" euro.")
                        


TOKEN = config.getToken()

bot = telepot.Bot(TOKEN)
bot.message_loop(on_chat_message)

print ('Listening ...')

import time
while 1:
        time.sleep(10)
