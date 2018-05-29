#!/usr/bin/env python

# import the ncclient library and xml libraries
from ncclient import manager
import xml.dom.minidom
import argparse

# Establish connection to the device

def netconf_get_config(hostname, port, user, pw, filter):

# connect via ncclient
    netconf_connection = manager.connect(host=hostname,
                                         port=port,
                                         username=user,
                                         password=pw,
                                         hostkey_verify=False,
                                         )

# Use the <get-config> NETCONF Operation to retrieve full configuration
    config = netconf_connection.get_config("running", filter=("subtree", filter))

# Output XML Data to file and screen (pretty print)
    with open("%s.config.xml" % hostname, 'w') as f:
       f.write(config.xml)
       print('-------------------------------')
       print('XML output start (pretty print)')
       print('-------------------------------')
       print(xml.dom.minidom.parseString(config.xml).toprettyxml())
       print('-------------------------------')
       print('XML output end (pretty print)')
       print('-------------------------------')

# Close the NETCONF Connection to the device
    netconf_connection.close_session()

if __name__ == "__main__":

# Load parameters
# note: default filter for IOS-XE native model is entire configuration via </native> tag
# note: default port is 830
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--hostname', help='hostname', dest='hostname', required = True)
    parser.add_argument('-p', '--port', help='NETCONF port', dest='port', default = 830, required = False)
    parser.add_argument('-u','--user', help='NETCONF username', dest='username', required = True)
    parser.add_argument('-w','--pw', help='NETCONF password', dest='password', required = True)
    parser.add_argument('-f', '--filter', help='XML filter - default is <native> </native>', default = "<native> </native>", dest='filter', required = False)
    args = parser.parse_args()


# Call netconf get_config function
    netconf_get_config(args.hostname, args.port, args.username, args.password, args.filter)