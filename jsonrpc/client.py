from jsonrpcclient import request, parse, Ok
import logging
import requests

response = requests.post("http://localhost:5000/", json=request("ping"))

parsed = parse(response.json())
if isinstance(parsed, Ok):
    print(parsed.result)
else:
    logging.error(parsed.message)


# curl -X POST http://localhost:5000 -d '{"jsonrpc": "2.0", "method": "ping", "id": 1}'