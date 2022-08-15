import xmlrpc.client

s = xmlrpc.client.ServerProxy("http://localhost:8000")
print(s.system.listMethods())

result = s.wikidocs(2)
print(result)
