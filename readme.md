Project Name: Python-Console-Bank
A Modular Banking Logic Implementation
What is this?
This is a Python-based banking backend designed to handle account creation, credential validation, and real-time transactions. The project focuses on efficient data retrieval and secure state management within a console environment.

Features Implemented
Account Creation: Validates 8-digit account numbers and 4-digit passwords before storage.

Authentication Logic: Uses a "Safety Net" (NoneType checking) to prevent crashes during user login.

Transaction Management: Supports Deposits, Withdrawals (with insufficient balance checks), and Balance inquiries.

Session Persistence: Implements a while True loop to allow multiple transactions without restarting the program.