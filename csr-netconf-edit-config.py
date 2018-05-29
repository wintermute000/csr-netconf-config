#!/usr/bin/env python

# import the ncclient library and xml libraries
from ncclient import manager
import xml.dom.minidom
import argparse

def netconf_create_payload(config_xml, payload_tag):
    xmldoc = xml.dom.minidom.parse(config_xml)

# Extract payload root (e.g. <native/> in IOS-XE YANG model) from raw netconf output
    native_list = xmldoc.getElementsByTagName(payload_tag)
    native = native_list[0]


# Create payload with <config/> wrapper
    payload = xml.dom.minidom.parseString("<config></config>")
    payload.childNodes[0].appendChild(native)

# Convert to string and print
    payload_text = payload.toprettyxml()
    print(payload_text)

# Return text
    return(payload_text)

def netconf_push_payload(hostname, port, user, pw, payload_text):

    # Establish connection to the device
    netconf_connection = manager.connect(host=hostname,
                        port=port,
                        username=user,
                        password=pw,
                        hostkey_verify=False,
                        )

    # Read in the standard config, and push to "running"
    push = netconf_connection.edit_config(payload_text, target="running")

    # Print out the XML Data to the screen
    print(xml.dom.minidom.parseString(push.xml).toprettyxml())

    # Close the NETCONF Connection to the device
    netconf_connection.close_session()


if __name__ == "__main__":

# Load parameters
# note: default filter for IOS-XE native YANG model is entire configuration via "native" tag
# note: default port is 830
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--hostname', help='hostname', dest='hostname', required = True)
    parser.add_argument('-p', '--port', help='NETCONF port', dest='port', default = 830, required = False)
    parser.add_argument('-u','--user', help='NETCONF username', dest='username', required = True)
    parser.add_argument('-w','--pw', help='NETCONF password', dest='password', required = True)
    parser.add_argument('-c', '--config', help='NETCONF XML configuration', dest='config_xml', required = True)
    parser.add_argument('-t', '--tag', help='XML tag containing payload e.g. for IOS-XE YANG its "native"', dest='payload_tag', required = True)
    args = parser.parse_args()

# Call netconf get_config function
    payload_text = netconf_create_payload(args.config_xml, args.payload_tag)
    netconf_push_payload(args.hostname, args.port, args.username, args.password, payload_text)