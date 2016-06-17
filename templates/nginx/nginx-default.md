1. 启用nginx status配置

在默认主机里面加上location或者你希望能访问到的主机里面。

server {
    listen  *:80 default_server;
    server_name _;
    location /ngx_status 
    {
        stub_status on;
        access_log off;
        allow 127.0.0.1;
        deny all;
    }
}

2. 重启nginx

请依照你的环境重启你的nginx

# service nginx restart
1
# service nginx restart
3. 打开status页面


# curl http://127.0.0.1/ngx_status
Active connections: 11921 
server accepts handled requests
 11989 11989 11991 
Reading: 0 Writing: 7 Waiting: 42

4. nginx status详解

active connections – 活跃的连接数量
server accepts handled requests — 总共处理了11989个连接 , 成功创建11989次握手, 总共处理了11991个请求
reading — 读取客户端的连接数.
writing — 响应数据到客户端的数量
waiting — 开启 keep-alive 的情况下,这个值等于 active – (reading+writing), 意思就是 Nginx 已经处理完正在等候下一次请求指令的驻留连接.
5. 完成

下篇文章我们将使用zabbix监控nginx
http://www.ttlsa.com/zabbix/zabbix-monitor-nginx-performance/