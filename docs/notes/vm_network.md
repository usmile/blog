## host ssh访问虚拟机
1. 安装vmware
2. 在vmware中安装Ubuntu虚拟机
3. 在vmware的Ubuntu对应网络设置中设置“仅使用主机网络” 一般情况下，“仅使用主机网络”对应的网卡为VMnet1
4. 设置实际主机中的本地网络共享给VMnet1，在此之前需要启用VMnet1
5. 查看VMnet1的IPv4配置的网卡地址
6. 在Ubuntu虚拟机中设置
    /etc/network/interface
    auto eth0
    iface eth0 inet static 
    address 192. 168. 137. 100【注：这里的地址保持与VMnet1在同一个网段】
    gateway 192. 168. 137. 1
    netmask 255. 255. 255. 0
7. 启动网络：/etc/init. d/networking restart
8. 此时可以用SSH客户端连接到Ubuntu虚拟机了

## 虚拟机上网
在windows的网络中，设置共享网络连接给VMnet1，虚拟机就可以上网了。

