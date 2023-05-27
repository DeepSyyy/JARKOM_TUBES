from socket import *

def requestHandler(filename):
    print(filename)
    response_line = "HTTP/1.1 200 OK\r\n"
    response_header = "Content-Type: text/html\r\n\r\n"
    if filename == "/":
        filename = "index.html"
    try:
        fin = open("view/" + filename, "r")
        message_body = fin.read()
        fin.close()
    except FileNotFoundError:
        response_line = "HTTP/1.1 404 Not Found\r\n"
        message_body = "<html><body><h1>Error 404: File not found</h1></body></html>"
    
    response = response_line + response_header + message_body
    return response