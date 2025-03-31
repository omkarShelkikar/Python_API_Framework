from src.logger import logger  # Import the logger



def test_logging():
    logger.info("Sending POST request to login endpoint")
    logger.error("Failed test")

