from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

# 템플릿 디렉터리 설정
templates = Jinja2Templates(directory="app/ui/templates")


# index
@router.get("/")
async def page_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# sqlite session 관리
@router.get("/session")
async def page_session_manage(request: Request):
    return templates.TemplateResponse("session/list.html", {"request": request})
