### Задача
Написать пример(ы) unit тестов на эту фнкцию:
```
async def logs(cont, name):
    conn = aiohttp.UnixConnector(path="/var/run/docker.sock")
    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get(f"http://xx/containers/{cont}/logs?follow=1&stdout=1") as resp:
            async for line in resp.content:
                print(name, line)
```

### Как запустить
1. Переходим в папку test и устанавливаем зависимости: pip install -r requirements.txt
2. Переходим в папку test/app и запускае тесты: pytest

### Задача
Напишите эндпойнт, который в качестве параметра сможет принимать незакодированную (unencoded) ссылку и возвращать его закодированным 

### Как запустить
1. Перейдите в папку решения fastapi и устанавливаем зависимости: pip install -r requirements.txt
2. Запустите сервер: python -m main
3. Отправляем запросы через postman: http://localhost:8000/api/v1/encode?url=http://example.com