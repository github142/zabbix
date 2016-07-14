#!/usr/bin/env python 
#im_server(1883,8883),im_websock(8088,8089),web_server(8083,8084),lb_server(8085,1885),erlang_epmd(4369),ham_server(8184,8183),web_manager(8096)
import os 
import simplejson as json
t=os.popen("""netstat -nlt |grep -E "1883|8883|8088|8089|8083|8084|8085|1885|4369|8184|8183|8096"|grep 0.0.0.0|awk '{print $4}'|awk -F: '{print $2}' """) 
iLink_ports = [] 
for port in  t.readlines(): 
        r = os.path.basename(port.strip()) 
        iLink_ports += [{'{#IM_SERVER_PORT}':r}] 
print json.dumps({'data':iLink_ports},sort_keys=True,indent=4,separators=(',',':'))