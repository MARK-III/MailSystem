# /bin/bash
for pid in $(ps aux|grep mailserver.py | awk '{print $2}')
do
sudo kill -9 $pid
done
sudo nohup python mailserver.py &

