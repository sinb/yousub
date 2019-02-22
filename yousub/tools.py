import time
def seconds_to_srt_time(seconds):
    time_str = time.strftime("%H:%M:%S,", time.gmtime(int(float(seconds))))
    seconds_split = seconds.split(".")
    if len(seconds_split) == 2:
        time_str += seconds_split[-1].zfill(3)
    else:
        time_str += "000"
    return time_str