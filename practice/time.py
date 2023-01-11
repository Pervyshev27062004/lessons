import time
from time import sleep
from _datetime import  datetime
from random import randint
start_time = datetime.now()
print(start_time)
time.sleep(randint(1,5))
end_time = datetime.now()
print(end_time)
