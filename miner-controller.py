import requests, argparse, time, uuid, hmac, json
from hashlib import sha256

ms = time.time_ns() // 1_000_000
nonce = uuid.uuid4().hex
requestid = uuid.uuid4().hex

parser = argparse.ArgumentParser()

parser.add_argument("-a", "--apikey", help = "API Key")
parser.add_argument("-s", "--apisecret", help = "API Secret")
parser.add_argument("-k", "--action", help = "Action")
parser.add_argument("-r", "--rigid", help = "Rig ID")
parser.add_argument("-o", "--orgid", help = "Org ID")

args = parser.parse_args()

apikey = args.apikey
apisecret = args.apisecret
action = args.action
rig_id = args.rigid
org_id = args.orgid
host = "https://api2.nicehash.com"
uri = "/main/api/v2/mining/rigs/status2"
url = "%s%s" % (host, uri)

payload = {"rigId": "%s" % (rig_id), "action": "%s" % (action.upper()) } 

print(ms)

message = bytearray(apikey, 'utf-8')
message += bytearray('\x00', 'utf-8')
message += bytearray(str(ms), 'utf-8')
message += bytearray('\x00', 'utf-8')
message += bytearray(nonce, 'utf-8')
message += bytearray('\x00', 'utf-8')
message += bytearray('\x00', 'utf-8')
message += bytearray(org_id, 'utf-8')
message += bytearray('\x00', 'utf-8')
message += bytearray('\x00', 'utf-8')
message += bytearray('POST', 'utf-8')
message += bytearray('\x00', 'utf-8')
message += bytearray(uri, 'utf-8')
message += bytearray('\x00', 'utf-8')
message += bytearray('', 'utf-8')

if payload:
    body_json = json.dumps(payload)
    message += bytearray('\x00', 'utf-8')
    message += bytearray(body_json, 'utf-8')

print(message)

signature = hmac.new(bytearray(apisecret, 'utf-8'), message, sha256).hexdigest()
headers = {"X-Organization-Id": "%s" % (org_id), "X-Auth": "%s:%s" % (apikey, signature),"X-Time": "%s" % (ms), "X-Nonce": "%s" % (nonce), "X-Request-Id": "%s" % (requestid), "Accept": "application/json, text/plain, /", "Content-Type": "application/json;charset=UTF-8" }
print(headers)
print(body_json)
r = requests.post(url, data=body_json, headers=headers)
print(r)
print(r.text)