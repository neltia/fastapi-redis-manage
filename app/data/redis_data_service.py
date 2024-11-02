from redis import Redis
from app.session.redis_session_repo import SQLiteSessionRepository
from app.infrastructure.common.response_result import ResponseResult

# repo
repository = SQLiteSessionRepository()


def create_key_data(session_id: int, key: str, request_data: str):
    try:
        session = repository.get_by_id(session_id)
    except Exception as e:
        result = ResponseResult(result_code=500, error_msg=str(e))
        return result

    if session is None:
        result = ResponseResult(result_code=404)
        return result

    redis_client = Redis(host=session.host, port=session.port)
    resp = redis_client.set(key, request_data)
    if resp:
        data = "Ok"
    else:
        data = "Failed"
    result = ResponseResult(result_code=200, data=data)
    return result


def update_key_data(session_id: int, key: str, request_data):
    try:
        session = repository.get_by_id(session_id)
    except Exception as e:
        result = ResponseResult(result_code=500, error_msg=str(e))
        return result

    if session is None:
        result = ResponseResult(result_code=404)
        return result

    redis_client = Redis(host=session.host, port=session.port)
    get_key = redis_client.get(key)
    if not get_key:
        result = ResponseResult(result_code=404)
        return result

    resp = redis_client.set(key, request_data)
    if resp:
        data = "Ok"
    else:
        data = "Failed"

    result = ResponseResult(result_code=200, data=data)
    return result


def delete_keys(session_id: int, key: str):
    try:
        session = repository.get_by_id(session_id)
    except Exception as e:
        result = ResponseResult(result_code=500, error_msg=str(e))
        return result

    if session is None:
        result = ResponseResult(result_code=404)
        return result

    redis_client = Redis(host=session.host, port=session.port)
    delete_result = redis_client.delete(key)
    if delete_result == 1:
        data = "Ok"
    else:
        data = "Failed"
    result = ResponseResult(result_code=200, data=data)
    return result
