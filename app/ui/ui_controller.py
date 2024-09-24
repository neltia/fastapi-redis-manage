from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

# 템플릿 디렉터리 설정
templates = Jinja2Templates(directory="app/ui/templates")


# HTML 파일 렌더링
@router.get("/")
async def render_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
