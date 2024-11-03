from redis import Redis
from app.session.redis_session_repo import SQLiteSessionRepository
from app.infrastructure.common.response_result import ResponseResult

# repo
repository = SQLiteSessionRepository()


# get redis session in SQLite Sesion Repo by session id
def get_redis_session(session_id: int):
    try:
        session = repository.get_by_id(session_id)
        return 0, session
    except Exception as e:
        return -1, str(e)


# get redis key list by key pattern with redis client
def get_redis_keys(redis_client, pattern: str):
    return redis_client.scan_iter(pattern)


# create key on
def create_key_data(session_id: int, key: str, request_data: str):
    get_status, session = get_redis_session(session_id)
    if get_status == -1:
        result = ResponseResult(result_code=500, error_msg=session)
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


# Redis Key update
def update_key_data(session_id: int, pattern: str, request_data: str):
    get_status, session = get_redis_session(session_id)
    if get_status == -1:
        result = ResponseResult(result_code=500, error_msg=session)
        return result
    if session is None:
        result = ResponseResult(result_code=404)
        return result

    redis_client = Redis(host=session.host, port=session.port)
    if "*" not in pattern:
        return update_key_one(redis_client, pattern, request_data)

    success_cnt, failed_cnt = 0, 0
    for idx, key in enumerate(get_redis_keys(pattern)):
        resp = redis_client.set(key, request_data)
        if resp:
            success_cnt += 1
        else:
            failed_cnt += 1

    data = f"total: {idx} succss: {success_cnt} failed: {failed_cnt}"
    result = ResponseResult(result_code=200, data=data)
    return result


def update_key_one(redis_client: Redis, key: str, request_data: str):
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


# Redis Key delete
def delete_keys(session_id: int, pattern: str):
    get_status, session = get_redis_session(session_id)
    if get_status == -1:
        result = ResponseResult(result_code=500, error_msg=session)
        return result
    if session is None:
        result = ResponseResult(result_code=404)
        return result

    redis_client = Redis(host=session.host, port=session.port)
    if "*" not in pattern:
        return delete_key_one(redis_client, pattern)

    success_cnt, failed_cnt = 0, 0
    for idx, key in enumerate(get_redis_keys(pattern)):
        delete_result = redis_client.delete(key)
        if delete_result == 1:
            success_cnt += 1
        else:
            failed_cnt += 1

    data = f"total: {idx} succss: {success_cnt} failed: {failed_cnt}"
    result = ResponseResult(result_code=200, data=data)
    return result


def delete_key_one(redis_client: Redis, key: str):
    get_key = redis_client.get(key)
    if not get_key:
        result = ResponseResult(result_code=404)
        return result

    resp = redis_client.delete(key)
    if resp:
        data = "Ok"
    else:
        data = "Failed"

    result = ResponseResult(result_code=200, data=data)
    return result
