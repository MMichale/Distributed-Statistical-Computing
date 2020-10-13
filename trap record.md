---
typora-copy-images-to: upload
---

# 记录一下踩过的坑

## windows和linux的编码问题

在Windows下写完脚本 通过Xftp上传到服务器 发现无法运行 或 报错

原因是win和linux对回车的编码不同

![image-20201013152955648](https://i.loli.net/2020/10/13/sARnZam9BEriNvx.png)

参考链接：https://blog.csdn.net/sz_bdqn/article/details/46499113

也可以通过VScode进行转换 将右下角的CRLF换成LF

![image-20201013153104875](https://i.loli.net/2020/10/13/wfju3ZHkPbNLzSB.png)

## \t制表符的问题

linux下制表符\t不是四个或八个空格

好像是一个整体

如果在vscode下编辑一些文本文件需要用\t分隔 可以在vscode中设置使用tab缩进 而不是空格缩进

![image-20201013153128350](https://i.loli.net/2020/10/13/QCGMlcHzAgqPL2a.png)

## Streaming命令中间不能加注释

在运行hadoop-streaming命令时 后面的一系列命令必须连起来

如果中间某个加注释了 就会报错

![image-20201013153142968](https://i.loli.net/2020/10/13/3xPMB9QWF4UGzl8.png)