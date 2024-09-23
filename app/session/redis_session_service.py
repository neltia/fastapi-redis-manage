from app.infrastructure.sqlite.sqlite_session_repo import SQLiteSessionRepository
from redis import Redis

# 서비스 클래스
repository = SQLiteSessionRepository()


def get_all_sessions():
    return repository.get_all()


def get_session_by_id(session_id: int):
    return repository.get_by_id(session_id)


def update_session(session_id: int, session_name: str, host: str, port: int):
    session = repository.get_by_id(session_id)
    if session:
        session.update_session(session_name, host, port)
        repository.save(session)
    else:
        raise Exception("Session not found")


def search_keys(session_id: int, pattern: str):
    session = repository.get_by_id(session_id)
    if session is None:
        raise Exception("Session not found")

    redis_client = Redis(host=session.host, port=session.port)
    keys = redis_client.keys(pattern)
    return keys
