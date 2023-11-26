import pywhatkit
import keyboard
import time
from datetime import datetime

contatos = [] #contatos com "+55" antecedendo o número

#mandar a mensagem enquanto a lista de contatos estive cheia
while len(contatos) >= 1:
    #enviar a mensagem e esperar 1 minuto
    pywhatkit.sendwhatmsg(contatos[0], 'Aqui  vai a mensagem', datetime.now().hour,datetime.now().minute + 1)
    del contatos[0] #apagar o primeiro contato
    time.sleep(20) #esperar 20 segundos para enviar para o próximo contato
    keyboard.press_and_release('ctrl + w')