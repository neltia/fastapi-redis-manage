from fastapi import APIRouter, HTTPException
from app.infrastructure.common.response_result import ResponseResult
from app.session import redis_session_service

# APIRouter 인스턴스 생성
router = APIRouter()


# Redis 세션 목록 조회 엔드포인트
@router.get("/sessions", response_model=ResponseResult)
async def get_redis_sessions():
    try:
        result = redis_session_service.get_all_sessions()
        return ResponseResult(success=True, data=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 특정 Redis 세션 조회 엔드포인트
@router.get("/sessions/{session_id}", response_model=ResponseResult)
async def get_redis_session(session_id: int):
    try:
        result = redis_session_service.get_session_by_id(session_id)
        if result is None:
            raise HTTPException(status_code=404, detail="Session not found")
        return ResponseResult(success=True, data=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Redis 세션 업데이트 엔드포인트
@router.put("/sessions/{session_id}", response_model=ResponseResult)
async def update_redis_session(session_id: int, session_name: str, host: str, port: int):
    try:
        redis_session_service.update_session(session_id, session_name, host, port)
        return ResponseResult(success=True, message="Session updated successfully")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
