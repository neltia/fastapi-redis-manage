# fastapi-redis-manage
redis manage service

## Test/Dev RDB Setting
### VM Setting
1. virtualbox install
2. vagrant install
3. vagrant up
<pre>vagrant up</pre>

### Redis Setting
- redis install
<pre>
sudo docker pull redis:alpine
sudo docker run -d -p 6379:6379 --name docker_redis redis:alpine
</pre>

- redis info check
<pre>
vagrant@ubuntu:~/code$ sudo docker exec -it docker_redis /bin/sh
/data # redis-cli
127.0.0.1:6379> info
# Server
redis_version:7.4.1
</pre>
