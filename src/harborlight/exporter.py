"""Trace export helpers for Harborlight."""

from typing import Any, Dict


class TraceExporter:
    def __init__(self, endpoint: str, batch_size: int = 64):
        self.endpoint = endpoint
        self.batch_size = batch_size
        self._buffer = []

    def emit(self, span: Dict[str, Any]) -> None:
        self._buffer.append(span)
        if len(self._buffer) >= self.batch_size:
            self.flush()

    def flush(self) -> None:
        self._buffer.clear()
