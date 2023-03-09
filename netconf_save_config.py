# NETCONF: SAVE THE CONFIG TO THe STARTUP CONFIG

# IMPORT
from ncclient import manager, xml_


# CALLING RPC
save_body = """
<cisco-ia:save-config xmlns:cisco-ia="http://cisco.com/yang/cisco-ia"/>
"""


# SEND RPC
netconf_reply = m.dispatch(xml_.to_ele(save_body))


# PARTIAL EXAMPLE OUTPUT
<result xmlns="http://cisco.com/yang/cisco-ia">Save running-config successful</result>


# RUN THE SCRIPT
# python netconf_save_config.py