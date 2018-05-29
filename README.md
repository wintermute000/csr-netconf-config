# csr-netconf-config
NETCONF python scripts to get and edit config - tested on CSR1000V IOS-XE 16.5+  
* csr-netconf-get-config.py
* csr-netconf-edit-config

requires: ncclient

## csr-netconf-get-config.py:
### Usage
Uses ncclient to connect and pull raw NETCONF XML configuration using get-config operation.  
Raw output saved to [hostname].config.xml - includes full NETCONF XML wrappers (<reply> etc.)  
Use parameter to input the XML filter - defaults to "< native > < /native >" as per IOS-XE native YANG model

#### Input Parameters
 * -n - hostname to connect to (mandatory)
 * -p - port to connect to (optional: defaults to 830)
 * -u - username to connect with (mandatory)
 * -w - password to connect with (mandatory)
 * -f - XML filter for the tag to extract (optional: defaults to "< native > < /native >" as per IOS-XE native YANG model

## csr-netconf-edit-config.py:
### Usage
Uses ncclient to connect and edit NETCONF XML configuration using edit-config operation.  
Builds proper NETCONF payload by wrapping "config" tag around input XML  
Use parameter to input the appropriate tag that includes the appropriate input XML element - e.g. use 'native' for IOS-XE native YANG model container - do this if you only want to send a sub-section (tag) of a larger XML  configuration  

#### Input Parameters
 * -n - hostname to connect to (mandatory)
 * -p - port to connect to (optional: defaults to 830)
 * -u - username to connect with (mandatory)
 * -w - password to connect with (mandatory)
 * -c - XML input file containing configuration to push (mandatory)
 * -t - XML filter for the tag to extract e.g. use "native" to get element for entire IOS-XE native model  (mandatory)
