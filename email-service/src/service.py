import json
from src.proxy import Proxy

proxy = Proxy()
def handleEmail(event, context):
    
    body = json.loads(event["Records"][0]["body"])
    address = body["address"]
    subject = body["subject"]
    message = body["message"]

    proxy.send(address=address, subject=subject, message=message)

    return True
