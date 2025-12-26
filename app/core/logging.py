from loguru import logger
import sys

def setup_logging():
    logger.remove()
    logger.add(sys.stdout, level="INFO")
    logger.add(
        "logs/app_{time:YYYY-MM-DD}.log",
        rotation="10 MB",
        retention="7 days"
    )
