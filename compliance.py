#!/usr/bin/python3

from cvprac.cvp_client import CvpClient
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

cvp1 = "192.168.0.5"
cvp_user = "arista"
cvp_pw = "aristarsc2"

client = CvpClient()

client.connect([cvp1], cvp_user, cvp_pw)

result = client.api.get_inventory()

# for item in result:
#     if item['complianceIndication'] != '':
#         print(item['hostname'], 'is not compliant')


