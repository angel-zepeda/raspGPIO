import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
enable_pin = 18
coil_A_1_pin = 23 
coil_A_2_pin = 24 
coil_B_1_pin = 25 
coil_B_2_pin = 12
serv = 21
delay = 3

GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)
GPIO.setup(serv, GPIO.OUT)

GPIO.output(enable_pin, 1)
p = GPIO.PWM(serv, 50)

def forward(delay, steps): 
    for i in range(0, steps):
        setStep(1, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 1)
        time.sleep(delay)
        setStep(1, 0, 0, 1)
        time.sleep(delay)

def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)

while True:
    steps = input("Cuantas vueltas? ")
    forward(int(delay) / 1000.0, int(steps) * 520)
    time.sleep(1)
    p.start(7.5)
    p.ChangeDutyCycle(2.5) # turn towards 0 degree
    time.sleep(1) 
    p.ChangeDutyCycle(7.5) # turn towards 90 degree
    time.sleep(1) 
    p.ChangeDutyCycle(12.5) # turn towards 180 degree
    time.sleep(1) 
    p.stop()
    GPIO.cleanup()
