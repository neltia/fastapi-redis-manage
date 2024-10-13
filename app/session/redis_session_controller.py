from fastapi import APIRouter
from app.infrastructure.common.response_result import ResponseResult
from app.session import redis_session_service

# APIRouter 인스턴스 생성
router = APIRouter()


# Redis 세션 추가 엔드포인트
@router.post("/sessions", response_model=ResponseResult)
async def create_redis_session(session_name: str, host: str, port: int):
    result = redis_session_service.create_session(session_name, host, port)
    return result


# Redis 세션 목록 조회 엔드포인트
@router.get("/sessions", response_model=ResponseResult)
async def get_redis_sessions():
    result = redis_session_service.get_all_sessions()
    return result


# 특정 Redis 세션 조회 엔드포인트
@router.get("/sessions/{session_id}", response_model=ResponseResult)
async def get_redis_session(session_id: int):
    result = redis_session_service.get_session_by_id(session_id)
    return result


# Redis 세션 업데이트 엔드포인트
@router.put("/sessions/{session_id}", response_model=ResponseResult)
async def update_redis_session(session_id: int, session_name: str, host: str, port: int):
    result = redis_session_service.update_session(session_id, session_name, host, port)
    return result
