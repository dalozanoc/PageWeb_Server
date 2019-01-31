import pyfirmata
import urllib2
from threading import Timer
import time
import random

from pyfirmata import Arduino, util
board = Arduino('COM2')

it = util.Iterator (board)
it.start ()

A0 = board.get_pin('a:0:i')
A1 = board.get_pin('a:1:i')
val=A0.read()
val1=A1.read()
print val

def send_sensor(val,val1):
        response = urllib2.urlopen('http://127.0.0.1:8080/?sensor1='+str(val)+'&sensor2='+str(val1))
        #html = response.read()
        #print html

 
def _timer():
        
        val=(A0.read())*100
        val1=(A1.read())*498.8
        #print val
        print "Valor_del_Potenciometro", '=', (val)
        print "Valor_del_LM35_Centigrados", '=', (val1)
        

        send_sensor(val,val1)
        Timer(1, _timer, ()).start()
Timer(1, _timer, ()).start()
