"""
desciption: 정의한 패턴 규칙에 의해 다수의 레디스 키를 관리할 수 있도록 함
"""
from fastapi import APIRouter
from app.infrastructure.common.response_result import ResponseResult
from app.data.dto.pattern import Pattern
from app.data import pattern_service

# APIRouter 인스턴스 생성
router = APIRouter(prefix="")


# 패턴 정의
@router.post("", response_model=ResponseResult)
async def create_pattern(pattern_request: Pattern):
    result = pattern_service.create_pattern(pattern_request)
    return result


# 패턴 삭제
@router.delete("", response_model=ResponseResult)
async def delete_pattern(pattern_idx: int):
    result = pattern_service.delete_pattern(pattern_idx)
    return result
