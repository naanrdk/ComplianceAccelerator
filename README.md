# ComplianceAccelerator

## Description

This utility helps organizations ensure compliance with data privacy regulations (e.g., GDPR, CCPA) by automatically identifying, classifying, and anonymizing sensitive data in their databases and files.

## Features

- **Automated data discovery and classification:** Automatically identifies and classifies sensitive data based on predefined patterns.
- **Anonymization and pseudonymization techniques:** Applies hashing and masking techniques to anonymize sensitive data.
- **Compliance reporting and auditing:** Provides a report of identified sensitive data and the applied anonymization techniques.
- **Integration with data governance tools:** Designed to integrate seamlessly with existing data governance tools.
- **Real-time monitoring for compliance violations:** Monitors data for potential compliance violations in real-time (feature to be implemented).

## Prerequisites

- Python 3.7 or higher
- Flask Module
- Pandas Module

## Setup

1. Ensure you have Python 3.7 or higher installed on your system.
2. Install the required Python packages using pip:

    ```bash
    pip install Flask
    pip install pandas
    ```

## Running the Script

1. Save the script as `app.py`.
2. Run the script using the following command:

    ```bash
    python app.py
    ```

3. Use a tool like Postman or `curl` to upload a CSV file to the endpoint `/upload`.

## Usage

1. The endpoint `/upload` accepts a CSV file upload.
2. The script will classify and anonymize sensitive data in the uploaded file.
3. The response will include the classifications and a link to download the anonymized file.

### Example Request

Using `curl`:

```bash
curl -F 'file=@yourfile.csv' http://127.0.0.1:5000/upload
