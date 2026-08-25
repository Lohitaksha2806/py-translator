# py-translator
py-translator is a lightweight Python desktop GUI application for text translation using Tkinter and the Google Translate API.

# Language Translator using Python

A desktop GUI application built in Python that translates text across various languages using the Google Translate API.

---

## Overview

This project provides a lightweight graphical interface to translate text between different languages. It automatically detects the source language if not specified and outputs the translated text in a popup message box.

---

## Features

* **GUI Interface:** Built using `tkinter` with clean input fields and action buttons.
* **Automatic Language Detection:** Detects the input language automatically when left blank.
* **Custom Destination Language:** Supports translation into any targeted language code or name supported by the API.
* **Input Validation & Error Alerts:** Uses `tkinter.messagebox` to notify users of missing input or network/API failures.
* **Reset Functionality:** Quick clear button to wipe all entry fields.

---

## Tech Stack & Dependencies

* **Python 3.x**
* **tkinter** (Standard GUI Library)
* **googletrans** (Google Translate API wrapper)

---

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/](https://github.com/)<your-username>/<repo-name>.git
   cd <repo-name>
