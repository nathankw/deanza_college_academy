import re

reg = re.compile(r'(cag)+')


def calc_repeat_frequency(sequence):
    sequence = sequence.lower()
    places = list(reg.finditer(sequence))
    max_times_repeated = 0
    for p in places:
        times_repeated = (p.end() - p.start())/3.0 # 3 is the length of "cag"
        if times_repeated > max_times_repeated:
            max_times_repeated = times_repeated
    return max_times_repeated

