# Context 2
## 可能原因
1. CPU 資源不足
2. 防火牆設定不當
3. 網路配置問題
4. 系統負載過高
5. DNS 解析問題
6. 安全性群組 (Security Group) 設定

## 排查方法

1. 系統資源檢查
```bash
# CPU 使用情況
top
htop
# 記憶體使用
free -m
# 硬碟使用
df -h
# IO 狀態
iostat
```

2. 網路
```bash
# 檢查網路連接
ping <target_ip>
telnet <target_ip> <port>
nc -zv <target_ip> <port>

# 檢查路由
traceroute <target_ip>
route -n

# 檢查網路介面
ifconfig 或 ip addr

# 檢查連線狀態
netstat -tan | grep <port>
```

3. Log
```bash
# 系統日誌
tail -f /var/log/syslog
# 安全日誌
tail -f /var/log/auth.log
```

4. 防火牆檢查
```bash
# 檢查 iptables 規則
sudo iptables -L -n
# 檢查 UFW 狀態 (Ubuntu)
sudo ufw status
```

5. DNS 檢查
```bash
nslookup <domain>
dig <domain>
cat /etc/resolv.conf
```