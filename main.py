from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = 'localhost'
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def __get_html_content(self):
        html_file = 'index.html'
        try:
            with open(html_file, 'r', encoding='utf-8') as file:
                html_text = file.read()
                return html_text
        except FileNotFoundError:
            return 'Файл не найден'

    def do_GET(self):
        query_component = parse_qs(urlparse(self.path).query)
        print(query_component)
        page_content = self.__get_html_content()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == '__main__':
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
