from redis import Redis
from app.session.redis_session_repo import SQLiteSessionRepository
from app.infrastructure.common.response_result import ResponseResult

# repo
repository = SQLiteSessionRepository()


def search_keys(session_id: int, pattern: str):
    try:
        session = repository.get_by_id(session_id)
    except Exception as e:
        result = ResponseResult(result_code=500, error_msg=str(e))
        return result

    if session is None:
        result = ResponseResult(result_code=404)

    redis_client = Redis(host=session.host, port=session.port)
    keys = redis_client.keys(pattern)
    result = ResponseResult(result_code=200, data=keys)
    return result
