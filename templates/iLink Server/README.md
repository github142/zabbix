 yum install python-simplejson -y

添加下面两行到 userparameter.conf
UserParameter=iLink_im.discovery, python /etc/zabbix/iLink_im_discovery.py
UserParameter=iLink_file.discovery, python /etc/zabbix/iLink_file_discovery.py