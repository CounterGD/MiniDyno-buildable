from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import sqlite3, datetime, os
from jose import jwt, JWTError
from core.db import get_conn, init_db
from core.punishments import add_punishment, get_active_punishments
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
templates = Jinja2Templates(directory=TEMPLATE_DIR)
app = FastAPI()
app.mount('/static', StaticFiles(directory=os.path.join(os.path.dirname(__file__),'static')), name='static')
SECRET = os.environ.get('MINIDYNO_SECRET','supersecretkey')
init_db()
def auth_cookie(request: Request):
    token = request.cookies.get('token')
    if not token: raise HTTPException(403, 'No token')
    try:
        payload = jwt.decode(token, SECRET, algorithms=['HS256'])
        return payload
    except JWTError:
        raise HTTPException(403, 'Invalid token')
@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('dashboard.html', {'request':request, 'stats':{}})
@app.get('/punishments', response_class=HTMLResponse)
async def view_punishments(request: Request, user=Depends(auth_cookie)):
    rows = get_active_punishments()
    return templates.TemplateResponse('punishments.html', {'request':request, 'rows':rows})
@app.get('/filters', response_class=HTMLResponse)
async def filters_page(request: Request, user=Depends(auth_cookie)):
    conn = get_conn(); cur = conn.cursor()
    rows = cur.execute('SELECT id, pattern FROM bad_words').fetchall(); conn.close()
    return templates.TemplateResponse('filters.html', {'request':request, 'rows':rows})
@app.post('/filters/add')
async def add_filter(request: Request, pattern: str = Form(...)):
    conn = get_conn(); cur = conn.cursor(); cur.execute('INSERT INTO bad_words (pattern) VALUES (?)', (pattern,)); conn.commit(); conn.close()
    return RedirectResponse(url='/filters', status_code=303)
@app.post('/filters/delete/{fid}')
async def delete_filter(request: Request, fid: int):
    conn = get_conn(); cur = conn.cursor(); cur.execute('DELETE FROM bad_words WHERE id=?', (fid,)); conn.commit(); conn.close()
    return RedirectResponse(url='/filters', status_code=303)
