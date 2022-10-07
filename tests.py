

clocks = {
    1:'12:20',
    2:'1222:20',
    3:'a:12',
    4:'12:q',
    5:'01:12',
    6:'24:01',
    7:'12:61',
    8:'12:111111',
    9:'12;00',
    10:'-12:00',
    11:'00:-1',
    12:'srs',
    13:'00000',
    14:'00:00'
    }

def check_success_time(data:list):
    for number,test in data.items():
        try:
            if ':' in test:
                time = test.split(':')
                if 0<=int(time[0])<=23 and 0<=int(time[1])<=59:
                    print(f'!!!!!!!!{time[0]}:{time[1]}!!!!!')
                else: raise
            else: raise
        except:
            print(f'''Test №{number} not passed!!!!!''')


# check_success_time(clocks)

# import datetime
# time = datetime.datetime.utcnow().strftime("%D....%H:%M")
# print(time)
# dt = datetime.datetime.now()
# print("Datetime object =", dt)
# # printing in dd/mm/YY H:M:S format using strftime()
# dt_string = dt.strftime("Date: %d/%m/%Y  time: %H:%M:%S")
# print("Current date and time =", dt_string)


import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    sec = 0
    while True:
        sec+=1
        print(f'{sec} seconds')
        time.sleep(2)
        if sec == 5:
            logging.info("Thread %s: finishing", name)
            break

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    x = threading.Thread(target=thread_function, args=(1,))


    threads = list()
    for index in range(1):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)