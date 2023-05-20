from argparse import ArgumentParser, Namespace
from os import environ

import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from sqlalchemy import create_engine

from server.api import v1
from server.database.config import Base, DBConfig

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
    parser.add_argument('--host', help='host where server is running', default='127.0.0.1')
    parser.add_argument('--port', help='port where server is running', default='8000')
    parser.add_argument('--db-host', help='host where database is running', default=DBConfig.DEFAULT_HOST)
    parser.add_argument('--db-port', help='port where database is running', default=DBConfig.DEFAULT_PORT)
    parser.add_argument('--db-name', help='name of the database', default=DBConfig.DEFAULT_NAME)
    parser.add_argument('--db-password', help='password to access database', required=True)
    parser.add_argument('--db-user', help='user to access database', required=True)
    parser.add_argument('--db-dbms', help='DBMS of the database', default=DBConfig.DEFAULT_DBMS)
    parser.add_argument('--dev-mode', help='starts server in development mode', action='store_true')
    return parser


def update_environment_variables(args: Namespace) -> None:
    environ['HOST'] = args.host
    environ['PORT'] = args.port
    environ['DB_DBMS'] = args.db_dbms
    environ['DB_HOST'] = args.db_host
    environ['DB_PORT'] = args.db_port
    environ['DB_NAME'] = args.db_name
    environ['DB_PASSWORD'] = args.db_password
    environ['DB_USER'] = args.db_user
    environ['DEV_MODE'] = str(args.dev_mode)


if __name__ == '__main__':
    # Get CLI arguments
    arguments = create_parser().parse_args()
    # Update environment variables that configure the server and the database connection
    update_environment_variables(arguments)
    # Create database and tables if they do not exist yet
    Base.metadata.create_all(create_engine(DBConfig().get_uri()))
    # Run server
    uvicorn.run("app:server", host=arguments.host, port=int(arguments.port), reload=arguments.dev_mode)
