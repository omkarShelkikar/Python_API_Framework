import pytest
import requests
import allure
from src.utils import BASE_URL, ACCESS_TOKEN
from src.logger import logger


@allure.feature("Authentication")
@allure.story("Login API")
@allure.severity(allure.severity_level.CRITICAL)
def test_login():
    """
    Test the Login API to authenticate and retrieve an access token.
    """
    global ACCESS_TOKEN
    url = f"{BASE_URL}/auth/login"
    payload = {
        "email": "bloddy_marry@example.com",
        "password": "Password123!"
    }

    logger.info("Sending POST request to login endpoint")
    with allure.step("Send POST request to login endpoint"):
        response = requests.post(url, json=payload)

    logger.info(f"Response status code: {response.status_code}")
    with allure.step("Validate response status code"):
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    logger.info("Extracting access token from response")
    with allure.step("Extract and store the access token"):
        data = response.json()
        ACCESS_TOKEN = data.get("token")
        allure.attach(ACCESS_TOKEN, name="Access Token", attachment_type=allure.attachment_type.TEXT)
        assert ACCESS_TOKEN, "Access token not found in the response"
    logger.info("Access token successfully retrieved")


@allure.feature("Status")
@allure.story("Get API Status")
@allure.severity(allure.severity_level.NORMAL)
def test_get_status():
    """
    Test the GET-Status API to validate the service status.
    """
    url = f"{BASE_URL}/status"

    logger.info("Sending GET request to status endpoint")
    with allure.step("Send GET request to status endpoint"):
        response = requests.get(url)

    logger.info(f"Response status code: {response.status_code}")
    with allure.step("Validate response status code"):
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    logger.info("Validating response contains 'OPERATIONAL'")
    with allure.step("Validate response contains 'OPERATIONAL'"):
        assert "OPERATIONAL" in response.text, "Response does not contain 'OPERATIONAL'"
    logger.info("Status API validation successful")


@allure.feature("Authentication")
@allure.story("Register API")
@allure.severity(allure.severity_level.NORMAL)
def test_register_request():
    """
    Test the Register API to create a new user.
    """
    url = f"{BASE_URL}/auth/register"
    payload = {
        "name": "Bloody Marry2",
        "email": "bloddy_marry2@example.com",
        "password": "Password123!"
    }

    logger.info("Sending POST request to register endpoint")
    response = requests.post(url, json=payload)

    logger.info(f"Response status code: {response.status_code}")
    if response.status_code == 201:
        logger.info("User successfully registered")
        data = response.json()
        assert "user" in data, "Response does not contain 'user'"
    else:
        logger.warning("User registration failed")
        assert response.status_code == 400, f"Expected status code 400, got {response.status_code}"


@allure.feature("Goals")
@allure.story("Get All Goals")
@allure.severity(allure.severity_level.NORMAL)
def test_get_all_goals():
    """
    Test the GetAllGoals API to retrieve all goals.
    """
    url = f"{BASE_URL}/goals"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

    logger.info("Sending GET request to goals endpoint")
    with allure.step("Send GET request to goals endpoint"):
        response = requests.get(url, headers=headers)

    logger.info(f"Response status code: {response.status_code}")
    with allure.step("Validate response status code"):
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    logger.info("Validating all goals have a title")
    with allure.step("Validate all goals have a title"):
        data = response.json()
        for goal in data.get("goals", []):
            assert "title" in goal, "Goal does not contain 'title'"
    logger.info("All goals validated successfully")


@allure.feature("Goals")
@allure.story("Post Goal")
@allure.severity(allure.severity_level.CRITICAL)
def test_post_goal():
    """
    Test the Post Goal API to create a new goal.
    """
    url = f"{BASE_URL}/goals"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    payload = {
        "title": "New Goal Title",
        "description": "This is a new goal description.",
        "priority": "low",
        "status": "to-do"
    }

    logger.info("Sending POST request to create a new goal")
    response = requests.post(url, json=payload, headers=headers)

    logger.info(f"Response status code: {response.status_code}")
    assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"

    logger.info("Validating response contains required fields")
    data = response.json()
    assert "goal" in data, "Response does not contain 'goal'"
    logger.info("Goal created successfully")


@allure.feature("Goals")
@allure.story("Get Single Goal")
@allure.severity(allure.severity_level.NORMAL)
def test_get_single_goal():
    """
    Test the GET_SingleGoals API to retrieve a specific goal by ID.
    """
    goal_id = "67e76b4186d5b4933c143b7e"  # Replace with a valid goal ID
    url = f"{BASE_URL}/goals/{goal_id}"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

    logger.info(f"Sending GET request to retrieve goal with ID: {goal_id}")
    response = requests.get(url, headers=headers)

    logger.info(f"Response status code: {response.status_code}")
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    logger.info("Validating goal contains required fields")
    data = response.json()
    goal = data.get("goal", {})
    required_fields = ["_id", "title", "description", "status", "priority", "createdBy", "createdAt"]
    for field in required_fields:
        assert field in goal, f"Goal does not contain '{field}'"
    logger.info("Goal validation successful")


@allure.feature("Goals")
@allure.story("Update Goal")
@allure.severity(allure.severity_level.CRITICAL)
def test_update_goal():
    """
    Test the Update_goal API to update an existing goal.
    """
    goal_id = "67e76b4186d5b4933c143b7e"  # Replace with a valid goal ID
    url = f"{BASE_URL}/goals/{goal_id}"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    payload = {
        "title": "Updated Goal Title",
        "description": "Updated description.",
        "status": "cancelled",
        "priority": "medium"
    }

    logger.info(f"Sending PATCH request to update goal with ID: {goal_id}")
    response = requests.patch(url, json=payload, headers=headers)

    logger.info(f"Response status code: {response.status_code}")
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    logger.info("Goal updated successfully")


@allure.feature("Goals")
@allure.story("Show Progress")
@allure.severity(allure.severity_level.NORMAL)
def test_show_progress():
    """
    Test the show_progress API to retrieve progress information.
    """
    url = f"{BASE_URL}/goals/showprogress"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

    logger.info("Sending GET request to show progress endpoint")
    response = requests.get(url, headers=headers)

    logger.info(f"Response status code: {response.status_code}")
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    logger.info("Progress information retrieved successfully")