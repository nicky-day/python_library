import http.client


def get_wikidocs(page):
    conn = http.client.HTTPSConnection("wikidocks.net")
    conn.request("GET", "/{}".format(page))
    r = conn.getresponse()
    with open("wikidocs_%s.html" % page, "wb") as f:
        f.writer(r.read())
    conn.close()


if __name__ == "__main__":
    get_wikidocs(12)
