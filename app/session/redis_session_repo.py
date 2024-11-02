import os
import sqlite3
from app.session.redis_session_model import RedisSession


class SQLiteSessionRepository:
    def __init__(self, db_path: str = "db/redis_sessions.db"):
        self.db_path = db_path
        self.ensure_db_directory_exists()
        self.connection = sqlite3.connect(self.db_path)
        self.create_table()

    def ensure_db_directory_exists(self):
        # 데이터베이스 경로의 디렉터리 존재 여부 확인
        db_dir = os.path.dirname(self.db_path)
        if not os.path.exists(db_dir):
            os.makedirs(db_dir)  # 경로가 없으면 생성

    def create_table(self):
        # 테이블이 존재하지 않으면 생성
        query = """
        CREATE TABLE IF NOT EXISTS redis_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_name TEXT NOT NULL,
            host TEXT NOT NULL,
            port INTEGER NOT NULL,
            status TEXT NULL
        )
        """
        self.connection.execute(query)
        self.connection.commit()

    def add_session(self, session_name: str, host: str, port: int):
        query = """
        INSERT INTO redis_sessions (session_name, host, port)
        VALUES (?, ?, ?)
        """
        self.connection.execute(query, (session_name, host, port))
        self.connection.commit()

    def get_all(self):
        # 모든 세션 가져오기
        cursor = self.connection.cursor()
        query = "SELECT id, session_name, host, port, status FROM redis_sessions"
        cursor.execute(query)
        rows = cursor.fetchall()
        return [RedisSession(id=row[0], session_name=row[1], host=row[2], port=row[3]) for row in rows]

    def get_by_id(self, session_id: int):
        # ID로 세션 가져오기
        cursor = self.connection.cursor()
        query = "SELECT id, session_name, host, port FROM redis_sessions WHERE id = ?"
        cursor.execute(query, (session_id,))
        row = cursor.fetchone()
        if row:
            return RedisSession(id=row[0], session_name=row[1], host=row[2], port=row[3])
        return None

    def save(self, session: RedisSession):
        # 세션 정보 저장
        query = """
        UPDATE redis_sessions SET session_name = ?, host = ?, port = ?
        WHERE id = ?
        """
        self.connection.execute(query, (session.session_name, session.host, session.port, session.id))
        self.connection.commit()
