from fastapi import FastAPI
from app.ui.ui_controller import router as ui_rouuter
from fastapi.staticfiles import StaticFiles
from app.session.redis_session_controller import router as redis_session_router
from app.search.redis_search_controller import router as redis_search_router
from app.infrastructure.common.error_handler import setup_exception_handlers

app = FastAPI()

# 예외 핸들러 설정
setup_exception_handlers(app)

# ui
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(ui_rouuter, prefix="/ui", tags=["UI"])

# Redis 라우터 설정 (prefix 및 tags 포함)
app.include_router(redis_session_router, prefix="/session", tags=["Redis Session"])
app.include_router(redis_search_router, prefix="/search", tags=["Redis Key Search"])
