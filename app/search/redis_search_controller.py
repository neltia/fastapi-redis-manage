from fastapi import APIRouter, HTTPException
from app.infrastructure.common.response_result import ResponseResult
from app.session import redis_session_service

# APIRouter 인스턴스 생성
router = APIRouter()


# Redis 세션에서 키 패턴 검색 엔드포인트
@router.get("/search", response_model=ResponseResult)
async def search_redis_keys(pattern: str, session_id: int):
    try:
        result = redis_session_service.search_keys(session_id, pattern)
        return ResponseResult(success=True, data=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
