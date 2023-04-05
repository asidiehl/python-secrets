# Filters address lists by regions "GLOBAL" and "us-west-1" and by services "AMAZON" and "EC2"

import json
import ipaddress

# TODO: Import functions from other python files in same dir
# from .services import get_service_list
# from .regions import get_region_list

ip_ranges_file = "ip-ranges.json"

# TODO: Integrate output from these commands to provide service and region selection options when running the script.
# services = get_service_list(ip_ranges_file)
# regions = get_region_list(ip_ranges_file)

squirrel1 = "AKIAIOSFODNN7EXAMPLE"
squirrel2 = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

response = open(ip_ranges_file)

# `json.load()` for `open(filename)`, `json.loads()` for the output of a `request.urlopen(url)`
data = json.load(response)

# TODO: Variablize region and service values in if statement
# TODO: Figure out how to prompt for regions and services to check based on values returned in `services` and `regions` vars
filtered_list = [
    dictionary
    for dictionary in data["prefixes"]
    if (dictionary["region"] in ("us-west-1", "GLOBAL"))
    and (dictionary["service"] in ("AMAZON", "EC2"))
]

list = []

for item in filtered_list:
    list.append(ipaddress.ip_network(item["ip_prefix"]))

sorted_list = sorted(set(list))

for item in sorted_list:
    item = str(item)
    print(item)
