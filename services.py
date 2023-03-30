# Retrieves service list from ip-ranges.json to facilitate filtering CIDRs via get-regional-ranges.py

import json
import urllib.request as request

def get_service_list(url):

   response = request.urlopen(url)

   data = json.loads(response.read())

   raw_list = [
      cidr for cidr in data["prefixes"]
   ]

   service_list = []
   for item in raw_list:
      service = item['service']
      if service not in service_list:
         service_list.append(item['service'])

   sorted_list = sorted(set(service_list))

   return sorted_list