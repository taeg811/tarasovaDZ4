#!/usr/bin/python
import re
from ansible.errors import (
    AnsibleFilterTypeError,
    AnsibleFilterError
)

def checkmac_filter(mac1):
    '''
        check mac in string type, count 12, 0-9, a-f, A-F
    '''
    if not isinstance(mac1, str):
        raise AnsibleFilterTypeError("String type is expected, "
                                     "got type is %s instead" % type(mac1))
    
    if len(mac1)!=12:
       raise AnsibleFilterError("Mac address length is error --> %s" % len(mac1)) 
           
    if len( re.findall(r'[0-9a-fA-F]', mac1)) != 12 :
       raise AnsibleFilterError("Symbols error, they should be in  A-F or a-f, wrong mac --> %s" % mac1)
       
    #return str( mac1[:2]+':'+mac1[2:4]+':'+mac1[4:6]+':'+mac1[6:8]+':'+mac1[8:10]+':'+mac1[10:])
    return (':'.join([ mac1[i:i+2] for i in range(0,11,2) ]))
    

class FilterModule(object):
    def filters(self):
        return {
            'checkmac_filter': checkmac_filter
                }
