
# LockBox: Secure File Sharing Application

LockBox is a Django-based web application designed for secure file sharing with end-to-end encryption. It provides a user-friendly interface for uploading, storing, and sharing files while ensuring data privacy and security.

## Features

- User Authentication: Secure login and registration system.
- End-to-End Encryption: Files are encrypted on the client-side before upload and decrypted after download.
- File Management: Upload, download, and manage your encrypted files.
- Event Tracking: Logs user actions for auditing purposes.
- Responsive Design: Works on desktop and mobile devices.

## Technologies Used

- Backend:
  - Python 3.8+
  - Django 3.2
  - SQLite (default database, can be configured to use others)
- Frontend:
  - HTML5
  - CSS3
  - JavaScript (ES6+)
- Encryption:
  - Web Crypto API (client-side)
  - cryptography library (server-side)