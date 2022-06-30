
import socket


# make sure to set the database endpoint
dbendpoint = "";



def microhttp():
    try:
        socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket1.bind(("",80))
        socket1.listen(10)
        print("Listening for connections")
        while True:
            conn, address = socket1.accept();
            print(" + Client Connected - Sending Page!")
            newdata = conn.recv(1000)
            # ------------ basic sql connection ------------
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
            s.connect((dbendpoint, 3306))
            s.sendall("testing connection")
            sqldata = s.recv(1024)
            s.close();
            # ----------
            htmldoc = """
            <html>
                <head>
                    <title>Hello World</title>
                </head>

                <body>
                    <p>
                    <b><Tristan S> </br>
                    Week 1 - day 4</b>  </br>
                    Setup Webserver on public network and database on private </br>
                    I did not know the best way to setup support for SQL on a webserver </br>
                    so I hope this is fine using a custom server</br>
                    Raw socket connection to SQL server seen below</br>
                    </br>
                    <div style="border:solid black 1px;">
                    """ +  sqldata + """
                    </div>
                    </p>
                </body>
            </html>
            """;
            replymsg = """HTTP/2 200 OK\r\nserver: sre-training-ts\r\ncontent-type: text/html; charset="UTF-8"\r\ncontent-length: """ + str(len(htmldoc))  + """\r\n\r\n""";
            conn.send(htmldoc)
            conn.close()
    except:
        print("Server threw an error - Make sure to run as root")
        conn.close()
    return

microhttp();
