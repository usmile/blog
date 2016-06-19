## 文件读取
```bash
# 读取文件的每一行
cat filename | while read line; do  echo "===="$line; done
while read line; do echo $line; done < filename
```
