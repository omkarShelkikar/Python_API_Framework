# Python API Framework

This project is a Python-based API framework designed to streamline the development and testing of APIs.

## Features

- Modular and scalable architecture.
- Built-in support for common HTTP methods (GET, POST, PUT, DELETE).
- Easy integration with third-party libraries.
- Comprehensive error handling and logging.

## Project Structure

```
Python_API_framework/
├── src/                # Source code for the framework
├── tests/              # Unit and integration tests
├── docs/               # Documentation
├── requirements.txt    # Python dependencies
├── tox.ini             # Tox configuration file
└── README.md           # Project overview
```

## Getting Started

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-repo/Python_API_framework.git
    cd Python_API_framework
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the framework**:
    ```bash
    python src/main.py
    ```

4. **Run tests and linting with tox**:
    ```bash
    tox
    ```

## Allure Reporting

This project uses **Allure** for generating detailed test reports.

### Generate and View Allure Reports

1. Run tests using `tox` or `pytest` with the `--alluredir` option:
    ```bash
    tox
    ```
    or
    ```bash
    pytest --alluredir=allure-results
    ```

2. Generate and serve the Allure report:
    ```bash
    allure serve allure-results
    ```

    This will generate the report and open it in your default web browser.

3. Alternatively, generate the report without serving it:
    ```bash
    allure generate allure-results -o allure-report --clean
    ```

4. Open the generated report manually:
    - Navigate to the `allure-report` directory.
    - Open the `index.html` file in your browser.

### Example Allure Report Features
- **Test Results**: View passed, failed, and skipped tests.
- **Test Steps**: Detailed breakdown of each test step.
- **Attachments**: Screenshots, logs, or other artifacts attached to test cases.
- **Statistics**: Summary of test execution metrics.

## Contributing

Contributions are welcome! Please follow the [contribution guidelines](docs/CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### **Changes Made**
1. **Added `tox` Instructions**:
   - Explained how to run `tox` for testing, linting, and cleaning.
   - Included commands for running specific environments.
2. **Updated Project Structure**:
   - Added [tox.ini](http://_vscodecontentref_/5) to the project structure.
3. **Included Allure Reporting**:
   - Added instructions for generating Allure reports.

---

### **Steps to Push the Updated [README.md](http://_vscodecontentref_/6)**
1. **Stage the File**:
   ```bash
   git add README.md