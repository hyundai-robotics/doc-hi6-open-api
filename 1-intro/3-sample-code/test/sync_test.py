import time

def do_work_sync():
    for i in range(5):
        print(f"작업 {i} 실행 중...")
        time.sleep(1)  # 각 작업 사이에 1초 대기

def print_hello():
    print("hello")

# 동기식 실행
do_work_sync()
print_hello()