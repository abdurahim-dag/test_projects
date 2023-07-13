import fastapi
import uvicorn

import api
import core


settings = core.Settings()
app = fastapi.FastAPI(
    title=settings.project_name,
    default_response_class=fastapi.responses.ORJSONResponse
)

app.include_router(api.v1.encode.router, prefix='/api/v1/encode')

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
    )