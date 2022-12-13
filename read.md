create virtual env:
python -m venv venv

activate venv:
Set-ExecutionPolicy Unrestricted -Scope Process
venv\Scripts\activate

dependencies for scraper:
pip3 install httpx selectolax