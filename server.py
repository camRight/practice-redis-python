#!/usr/bin/env python3
import redis
from aiohttp import web
from datetime import datetime

routes = web.RouteTableDef()
r = redis.Redis(decode_responses=True)

@routes.get('/ping')
async def ping(request):
    r.set('lastPing', datetime.utcnow().isoformat())
    print("got ping!")
    return web.Response()

app = web.Application()
app.add_routes(routes)#[ web.get('/', ping) ])

if __name__ == '__main__':
    web.run_app(app)
