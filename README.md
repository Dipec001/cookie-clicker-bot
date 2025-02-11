<h1>Cookie Clicker Automation Bot</h1>

Overview

This project automates the Cookie Clicker game using Selenium WebDriver. The bot continuously clicks the cookie while monitoring available upgrades and purchasing the most expensive one that the player can afford.

Features

Automated Clicking: Continuously clicks the cookie.

Upgrade Management: Checks available upgrades and buys the most expensive one within budget.

Dynamic Element Handling: Finds and interacts with page elements dynamically to avoid stale references.

Optimized Execution: Runs for a specified duration (e.g., 5 minutes) with periodic checks for upgrades.

Installation

Prerequisites

Python (3.x recommended)

Google Chrome

Chrome WebDriver (compatible with your Chrome version)

Selenium

Setup

1) Clone the Repository:
```bash
git clone https://github.com/dipec001/cookie-clicker-bot.git
cd cookie-clicker-bot
```
2) Install Dependencies:
```bash
pip install selenium
```
3) Download Chrome WebDriver:
 Download from Chrome WebDriver
 Extract and place it in the project directory.
##Usage

1) Run the bot:
```bash
python cookie_bot.py
```
2) The bot will start clicking the cookie and buying upgrades.

3) It runs for a fixed time (default: 5 minutes).

## Demo


Author

Divine (@dipec001)

License

This project is licensed under the MIT License.

