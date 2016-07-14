#!/usr/bin/env python 
import os 
import simplejson as json
t=os.popen("""netstat -nlt |grep -E ":6020|:5066|:3478|:5349"|grep 0.0.0.0|awk '{print $4}'|awk -F: '{print $2}'|uniq -w 2 """) 
iLink_ports = [] 
for port in  t.readlines(): 
        r = os.path.basename(port.strip()) 
        iLink_ports += [{'{#AV_SERVER_PORT}':r}] 
print json.dumps({'data':iLink_ports},sort_keys=True,indent=4,separators=(',',':'))
