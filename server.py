from fastapi import FastAPI, Request
import uvicorn
from fastapi.responses import HTMLResponse

app = FastAPI()
listening_to = ''
@app.get('/')
def hello_world():
    return 'hello world'

@app.post('/currently_playing')
async def change_playing(request:Request):
    global listening_to
    form =  await request.form()
    currently_playing = form.get('track')
    listening_to = currently_playing

@app.get('/currently_playing', response_class=HTMLResponse)
async def view_playing():
        return f"""
    <html>
        <head>
            <meta http-equiv="refresh" content="5" >
            <title>Currently playing</title>
        </head>
        <body>
            <h1>{listening_to}</h1>
        </body>
    </html>
    """


uvicorn.run(app)