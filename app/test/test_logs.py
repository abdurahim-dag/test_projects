import pytest

from ..src.main import logs


@pytest.mark.asyncio
async def test_print_docker_logs(capsys):
    await logs('postgres', 'name')
    catured = capsys.readouterr()
    assert catured.out ==  "name b'test1'\nname b'test2'\n"
