zabbix监控mysql本来就已经配置好现在只有启用一下就好了

可查了一下百度，没有完整的文档，都是自己写的sh脚本，在监控mysql

现在我写一下zabbix启用默认的mysql监控的

mysql> GRANT USAGE ON *.* TO 'zabbixagent'@'localhost' IDENTIFIED BY 'Zabbix_agent1';
mysql> FLUSH PRIVILEGES;

新建.my.cnf文件，我把这个文件放到/etc/zabbix目录下
内容为
# vi /etc/zabbix/.my.cnf
[mysql]
user=zabbixagent
password=Zabbix_agent1
[mysqladmin]
user=zabbixagent
password=Zabbix_agent1
上面的配置项根据自己的情况修改配置文件

# vi /etc/zabbix/zabbix_agentd.d/userparameter_mysql

/var/zabbix
全部修改成
/etc/zabbix
目录的执行是指向到.my.cnf的文件目录

保存重启zabbix_agent

# service zabbixagent restart

在zabbix 管理机上 用zabbix-get测试一下
# yum install zabbix-get -y
# zabbix_get -s 114.215.142.27 -k mysql.ping
1

然后到web界面上使用一下Template App MySQL模板，这个模板是默认存在的
到此，mysql监控已经成功

添加mysql连接数监控
# vi /etc/zabbix/zabbix_agentd/userparameter_mysql 添加下面一行
UserParameter=mysql.connect,netstat -nalt|grep 3306|wc -l

## 报错信息
(Not all processes could be identified, non-owned process info
will not be shown, you would have to be root to see it all.)
## 原因
某些命令或参数执行需要root权限