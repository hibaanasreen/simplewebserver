from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <body bgcolor="pink">
        <h1 
    align ="center"><u> Device Configuration</u></h1>
    <h2>(Hiba Nasreen)(2490018)</h2>
    <ol type="1">
      <li> Device name	LAPTOP-QSBNE8LE</li>
      <li> Processor	12th Gen Intel(R) Core(TM) i5-12450H   2.00 GHz</li>
      <li> Installed RAM	16.0 GB (15.7 GB usable)</li>
        <li> Device ID	5904DCD3-A2A8-4687-9304-53E1016ACEA9</li>
            <li> Product ID	00342-42699-61930-AAOEM</li>
                <li> System type	64-bit operating system, x64-based processor</li>
                    <li> Pen and touch	No pen or touch input is available for this display</li>
         
    </ol>

    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()