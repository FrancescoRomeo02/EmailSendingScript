# Email Sending Script with Attachments

A Python script to send emails with attachments using the `smtplib` and `email.message` modules.

## Description

This script allows you to send emails with attachments using a Gmail account. The user can choose between using predefined data stored in a file or manually entering the email details. The sender's account must have "less secure app" access enabled or, if two-step authentication is enabled, a specific app password must be generated.

## Prerequisites

- Python 3.x installed
- `smtplib` and `email.message` modules are included with the Python installation.

## Instructions

1. Clone or download this repository.
2. Ensure Python is installed on your system.
3. Open the terminal and navigate to the directory containing the `send_email.py` file.
4. Run the script using the command: `python send_email.py`.
5. Follow the instructions presented by the script to send the email with the attachment.

## Usage

1. Run the `send_email.py` script.
2. You will be prompted whether to use predefined data or manually input the data.
3. If you choose predefined data, ensure the `dati_predefiniti.txt` file is present in the same directory as the script. The file should contain necessary information on separate lines (sender email, password, recipient, folder path).
4. If you choose to input data manually, follow the instructions provided by the script.
5. In the end, the program will send the email with the attachments to the specified address.

## Notes

- For sending via Gmail, make sure "less secure app" access is enabled or use a specific app password if you have two-step authentication enabled.
- This script is created for demonstration and educational purposes only. Make sure to abide by the usage policies of the email service used for sending emails.

# Thinks I learned

- **File Handling**: The script deals with reading from and writing to files to store and retrieve predefined data for email sending.
- **User Input Handling**: Handling user input is crucial for customization. The script provides prompts and input fields for various data elements.
- **Authentication and Security**: Working with email APIs requires an understanding of authentication mechanisms.
- **Email Composition**: The script uses the `email.message` module to compose email messages with subjects, content, and attachments.
- **Module Integration**: Integrating modules like `smtplib` and `email.message`.
- **Code Organization**: Keeping the code organized, using functions if needed, and separating different functionalities.
- **Documentation**: Creating clear and concise documentation, such as this README file, helps users understand the purpose and usage of the script.


