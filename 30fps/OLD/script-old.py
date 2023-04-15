import time
import random
import utils
import Engine
# - create your variables HERE
engine = Engine.initEngine()
# - END -

def start():
    print("STARTING...")
    pass

def loop():
    delay = random.uniform(0,0.5)
    # utils.log(f"sleping for {delay} seconds")
    time.sleep(delay)

    # print(f"LOOPING...")
    pass

def stop():
    print("STOPPING...")
    pass