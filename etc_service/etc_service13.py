import time
import atexit


def handle_exit(msg):
    print(msg)


atexit.register(handle_exit, "프로그램 종료 시 반드시 호출되어야 합니다.")
while True:
    print("작업중...")
    time.sleep(1)
