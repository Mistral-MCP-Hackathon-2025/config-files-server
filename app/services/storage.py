from __future__ import annotations

from pathlib import Path


class FileStorage:
    """Simple filesystem-based storage rooted at a base directory.

    Ensures safe path resolution and prevents directory traversal.
    """

    def __init__(self, base_dir: Path) -> None:
        self.base_dir = base_dir.resolve()

    def resolve(self, *parts: str) -> Path:
        candidate = (self.base_dir.joinpath(*parts)).resolve()
        if not str(candidate).startswith(str(self.base_dir)):
            raise PermissionError("Illegal path traversal outside base directory")
        return candidate

    def read_bytes(self, *parts: str) -> bytes:
        path = self.resolve(*parts)
        return path.read_bytes()

    def content_type_for(self, filename: str) -> str:
        lower = filename.lower()
        if lower.endswith((".yml", ".yaml")):
            return "application/yaml"
        if lower.endswith(".json"):
            return "application/json"
        if lower.endswith(".toml"):
            return "application/toml"
        if lower.endswith(".ini"):
            return "text/plain"
        return "application/octet-stream"
