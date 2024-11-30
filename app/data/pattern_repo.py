import os
import sqlite3


class SQLitePatternRepository:
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
        CREATE TABLE IF NOT EXISTS data_patterns (
            idx INTEGER PRIMARY KEY AUTOINCREMENT,
            pattern VARCHAR(50) NOT NULL,
            description TEXT NULL
        )
        """
        self.connection.execute(query)
        self.connection.commit()

    def add_pattern(self, pattern: str, description: str):
        query = """
        INSERT INTO data_patterns (pattern, description)
        VALUES (?, ?)
        """
        self.connection.execute(query, (pattern, description))
        self.connection.commit()

    def get_by_id(self, pattern_id: int):
        # ID로 패턴 가져오기
        cursor = self.connection.cursor()
        query = "SELECT idx, pattern, description FROM data_patterns WHERE idx = ?"
        cursor.execute(query, (pattern_id))
        row = cursor.fetchone()
        if row:
            return {row[1]: row[2]}
        return None

    def delete_pattern(self, idx: int):
        query = "DELETE FROM data_patterns WHERE idx = ?;"
        self.connection.execute(query, (idx))
        self.connection.commit()
