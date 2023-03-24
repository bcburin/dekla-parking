from argparse import ArgumentParser, Namespace
from os import environ

import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from server.api import v1
from server.database.config import DBConfig

server = FastAPI(
    title='Dekla Parking API',
    version='1.0.0'
)

server.include_router(v1.router)


@server.get('/')
async def root():
    return RedirectResponse(url='/docs')


def create_parser() -> ArgumentParser:
    parser = ArgumentParser(description='Set environment variables for database configuration.')
    parser.add_argument('--dbms', help='DBMS of the database', default=DBConfig.DEFAULT_DBMS)
    parser.add_argument('--host', help='host where database is running', default=DBConfig.DEFAULT_HOST)
    parser.add_argument('--port', help='port where database is running', default=DBConfig.DEFAULT_PORT)
    parser.add_argument('--name', help='name of the database', default=DBConfig.DEFAULT_NAME)
    parser.add_argument('--password', '-p', help='password to access database', required=True)
    parser.add_argument('--user', '-u', help='user to access database', required=True)
    return parser


def update_environment_variables(args: Namespace) -> None:
    environ['DB_DBMS'] = args.dbms
    environ['DB_HOST'] = args.host
    environ['DB_PORT'] = args.port
    environ['DB_NAME'] = args.name
    environ['DB_PASSWORD'] = args.password
    environ['DB_USER'] = args.user


if __name__ == '__main__':
    # Update environment variables that configure the database
    update_environment_variables(create_parser().parse_args())
    # Run server
    uvicorn.run("main:server", host='0.0.0.0', port=8000, reload=True)
