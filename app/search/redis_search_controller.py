from fastapi import APIRouter
from app.infrastructure.common.response_result import ResponseResult
from app.search import redis_search_service

# APIRouter 인스턴스 생성
router = APIRouter()


# Redis 세션에서 키 패턴 검색 엔드포인트
@router.get("/search", response_model=ResponseResult)
async def search_redis_keys(session_id: int, pattern: str, ):
    result = redis_search_service.search_keys(session_id, pattern)
    return result
