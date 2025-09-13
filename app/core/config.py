from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Final

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    api_key: str
    base_dir: Path
    configs_dir: Path


def get_settings() -> Settings:
    # Load .env from project root if present
    load_dotenv(override=False)

    api_key = os.getenv("API_KEY", "change-me")
    if api_key == "change-me":
        print("WARNING: Using default API key. This is insecure and should be changed in production.")

    base_dir: Final[Path] = Path(__file__).resolve().parents[2]
    configs_dir = base_dir / "configs"
    return Settings(api_key=api_key, base_dir=base_dir, configs_dir=configs_dir)
