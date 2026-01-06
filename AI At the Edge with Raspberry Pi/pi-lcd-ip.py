from RPLCD.i2c import CharLCD
from time import sleep
import os

lcd = CharLCD('PCF8574', address=0x27, port=1, cols=20, rows=4)

command = 'ip address | grep inet | grep -v inet6'
response = os.popen(command).readlines()

print(response)

lcd.clear()
row = 0
for text in response:
    line = text.split(' ')
    for value in line:
        if '/' in value:
            lcd.cursor_pos = (row, 0)
            lcd.write_string(value)
    row+=1

sleep(10)
lcd.clear()