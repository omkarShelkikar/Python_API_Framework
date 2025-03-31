from src.logger import logger
import requests

def get_objects():
    """
    Function to fetch objects using a GET request.
    """
    url = "https://api.restful-api.dev/objects"
    logger.info("Sending GET request to %s", url)
    response = requests.get(url)

    if response.status_code == 200:
        logger.info("GET request successful. Status code: %d", response.status_code)
        try:
            data = response.json()
            logger.info("Response JSON: %s", data)
            return data
        except ValueError:
            logger.error("Failed to parse JSON response.")
    else:
        logger.error("GET request failed. Status code: %d", response.status_code)
    return None


def post_object():
    """
    Function to create an object using a POST request.
    """
    url = "https://api.restful-api.dev/objects"
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    logger.info("Sending POST request to %s with payload: %s", url, payload)
    response = requests.post(url, json=payload)

    if response.status_code == 201:
        logger.info("POST request successful. Status code: %d", response.status_code)
        try:
            data = response.json()
            logger.info("Response JSON: %s", data)
            return data
        except ValueError:
            logger.error("Failed to parse JSON response.")
    else:
        logger.error("POST request failed. Status code: %d", response.status_code)
    return None


def main():
    """
    Main function to execute API calls.
    """
    logger.info("Starting the application...")

    # Perform a GET request
    logger.info("Performing GET request...")
    objects = get_objects()
    if objects:
        logger.info("Fetched objects: %s", objects)

    # Perform a POST request
    logger.info("Performing POST request...")
    created_object = post_object()
    if created_object:
        logger.info("Created object: %s", created_object)

    logger.info("Application execution completed.")


if __name__ == "__main__":
    main()