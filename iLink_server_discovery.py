#!/usr/bin/env python 
import os 
import simplejson as json
t=os.popen("""netstat -nlt |grep -E "1883|8883|8088|8089|8083|8084|8085|1885|4369|8184|8183"|grep 0.0.0.0|awk '{print $4}'|awk -F: '{print $2}' """) 
iLink_ports = [] 
for port in  t.readlines(): 
        r = os.path.basename(port.strip()) 
        iLink_ports += [{'{#IM_SERVER_PORT}':r}] 
t=os.popen("""netstat -nlt |grep -E "2345|22122|23000"|grep 0.0.0.0|awk '{print $4}'|awk -F: '{print $2}' """)
for port in  t.readlines():
        r = os.path.basename(port.strip())
        iLink_ports += [{'{#FILE_SERVER_PORT}':r}]
print json.dumps({'data':iLink_ports},sort_keys=True,indent=4,separators=(',',':'))