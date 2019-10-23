import time

def execute(arg01, arg02):
    start_time = time.time()
    
    print('[FUNCTION] start_time: ' + str(start_time))
    print('[FUNCTION] arg01: ' + str(arg01))
    print('[FUNCTION] arg02: ' + str(arg02))

    time.sleep(120)

    hours, rem = divmod(time.time()-start_time, 3600)
    minutes, seconds = divmod(rem, 60)
    print("[FUNCTION] elapsed_time: " + "{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))
