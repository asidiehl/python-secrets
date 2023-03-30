# Filters address lists by regions "GLOBAL" and "us-west-1" and by services "AMAZON" and "EC2"

import json
import ipaddress
import urllib.request as request
from .services import get_service_list
from .regions import get_region_list

url = "https://ip-ranges.amazonaws.com/ip-ranges.json"

services = get_service_list(url)
regions = get_region_list(url)

squirrel1 = "AKIAIOSFODNN7EXAMPLE"
squirrel2 = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

response = request.urlopen(url)

data = json.loads(response.read())

# TODO: Variablize region and service values in if statement
# TODO: Figure out how to prompt for regions and services to check based on values returned in `services` and `regions` vars
filtered_list = [
    dictionary for dictionary in data["prefixes"]
    if (dictionary['region'] in ("us-west-1", "GLOBAL")) and (dictionary['service'] in ("AMAZON", "EC2"))
]

list = []

for item in filtered_list:
    list.append(ipaddress.ip_network(item['ip_prefix']))

sorted_list = sorted(set(list))

for item in sorted_list:
  item = str(item)
  print(item)
