# Django Restframework Streaming Response

---

>Please execute following command in sequence for seamless configuration

### Activate virtual environment

````shell
virtualenv -p python3 /home/myproject/venv
source venv/bin/activate
````

### Application dependencies
```shell
pip install -r requirements.txt
```

### Application setup

```shell
./manage.py migrate

To run the project using the asgi application

python -m gunicorn DrfStreaming.asgi:application -k uvicorn.workers.UvicornWorker

run in shell in order to generate results in shell

curl -X GET  http://127.0.0.1:8000/generate-stream
```

