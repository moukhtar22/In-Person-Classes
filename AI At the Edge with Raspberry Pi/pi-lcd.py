from RPLCD.i2c import CharLCD
from time import sleep

lcd = CharLCD('PCF8574', address=0x27, port=1, cols=20, rows=4)

lcd.clear()
lcd.write_string("Hello World from the Raspberry Pi")
sleep(10)
lcd.clear()