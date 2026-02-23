# Pokemon Python backend

This repository contains the code for a Python backend using FastAPI framework with a MariaDB database for accessing Pokemon information. 
It serves as one part of the whole in the CI/CD pipeline for accessing Pokemon data.

## Overview

The backend is designed to handle read operations for Pokemon information. It utilizes FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Features

- RESTful API endpoints for accessing Pokemon data
- Integration with MariaDB database for persistent storage
- Easy-to-use interface for developers to interact with the API

## Requirements

- Python 3.7+
- FastAPI
- MariaDB

## Installation

1. Clone this repository:

```bash
git clone https://github.com/donovicv/devops_python.git
```

## Running
1. Run the application:

```bash
uvicorn src.main:app --host=0.0.0.0 --port=80
```
