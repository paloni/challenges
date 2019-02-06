"""Pomodoro clock
to run: python pomodoro.py
"""

from datetime import datetime, timedelta
import time
import sys

import simpleaudio as sa


def show_passed_minutes(start_time):
    """print passed minutes from start_time

    Arguments:
        start_time {datetime} -- time when clock was started
    """

    original_delta = (datetime.now() - start_time).seconds
    if original_delta % 60 == 0:
        passed_minutes = original_delta / 60
        print(f'{passed_minutes} minute(s) passed')


def check_time(start_time, end_time):
    """return true if end_time is reached, false - otherwise

    Arguments:
        start_time {datetime}   
        end_time {datetime}

    Returns:
        [Boolean]
    """
    show_passed_minutes(start_time)

    remaining_delta = (end_time - datetime.now()).seconds
    if (remaining_delta == 0):
        return True

    return False


def get_interval(minutes):
    """adds minutes to datetime now

    Arguments:
        minutes {int}

    Returns:
        datetime
    """

    return datetime.now() + timedelta(minutes=minutes)


def run_time(type, period_end):
    """run time until it reaches period_end

    Arguments:
        type {str} -- type of clock ("Work", "Rest")
        period_end {datetime} -- when clock ends

    Returns:
        Boolean -- return true if period_end is reached, false - otherwise
    """

    print(f'{type} time has begun.')
    start_time = datetime.now()
    while True:
        time.sleep(1)
        if check_time(start_time, period_end):
            print(f'{type} time is finished')
            play_ring()
            print(f'Time now is: {datetime.now().strftime("%H:%M")}')
            print()
            break

    return True


def play_ring():
    wave_obj = sa.WaveObject.from_wave_file('./old-alarm-clock-sound.wav')
    play_obj = wave_obj.play()
    play_obj.wait_done()


def main():

    work_interval = 0
    break_interval = 0
    try:
        work_interval = int(
            input("Choose interval for work (in minutes 0-60): "))
    except ValueError:
        print('Time should be a number. The program is finished')
        sys.exit()

    try:
        break_interval = int(input("Choose interval for break (in minutes): "))
    except ValueError:
        print('Time should be a number. The program is finished')
        sys.exit()

    print(f'You set {work_interval} minutes for work')
    print(f'You set {break_interval} minutes for rest')
    print()

    while True:
        if run_time("Work", get_interval(work_interval)):
            run_time("Rest", get_interval(break_interval))


if __name__ == "__main__":
    main()
