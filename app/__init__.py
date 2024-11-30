from fastapi import FastAPI
from app.ui.ui_controller import router as ui_router
from fastapi.staticfiles import StaticFiles
from app.data.redis_data_controller import router as redis_data_router
from app.data.pattern_controller import router as pattern_data_router
from app.session.redis_session_controller import router as redis_session_router
from app.search.redis_search_controller import router as redis_search_router
from app.infrastructure.common.error_handler import setup_exception_handlers

app = FastAPI()

# 예외 핸들러 설정
setup_exception_handlers(app)

# ui
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(ui_router, prefix="/ui", tags=["UI"])

# Redis 라우터 설정
app.include_router(redis_session_router, prefix="/session", tags=["Redis Session"])
app.include_router(redis_data_router, prefix="/data", tags=["Redis data"])
app.include_router(pattern_data_router, prefix="/pattern", tags=["Pattern data for search"])
app.include_router(redis_search_router, prefix="/search", tags=["Redis Key Search"])
