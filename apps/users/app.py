from pkgs.core import create_server
from .container import UserContainer
from .controllers import controllers

app = create_server(UserContainer, controllers)