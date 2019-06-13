### aqi-backup

> 空气质量数据库备份

### Usage

（1）编译镜像

```
docker build -t zengjing/aqi-backup:0.0.1 .
```

（2）配置执行代码

```
#!/bash
. /etc/profile
. ~/.bash_profile
cd /home/aqi-backup
docker run --rm zengjing/aqi-backup:0.0.1
```

（3）配置任务计划

```
0 9 2 * * sh /home/aqi-backup/run.sh >> /home/aqi-backup/log/log.`date +\%Y\%m\%d\%H\%M\%S` 2>&1
```