from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import re


class OverrideHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        self.wfile.write(bytes("{ you did it }", 'utf-8'))

    def do_POST(self):
        # get request body
        request_body = int(self.headers.get('Content-length'))
        # decode request body
        post_body = self.rfile.read(request_body).decode("utf-8")
        # determine if request body is the correct pattern
        pattern = re.compile(r"^\\{ \"coin\": 1 \\}$")
        correct_input = re.search(pattern, post_body)
        # if input is incorrect, send back as a bad command
        print(correct_input.string)
        # if(pattern.match(request_body)):
        #    print("picking up on the 1 with 12. Needs refining")

        # .index is the way to go for checking validity
        if post_body.index("coin") and post_body.index("1"):
            print("the body has a coin")

        print(post_body)

        print(len(post_body))
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes("{ you did it }", "utf-8"))
