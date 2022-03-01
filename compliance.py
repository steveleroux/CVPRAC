#!/usr/bin/python3

from cvprac.cvp_client import CvpClient
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

cvp1 = "192.168.0.5"
cvp_user = "arista"
cvp_pw = "aristarsc2" # Change this to your environment password

client = CvpClient()

client.connect([cvp1], cvp_user, cvp_pw)

result = client.api.get_inventory()

# print(result)

for item in result:
    # print(item['hostname'])
    if item['complianceIndication'] == 'WARNING':
        print(item['hostname'], 'is not compliant')
    else:
        print(item['hostname'], 'is compliant')


