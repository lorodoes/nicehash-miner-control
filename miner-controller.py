import requests, argparse

parser = argparse.ArgumentParser()

parser.add_argument("-a", "--apikey", help = "API Key")
parser.add_argument("-s", "--apisecret", help = "API Secret")
parser.add_argument("-k", "--action", help = "Action")
parser.add_argument("-r", "--rigid", help = "Rig ID")

args = parser.parse_args()

apikey = args.apikey
apisecret = args.apisecret
action = args.action
rig_id = args.rigid
host = "https://api2.nicehash.com"
uri = "/main/api/v2/mining/rigs/status2"
url = "%s%s" % (host, uri)

payload = {"rigId": "%s", "action": "%s"} % (rig_id,action)

headers = {"X-Organization-Id": "d0d64f17-1dc5-4615-a7de-30a7a3fbbbeb", "X-Auth": "%s:%s" }% (apikey, apisecret)
r = requests.post(url, data=payload, headers=headers)
