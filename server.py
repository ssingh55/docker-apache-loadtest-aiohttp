import aiohttp
import logging
from aiohttp import web

# async def handle(request):
#     return web.Response(text="Hello, world!")
async def handle_hello(request):
    logging.info(f"Received request for {request.path}")
    headers = {'Custom-Header': 'Hello-Header'}
    return web.Response(text="Hello, world!", headers=headers)

async def handle_goodebye(request):
    logging.info(f"Received request for {request.path}")
    headers = {'Custom-Header': 'Goodbye-Header'}
    return web.Response(text="Goodbye, world!",headers=headers)

async def init():
    logging.basicConfig(level=logging.INFO)
    app = web.Application()
    app.router.add_get('/', handle_hello)
    app.router.add_get('/goodbye', handle_goodebye)
    return app

if __name__ == "__main__":
    web.run_app(init(), port=8080)