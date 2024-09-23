from pydantic import BaseModel


# Redis 세션 도메인 모델
class RedisSession(BaseModel):
    id: int
    session_name: str
    host: str
    port: int

    def can_connect(self) -> bool:
        """
        Redis 세션이 유효한지 확인하는 메서드
        """
        # 여기에 Redis 서버 연결 테스트 로직을 추가할 수 있음.
        return True

    def update_session(self, session_name: str, host: str, port: int):
        """
        세션 정보를 업데이트하는 도메인 로직
        """
        self.session_name = session_name
        self.host = host
        self.port = port
