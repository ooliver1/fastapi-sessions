from distutils.core import setup, find_packages

setup(
    name="fastapi_sessions",
    packages=find_packages(include="fastapi_sessions*"),
    version="0.1",
    license="MIT",
    description="Ready-to-use session cookies with custom backends for FastAPI",
    long_description=open("readme.md").read(),
    author="Jordan Isaacs",
    url="https://github.com/jordanisaacs/fastapi-sessions",
    install_requires=["fastapi", "itsdangerous", "pydantic"],
)
