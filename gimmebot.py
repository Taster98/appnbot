import telepot
#import urllib3

from forex_python.converter import CurrencyRates
c = CurrencyRates()

"""#Questa roba serve per farlo funzionare su PythonEverywhere
proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
#Fine roba brutta, ugh"""

#Questa funzione serve per gestire un qualsiasi messaggio ricevuto
def on_chat_message(msg):
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
                        bot.sendMessage(chat_id, "SONO PRESENTI DEI TASK "+txtt+" \n\n@Jack_96 @gotoxy @Sopralapanca @Daniloat94 @niryasodd @sempronio18 @Fljku @Flank71 @fedabooks @DavideCoccomini @CtrlAltCanc7 @Giuseppe09999 @claramant")
                if(msg["text"].startswith(config.getPower())):
                        taxt = msg["text"]
                        taxt = taxt.split(config.getPower())[1]
                        taxt = taxt.upper()
                        bot.sendMessage("-1001123977184",taxt)
                if(msg["text"]=="/help@reviubot"):
                        bot.sendMessage(chat_id,"Mi hanno aggiornato aggiungendomi questi comandi molto fighi, per velocizzare il tutto. Puoi anche vedere la valuta euro dollaro.")
                if(msg["text"]=="/reviu@reviubot"):
                        bot.sendMessage(chat_id,"SONO PRESENTI REVIU' \n\n@Jack_96 @gotoxy @Sopralapanca @Daniloat94 @niryasodd @sempronio18 @Fljku @Flank71 @fedabooks @DavideCoccomini @CtrlAltCanc7 @Giuseppe09999 @claramant")
		if(msg["text"]=="/uno@reviubot"):
                        bot.sendMessage(chat_id,"SONO PRESENTI ROBE DA 1 BRUTTE \n\n@Jack_96 @gotoxy @Sopralapanca @Daniloat94 @niryasodd @sempronio18 @Fljku @Flank71 @fedabooks @DavideCoccomini @CtrlAltCanc7 @Giuseppe09999 @claramant")
		if(msg["text"]=="/due@reviubot"):
                        bot.sendMessage(chat_id,"SONO PRESENTI ROBE DA 2 BRUTTE \n\n@Jack_96 @gotoxy @Sopralapanca @Daniloat94 @niryasodd @sempronio18 @Fljku @Flank71 @fedabooks @DavideCoccomini @CtrlAltCanc7 @Giuseppe09999 @claramant")
		if(msg["text"]=="/uo@reviubot"):
                        bot.sendMessage(chat_id,"SONO PRESENTI UPSETTING/OFFENSIVE \n\n@Jack_96 @gotoxy @Sopralapanca @Daniloat94 @niryasodd @sempronio18 @Fljku @Flank71 @fedabooks @DavideCoccomini @CtrlAltCanc7 @Giuseppe09999 @claramant")
		if(msg["text"]=="/image@reviubot"):
                        bot.sendMessage(chat_id,"SONO PRESENTI IMAGE BELLISSIME \n\n@Jack_96 @gotoxy @Sopralapanca @Daniloat94 @niryasodd @sempronio18 @Fljku @Flank71 @fedabooks @DavideCoccomini @CtrlAltCanc7 @Giuseppe09999 @claramant")
		if(msg["text"]=="/valuta@reviubot"):
			bot.sendMessage(chat_id,"Attualmente, 1 dollaro = "+str(round(c.get_rate('USD','EUR'),2))+" euro.\nPer PayPal invece, da bravo monellone, \n1 dollaro = "+str(round((c.get_rate('USD','EUR')-(c.get_rate('USD','EUR')*2.5)/100),2))+" euro.")


import config
TOKEN = config.getToken()

bot = telepot.Bot(TOKEN)
bot.message_loop(on_chat_message)

print ('Listening ...')

import time
while 1:
        time.sleep(10)
