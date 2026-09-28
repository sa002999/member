from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def member_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="member.html",
        context={"name": "王小明", "email": "ming@example.com"},
    )
