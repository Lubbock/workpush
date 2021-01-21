# workpush

钉钉md推送，包含功能
- markdown 解析，日志提取
- markdown转pdf
- pdf转图片，需要进行文字识别精确裁剪
- 钉钉推送
- markdown 日期选择
- crontab -e 定时推送 

定时推送使用crontab -e 自行实现

```sh
8 18 * * * /usr/bin/python3 /home/lame/dingtalk_rf.py
```

# 依赖的库

- python3
- requests
- pandoc
- pillow
- wand


# 常规工作清单推荐 样式

20210119

| 工作内容                | 备注 |
| ----------------------- | ---- |
| [ x ]密钥查询接口       | 完成 |
| [ x ]申请单密码机组过滤 | 完成 |
| [ x ]第二个服务无法打开 | 完成 |
| [ x]密码应用ak修改      | 完成 |

20210120

| 工作内容           | 备注 |
| ------------------ | ---- |
| 租户管理员添加租户 |      |

程序目前会检索时间，推送工作日志。
md会被转成pdf ,由于经过了dingtalk运转，还需要一个外网服务才能直接看到图片

# I HOPE
- 目前图片托管到gitee dingding不认识，需要增加外接图床
- pdf转图片，需要进行文字识别精确裁剪,用opencv 可以弄
- 代码结构拆分
    - 日志
    - 配置文件分离
    - venv
    - 图像精确区分裁剪
