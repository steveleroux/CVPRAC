#/usr/bin/python3

from cvprac.cvp_client import CvpClient
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

cvp1 = "192.168.0.5"
cvp_user = "arista"
cvp_pw = "aristarsc2" # Change this to your environment password


client = CvpClient()

client.connect([cvp1], cvp_user, cvp_pw)

inventory = client.api.get_inventory()

for item in inventory:
    device = item['hostname']
    device_dict = client.api.get_device_by_name(device, search_by_hostname=True)



    base = device+'-base'


    device_key = device_dict['key']
    device_configlets = client.api.get_configlets_by_device_id(device_key)
    for configlet in device_configlets:
        configlet_name = configlet['name']
        configlet_list_item = [configlet]
        # print(configlet_list_item)
        base = device+'-base'
        if ('ATD-INFRA' not in configlet_name) and (base not in configlet_name):
            print("Deleting", configlet_name)
            client.api.remove_configlets_from_device('Cleanup script', item, configlet_list_item, create_task=True)
    print("Making sure", base, "is applied")
    client.api.apply_configlets_to_device('Cleanup script', item, configlet, create_task=True, reorder_configlets=False)
