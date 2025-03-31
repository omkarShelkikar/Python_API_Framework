import os
from dotenv import load_dotenv
import pytest
import requests

# Load environment variables from the .env file in the src folder
env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path=env_path)

# Access environment variables
BASE_URL = os.getenv("BASE_URL")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

# Print for debugging (optional)
if __name__ == "__main__":
    print(f"BASE_URL: {BASE_URL}")
    print(f"ACCESS_TOKEN: {ACCESS_TOKEN[:10]}...")  # Print only part of the token for security

