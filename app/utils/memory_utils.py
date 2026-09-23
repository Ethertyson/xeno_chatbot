import os
import psutil

from app.utils.logger import logger


_process = psutil.Process(os.getpid())
_previous_rss = None


def log_memory(label: str) -> None:
    global _previous_rss

    rss = _process.memory_info().rss
    rss_mb = rss / (1024 * 1024)

    if _previous_rss is None:
        delta_mb = 0
    else:
        delta_mb = (rss - _previous_rss) / (1024 * 1024)

    logger.info(
        "[MEMORY] %s | RSS: %.2f MB | Delta: %+.2f MB",
        label,
        rss_mb,
        delta_mb,
    )

    _previous_rss = rss