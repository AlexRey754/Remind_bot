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


check_success_time(clocks)

# import datetime
# time = datetime.datetime.utcnow().strftime("%D....%H:%M")
# print(time)
# dt = datetime.datetime.now()
# print("Datetime object =", dt)
# # printing in dd/mm/YY H:M:S format using strftime()
# dt_string = dt.strftime("Date: %d/%m/%Y  time: %H:%M:%S")
# print("Current date and time =", dt_string)
