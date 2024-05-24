# -*- coding: utf-8 -*-
import sys
from cx_Freeze import setup, Executable
from src.constants import version

# with open("requirements.txt", "r") as f:
#     requirements = f.read().splitlines()
#     packages = []
#     for r in requirements:
#         if "==" in r:
#             packages.append(r.split("==")[0])
#         elif "~=" in r:
#             packages.append(r.split("~=")[0])
#         elif ">=" in r:
#             packages.append(r.split(">=")[0])
#         elif "<=" in r:
#             packages.append(r.split("<=")[0])

build_exe_options = {
    "path": sys.path,
    "include_files": ['configurator.bat'],
    "packages": ["requests", "colr", "InquirerPy", "websockets", "pypresence", "nest_asyncio", "rich", "websocket_server"],
    "excludes": ["tkinter", "test", "unittest", "pygments", "xmlrpc"]
}

setup(
    name="ValoAssist",
    version=version,
    description='VAS - ValoAssist',
    executables=[Executable(
        "main.py", icon="./assets/Logo.ico", target_name="VAS.exe")],
    options={"build_exe": build_exe_options}
)
