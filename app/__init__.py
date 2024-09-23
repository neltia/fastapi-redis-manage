from fastapi import FastAPI
from app.session.redis_session_controller import router as redis_session_router
from app.infrastructure.common.error_handler import setup_exception_handlers

app = FastAPI()

# 예외 핸들러 설정
setup_exception_handlers(app)

# Redis 세션 라우터 설정 (prefix 및 tags 포함)
app.include_router(redis_session_router, prefix="/session", tags=["Redis Session"])
