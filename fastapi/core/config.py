import pydantic


class Settings(pydantic.BaseConfig):
    project_name: str = pydantic.Field('Encode url', env='PROJECT_NAME')
