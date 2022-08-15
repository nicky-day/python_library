from urllib.parse import parse_qs


def application(environ, start_response):
    params = parse_qs(environ["QUERY_STRING"])
    a = params.get("a", [0])[0]
    b = params.get("b", [0])[0]
    result = int(a) * int(b)

    status = "200 OK"  # HTTP Status
    headers = [("Content-type", "text/plain; charset=utf-8")]  # HTTP Headers
    start_response(status, headers)

    return [f"Result:{result}".encode("utf-8")]


if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    with make_server("", 8888, application) as httpd:
        print("Serving on port 8888....")
        httpd.serve_forever()
