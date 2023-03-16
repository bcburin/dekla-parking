from argparse import ArgumentParser
from os import environ

import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from server.api import v1

server = FastAPI(
    title='Dekla Parking API',
    version='1.0.0'
)

server.include_router(v1.router)


@server.get('/')
async def root():
    return RedirectResponse(url='/docs')


if __name__ == '__main__':
    # Add argument parser
    parser = ArgumentParser(description='Set environment variables for sensitive data')
    parser.add_argument('host', help='host running Dekla DB')
    parser.add_argument('password', help='password for Dekla DB')
    parser.add_argument('user', help='user for the Dekla DB')
    args = parser.parse_args()
    # Store sensitive data as environment variables
    environ['DB_HOST'] = args.host
    environ['DB_PASSWORD'] = args.password
    environ['DB_USER'] = args.user
    # Run server
    uvicorn.run("main:server", host='0.0.0.0', port=8000, reload=True)
