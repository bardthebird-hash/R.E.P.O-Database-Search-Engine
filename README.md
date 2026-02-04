# R.E.P.O. Search Engine 🔍

A Python-based CLI tool that functions as a custom search engine for game data (Monsters, Weapons, Items) stored in Google Sheets. It features dynamic category searching, color-coded output, and a "Game Tips" system.

## Features
- **Live Database:** Pulls data directly from Google Sheets (updates in real-time).
- **Smart Search:** Searches by Name for monsters/weapons, but switches to **Size** for items.
- **Tip Injection:** Automatically analyzes stats (like HP or Damage) and prints strategic advice.
- **Cyber-Style UI:** Uses `colorama` and `pyfiglet` for a stylish terminal interface.

## Prerequisites
You need Python 3.x installed.

## Setup Guide

### 1. Google Cloud Setup (The Hard Part)
To use this tool, you need your own Google Sheet and API credentials.
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project and enable the **Google Sheets API** and **Google Drive API**.
3. Create a **Service Account** and download the JSON key.
4. Rename the key file to `credentials.json` and place it in this project folder.
5. **Important:** Open the JSON file, copy the `client_email`, and "Share" your Google Sheet with that email address (Editor or Viewer access).

### 2. Sheet Configuration
This tool expects a Google Sheet with tabs named:
- `Monsters` (Columns: Name, HP, Damage, etc.)
- `Weapons` (Columns: Name, Damage, etc.)
- `Items` (Columns: Name, Size, Effect, etc.)

*Open `main.py` and replace the `SHEET_ID` variable with the ID from your own Google Sheet URL.*

### 3. Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Run the engine
python main.py
