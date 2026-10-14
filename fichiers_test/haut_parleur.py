from machine import Pin, PWM
import time

PIN_HP = 1        # fil blanc du Grove 1 = GP1 (essaie 0 si ça ne sonne pas)
FREQ = 1000       # hauteur du bip en Hz
DUREE_BIP = 100   # durée du bip en ms

hp = PWM(Pin(PIN_HP))
hp.freq(FREQ)

try:
    while True:
        hp.duty_u16(32768)          # signal carré à 50 % : le son
        time.sleep_ms(DUREE_BIP)
        hp.duty_u16(0)              # silence
        time.sleep_ms(1000 - DUREE_BIP)
except KeyboardInterrupt:
    hp.duty_u16(0)
    hp.deinit()   