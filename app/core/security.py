from __future__ import annotations

from fastapi import Header, HTTPException, status

from .config import get_settings


async def verify_api_key(x_api_key: str | None = Header(None)) -> None:
    """Dependency to enforce X-API-Key header.

    Raises 401 if the header is missing or invalid.
    """
    settings = get_settings()
    if not x_api_key or x_api_key != settings.api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
        )
