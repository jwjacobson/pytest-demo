from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.api_route("/", methods=["GET", "POST"], response_class=HTMLResponse)
async def index(
    request: Request,
    name: str = Form(None),
    email: str = Form(None),
):
    """
    Load index.html. If the user submits info, return a confirmation.
    """
    if request.method == "GET":
        return templates.TemplateResponse(request, "index.html")
    
    elif request.method == "POST":
    
        
        return HTMLResponse(f"""
                            <h1>Thank you, {name}!</h1>
                            <p>We received your info and will contact you at {email}.</p>
                            <p><a href='/'>Go back</a></p>
                            """)