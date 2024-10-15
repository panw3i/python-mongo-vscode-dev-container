# Python MongoDB VSCode Dev Container

This repository contains a Python development environment configured for MongoDB, designed to work with Visual Studio Code's Dev Containers feature.

## Features

- Python 3.10
- MongoDB integration using `pymongo`
- Docker-based development environment
- Ready-to-use VSCode Dev Container configuration

## Prerequisites

- Docker installed on your machine
- Visual Studio Code with the Dev Containers extension

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/panw3i/python-mongo-vscode-dev-container.git
   cd python-mongo-vscode-dev-container

1. **Open in VSCode:**

   Make sure you have the VSCode Dev Containers extension installed. Open the project in VSCode and it will automatically build the development container.

   ```
   code .
   ```

2. **Run the container:**

   VSCode will prompt you to reopen the project in a container. Once inside the container, run the application:

   ```
   python main.py
   ```

   You should see the message "MongoDB connected!" if the MongoDB instance is running correctly.

## MongoDB Setup

- The container is pre-configured to connect to a local MongoDB instance.
- You can modify the connection string in `main.py` to connect to a remote MongoDB instance if needed.
