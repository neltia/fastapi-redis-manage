from app.session.redis_session_repo import SQLiteSessionRepository
from app.infrastructure.common.response_result import ResponseResult
import redis

# repo
repository = SQLiteSessionRepository()


def create_session(session_name: str, host: str, port: int):
    repository.add_session(session_name, host, port)
    result = ResponseResult(result_code=200, result_msg="session added")
    return result


def get_all_sessions():
    try:
        data = repository.get_all()
        result = ResponseResult(result_code=200, data=data, exclude_unset=True)
    except Exception as e:
        result = ResponseResult(result_code=500, error_msg=str(e))

    return result


def get_session_by_id(session_id: int):
    try:
        data = repository.get_by_id(session_id)
    except Exception as e:
        result = ResponseResult(result_code=500, error_msg=str(e))
        return result

    if data is None:
        result = ResponseResult(result_code=404, data=data, exclude_unset=True)
    else:
        result = ResponseResult(result_code=200, data=data, exclude_unset=True)
    return result


def get_session_by_alias(session_name: str):
    try:
        data = repository.get_by_alias(session_name)
    except Exception as e:
        result = ResponseResult(result_code=500, error_msg=str(e))
        return result

    if data is None:
        result = ResponseResult(result_code=404, data=data, exclude_unset=True)
    else:
        result = ResponseResult(result_code=200, data=data, exclude_unset=True)
    return result


def update_session(session_id: int, session_name: str, host: str, port: int):
    try:
        session = repository.get_by_id(session_id)
    except Exception as e:
        result = ResponseResult(result_code=500, error_msg=str(e))
        return result

    if not session:
        result = ResponseResult(result_code=404)
        return result

    session.update_session(session_name, host, port)
    repository.save(session)

    result = ResponseResult(result_code=200, result_msg="session updated")
    return result


# 저장된 세션 정보의 사용 가능 여부 확인
def ping_redis_session(session_id):
    # 세션 아이디 탐색
    try:
        session = repository.get_by_id(session_id)
    except Exception as e:
        result = ResponseResult(result_code=500, error_msg=str(e))
        return result

    try:
        redis_client = redis.Redis(host=session.host, port=session.port)
        response = redis_client.ping()
    except Exception as e:
        result = ResponseResult(result_code=500, error_msg=str(e))
        return result

    if response:
        result = ResponseResult(result_code=200, data=response, exclude_unset=True)
    else:
        result = ResponseResult(result_code=200, data=response, exclude_unset=True)
    return result
