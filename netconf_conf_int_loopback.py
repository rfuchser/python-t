# NETCONF: CONFIGURE LOOPBACK INTERFACE


# CREATE XML CONFIG TEMPLATE FOR IETF-INTERFACE
netconf_interface_template = """
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>{name}</name>
            <description>{desc}</description>
            <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
                {type}
            </type>
            <enabled>{status}</enabled>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                <address>
                    <ip>{ip_address}</ip>
                    <netmask>{mask}</netmask>
                </address>
            </ipv4>
        </interface>
    </interfaces>
</config>"""


# ASK FOR NEW INTERFACE DETAILS
new_loopback = {}
new_loopback["name"] = "Loopback" + input("What loopback number to add? ")
new_loopback["desc"] = input("What description to use? ")
new_loopback["type"] = IETF_INTERFACE_TYPES["loopback"]
new_loopback["status"] = "true"
new_loopback["ip_address"] = input("What IP address? ")
new_loopback["mask"] = input("What network mask? ")


# CREATE NETCONF DATA FOR THE INTERFACE
netconf_data = netconf_interface_template.format(
        name = new_loopback["name"],
        desc = new_loopback["desc"],
        type = new_loopback["type"],
        status = new_loopback["status"],
        ip_address = new_loopback["ip_address"],
        mask = new_loopback["mask"]

# ADD CONFIG TO THE RUNNING CONFIG
netconf_reply = m.edit_config(netconf_data, target = 'running')


# RUN THE SCRIPT
# python netconf_conf_int_loopback.py