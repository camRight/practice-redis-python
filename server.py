#!/usr/bin/env python3
import logging
import redis
from aiohttp import web
from datetime import datetime

routes = web.RouteTableDef()
r = redis.Redis(decode_responses=True, host='redis')

@routes.get('/ping')
async def ping(request):
    r.set('lastPing', datetime.utcnow().isoformat())
    print("got ping!")
    logging.info("lastPing: " + r.get("lastPing"))
    return web.Response()

app = web.Application()
app.add_routes(routes)#[ web.get('/', ping) ])

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    web.run_app(app)
