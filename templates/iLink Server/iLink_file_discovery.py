#!/usr/bin/env python 
import os 
import simplejson as json
t=os.popen("""netstat -nlt |grep -E "2345|22122|23000"|grep 0.0.0.0|awk '{print $4}'|awk -F: '{print $2}' """)
iLink_ports = [] 
for port in  t.readlines():
        r = os.path.basename(port.strip())
        iLink_ports += [{'{#FILE_SERVER_PORT}':r}]
print json.dumps({'data':iLink_ports},sort_keys=True,indent=4,separators=(',',':'))