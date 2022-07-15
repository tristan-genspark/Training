

import socket

def GetPage():
    s = socket.socket()
    s.connect(("127.0.0.1", 8081))
    s.sendall(b"GET / HTTP/2.0\r\nHost: 127.0.0.1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0\r\nAccept: */*\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate, br\r\nConnection: keep-alive\r\n\r\n")
    returndata = s.recv(1024);
    return returndata;

try:
    html = GetPage();

    if b"Friday Lab - CI CD with Jenkins and Terraform" in html:
        print("Test Successful")
    else:
        print("Test Failed - Malformed Content")
except:
    print("Test Failed - Unable to connect")
    pass;
