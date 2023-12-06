import asyncio

async def do_work_async():
    for i in range(5):
        print(f"작업 {i} 실행 중...")
        await asyncio.sleep(1)  # 각 작업 사이에 1초 비동기 대기

def print_hello():
    print("hello")

async def main():
    task = asyncio.create_task(do_work_async())  # 비동기 작업 생성
    await asyncio.sleep(0.5)                     # 작업 시작 후 약간의 대기'
    print_hello()                                # 중간에 hello 출력
    await task                                   # 작업 완료까지 기다림

asyncio.run(main())