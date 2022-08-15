import socket

HOST = "localhost"
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        n = input("1-9 사이의 숫자를 입력하세요(0은 게임 포기):")
        if not n.strip():
            print("입력 값이 잘못되었습니다.")
            continue
        s.sendall(n.encode("utf-8"))
        data = s.recv(1024).decode("uft-8")
        print(f"서버 응답 : {data}")
        if data == "정답" or data == "종료":
            break
