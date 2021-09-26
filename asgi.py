from app.main import get_app
from app.log_manager import log

log.info('get_app()')
app = get_app()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
