# NETCONF: GET THE INTERFACE CONFIGURATION AND STATUS


# IMPORT
import os
import sys
from ncclient import manager
import xmltodict
import xml.dom.minidom


# GET THE ABSLOUTE PATH TO THIS FILE HERE "here"
here = os.path.abspath(os.path.dirname("netconf_get_int_list.py"))


# GET THE ABSLOUTE PATH  FOR THE PROJECT / REPOSITORY ROOT
project_root = os.path.abspath(os.path.join(here, "../.."))


# EXTEND THE SYSTEM PATH TO INCLUDE PROJECT ROOT AND IMPORT THE ENV FILES
sys.path.insert(0, project_root)
import env_lab  # noqa


# CREATE A FILTER FOR FILTERING INTERFACE DATA
netconf_filter = """
<filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface></interface>
    </interfaces>
</filter>"""


# OPEN CONNECTION TO HOST
#with manager.connect(
#        host=env_lab.IOS_XE_1["host"],
#        port=env_lab.IOS_XE_1["netconf_port"],
#        username=env_lab.IOS_XE_1["username"],
#        password=env_lab.IOS_XE_1["password"],
#        hostkey_verify=False
#        ) as m:
     
with manager.connect(
        host=env_lab.IOS_XE_1["sandbox-iosxe-latest-1.cisco.com"],
        port=env_lab.IOS_XE_1["830"],
        username=env_lab.IOS_XE_1["developer"],
        password=env_lab.IOS_XE_1["pC1sco12345"],
        hostkey_verify=False
        ) as m:
       

     # GET THE HOST CONFIGURATION FILTERED
     print("Sending a <get-config> operation to the device.\n")
     netconf_reply = m.get_config(source = 'running', filter = netconf_filter)


# PRINT THE RAW XML DATA IN PRETTY FORMAT
print("Here is the raw XML data returned from the device.\n")
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
print("")


# PARSE THE XML STRING TO PYTHON DICTIONARY
netconf_data = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]




# CREATE A LIST OF INTERFACES FROM THE DICTIONARY
interfaces = netconf_data["interfaces"]["interface"]


# LOOP OVER THE INTERFACES AND PRINT THE NAME AND STATUS
print("The interface status of the device is: ")
for interface in interfaces:
    print("Interface {} enabled status is {}".format(
            interface["name"],
            interface["enabled"]
            )
        )
print("\n")


# RUN THE SCRIPT
# python netconf_get_int_list.py