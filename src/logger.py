import logging
import os

# Get the absolute path to the log file
log_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../app.log"))

# Configure the logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file_path),  # Log to a file
        logging.StreamHandler()             # Log to the console
    ]
)

# Create a logger instance
logger = logging.getLogger("API_Framework")