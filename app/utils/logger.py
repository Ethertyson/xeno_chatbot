import logging
import os


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

LOG_DIR = os.path.join(BASE_DIR, "logs")

os.makedirs(LOG_DIR, exist_ok=True)


LOG_FORMAT = (
    "%(asctime)s | %(levelname)s | "
    "%(name)s | %(filename)s:%(lineno)d | %(message)s"
)


logger = logging.getLogger("xeno")
logger.setLevel(logging.INFO)


if not logger.handlers:

    # SERVER.log
    server_handler = logging.FileHandler(
        os.path.join(LOG_DIR, "SERVER.log"),
        encoding="utf-8",
    )

    server_handler.setLevel(logging.INFO)
    server_handler.setFormatter(
        logging.Formatter(LOG_FORMAT)
    )


    # ERROR.log
    error_handler = logging.FileHandler(
        os.path.join(LOG_DIR, "ERROR.log"),
        encoding="utf-8",
    )

    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(
        logging.Formatter(LOG_FORMAT)
    )


    logger.addHandler(server_handler)
    logger.addHandler(error_handler)

    logger.propagate = False