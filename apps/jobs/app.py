from pkgs.core import create_server
from .container import JobContainer
from .controllers import controllers

app = create_server(JobContainer, controllers)
