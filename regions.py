# Retrieves region list from ip-ranges.json to facilitate filtering CIDRs via get-regional-ranges.py

import json
import urllib.request as request

def get_region_list(url):
  response = request.urlopen(url)

  data = json.loads(response.read())

  raw_list = [
    cidr for cidr in data["prefixes"]
  ]

  region_list = []
  for item in raw_list:
    region_list.append(item['region'])

  sorted_list = sorted(set(region_list))

  for region in sorted_list:
    print(region)
  return sorted_list