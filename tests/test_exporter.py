from harborlight.exporter import TraceExporter


def test_buffer_flushes():
    exporter = TraceExporter("http://localhost:4317", batch_size=2)
    exporter.emit({"name": "a"})
    exporter.emit({"name": "b"})
    assert exporter._buffer == []
