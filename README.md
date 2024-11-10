# fastapi-redis-manage
이 프로젝트는 Python FastAPI 웹 프레임워크를 사용해 In-Memory NoSQL DB인 Redis 사용을 돕는 관리 프로젝트입니다.

## 목표 기능
- Vagrant & Docker를 활용한 간편한 개발 환경 구성
- SQLite3 레디스 연결 세션 관리
    - 자주 접속하는 레디스 주소, 포트 등 정보 관리
    - 현재 접속 가능한 지 ping 확인
    - (Optional) health check 스케줄러 실행
- Redis CRUD API
    - 키 패턴을 활용한 키-값 데이터 목록 검색
    - 특정 키에 따른 데이터 생성, 갱신, 삭제
- Redis 테스트셋 데이터 생성
    - 특정 키 패턴에 해당하는 임의 데이터 생성
    - 특정 키 패턴 관련된 키-값 데이터 목록 복제

## 목차
- [개발 환경](#개발-환경)
- [환경 구성 가이드](#환경-구성-가이드)
    - [VM 설정](#vm-설정)
    - [Redis](#Redis)

## 개발 환경
- Linux Ubuntu 22.04 (선택 사항, 테스트 DB 구성용)
  - Vagrant
  - Docker
- Python 3.10

## 환경 구성 가이드
### VM 설정
1. Virtualbox install
2. vagrant install
3. vagrant up
<pre>vagrant up</pre>

### Redis
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
