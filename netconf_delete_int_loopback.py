# NETCONF: DELETE LOOPBACK INTERFACE


# CREATE XML DELETE TEMPLATE FOR IETF-INTERFACE
netconf_interface_template = """
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface operation="delete">
            <name>{name}</name>
        </interface>
    </interfaces>
</config>"""


# RUN THE SCRIPT
# python netconf_delete_int_loopback.py