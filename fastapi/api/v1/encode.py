from urllib.parse import quote

from fastapi import APIRouter


router = APIRouter()


@router.get('')
async def encode_url(url: str) -> dict:
    return {"original_url": url, "encoded_url": quote(url, safe='')}
