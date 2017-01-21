import threading
from random import randint
from time import sleep

def print_number(number):
        rand_int_var = randint(1,10)
        sleep(rand_int_var)
        print "Thread "+str(number) + " slept for " + str(rand_int_var) + "seconds"

thread_list = []

for i in range(1,10):
        t = threading.Thread(target = print_number , args=(i,))
        thread_list.append(t)

for thread in thread_list:
        thread.start()

for thread in thread_list:
        thread.join()

print "Done"

