from fastapi import APIRouter
from app.infrastructure.common.response_result import ResponseResult
from app.data import redis_data_service

# APIRouter 인스턴스 생성
router = APIRouter()


# 단일 키 생성
@router.post("", response_model=ResponseResult)
async def create_redis_key(session_id: int, key: str, request_data: str):
    if "*" in key:
        return ResponseResult(result_code=400)

    result = redis_data_service.create_key_data(session_id, key, request_data)
    return result


# 키 데이터 갱신
@router.put("", response_model=ResponseResult)
async def update_redis_key(session_id: int, key: str, request_data: str):
    result = redis_data_service.update_key_data(session_id, key, request_data)
    return result


# 키 삭제
@router.delete("", response_model=ResponseResult)
async def delete_redis_keys(session_id: int, key: str):
    if "*" in key:
        return ResponseResult(result_code=400)

    result = redis_data_service.delete_keys(session_id, key)
    return result
