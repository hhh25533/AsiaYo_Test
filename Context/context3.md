# Context 3
## 可能原因
1. SSH Key 設定
2. 使用的 user 不對
3. EC2 資源不足
4. SSH Model 損壞

## 排查方式
```
# 檢查私鑰權限
ls -l ~/.ssh/key.pem

# 檢查 SSH 服務狀態（需要透過 AWS SSM）
sudo systemctl status sshd

# 檢查系統資源（需要透過 AWS SSM）
top
df -h

# 檢查 SSH 除錯資訊
ssh -v -i ~/.ssh/your-key.pem ec2-user@your-instance-ip
```

## 修復方式
注意：在執行前，建議先備份 Disk
1. SSH 金鑰修復
```
# 修正私鑰權限
chmod 400 ~/.ssh/key.pem

# 檢查 authorized_keys 權限
sudo chmod 600 ~/.ssh/authorized_keys
sudo chown ec2-user:ec2-user ~/.ssh/authorized_keys
```
2. SSH 服務修復
```
# 透過 AWS SSM 重啟 SSH 服務
sudo systemctl restart sshd

# 檢查 SSH 設定檔是否正確
sudo sshd -t
```
3. 系統資源問題修復
```
# 透過SSM 登入
# 清理系統log
sudo find /var/log -type f -name "*.log" -exec truncate -s 0 {} \;

# 清理暫存檔
sudo rm -rf /tmp/*
```
4. 驗證連接
