#!/usr/bin/env python 
import os 
import simplejson as json
t=os.popen("""sudo netstat -nltp |grep -E "redis-server"|grep 0.0.0.0|awk '{print $4}'|awk -F: '{print $2}' """) 
redis_ports = [] 
for port in  t.readlines(): 
        r = os.path.basename(port.strip()) 
        redis_ports += [{'{#REDISPORT}':r}] 
print json.dumps({'data':redis_ports},sort_keys=True,indent=4,separators=(',',':'))