from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Response, status

from app.core.config import get_settings
from app.core.security import verify_api_key
from app.services.storage import FileStorage

router = APIRouter()


@router.get("/{version}/{filename}")
async def get_config_file(version: str, filename: str, _: None = Depends(verify_api_key)) -> Response:
    """Serve a config file from configs/{version}/{filename}.

    Protects against path traversal and returns 404 if not found.
    """
    settings = get_settings()
    storage = FileStorage(settings.configs_dir)
    try:
        data = storage.read_bytes(version, filename)
    except FileNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="File not found") from e
    except PermissionError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid path") from e

    media_type = storage.content_type_for(filename)
    return Response(content=data, media_type=media_type)
