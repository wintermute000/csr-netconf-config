# csr-netconf-config
NETCONF scripts to get and edit config - tested on CSR1000V IOS-XE 16.5+

SCRIPTS:
- csr-netconf-get-config.py
- csr-netconf-edit-config

USAGE - csr-netconf-get-config.py:
Uses ncclient to connect and pull raw NETCONF XML configuration using get-config operation.
Raw output saved to [hostname].config.xml - includes full NETCONF XML wrappers (<reply> etc.)

PARAMETERS - csr-netconf-get-config.py:
-n - hostname to connect to (mandatory)
-p - port to connect to (optional: defaults to 830)
-u - username to connect with (mandatory)
-w - password to connect with (mandatory)
-f - XML filter for the tag to extract (optional: defaults to "<native></native>" as per IOS-XE native YANG model

USAGE - csr-netconf-edit-config.py:
Uses ncclient to connect and edit NETCONF XML configuration using edit-config operation.
Builds proper NETCONF payload by wrapping <config></config> tag around input XML
Use parameter to input the appropriate tag that includes the appropriate input XML element - e.g. use 'native' for IOS-XE native YANG model container

PARAMETERS - csr-netconf-edit-config.py:
-n - hostname to connect to (mandatory)
-p - port to connect to (optional: defaults to 830)
-u - username to connect with (mandatory)
-w - password to connect with (mandatory)
-c - XML input file containing configuration to push (mandatory)
-t - XML filter for the tag to extract e.g. use "native" to get element for entire IOS-XE native model  (mandatory)
