"""
Logging configuration for the application.
"""
import logging
import sys
from app.config import get_settings

settings = get_settings()


def setup_logging():
    """
    Configure logging for the application.
    Sets up formatters, handlers, and log levels.
    """
    log_level = getattr(logging, settings.log_level.upper(), logging.INFO)
    
    # Create formatter
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    root_logger.addHandler(console_handler)
    
    # Configure specific loggers
    loggers = [
        'app',
        'uvicorn',
        'uvicorn.error',
        'uvicorn.access',
        'sqlalchemy.engine'
    ]
    
    for logger_name in loggers:
        logger = logging.getLogger(logger_name)
        logger.setLevel(log_level)
    
    # Adjust SQLAlchemy logging based on debug mode
    if not settings.debug:
        logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)
    
    logging.info("Logging configured successfully")
