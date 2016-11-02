# coding:utf-8
import asyncio
from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'Hello index')

async def hello(request):
    await asyncio.sleep(1)
    text = 'hello, %s' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)

    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('server start at 127.0.0.1:8000')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
