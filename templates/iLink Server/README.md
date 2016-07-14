 yum install python-simplejson -y

添加下面两行到 userparameter.conf
UserParameter=iLink_im.discovery, python /etc/zabbix/iLink_im_discovery.py
UserParameter=iLink_file.discovery, python /etc/zabbix/iLink_file_discovery.py
UserParameter=iLink_av.discovery, python /etc/zabbix/iLink_av_discovery.py
UserParameter=iLink_apn_server.status,ps -fe|grep apn_server |grep -v grep|wc -l
UserParameter=iLink_log_server.status,ps -fe|grep log_server |grep -v grep|wc -l
UserParameter=iLink_mnesia_server.status,ps -fe |grep mnesia_server |grep -v grep |wc -l