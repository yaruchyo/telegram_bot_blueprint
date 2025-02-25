# Telegram Bot with Gemini Integration and with deployment on vercel

To obtain the necessary credentials:

*   **Gemini API Key:**  Visit [https://aistudio.google.com/](https://aistudio.google.com/) to generate your Gemini API key.
*   **Telegram Bot Token:** Use [BotFather](https://t.me/BotFather) on Telegram to create your bot and obtain its token.

## Description

This project implements a Telegram bot that integrates with the Gemini language model to generate responses to user input. It uses FastAPI to handle Telegram webhook requests. The bot is designed to be configurable for both development and production environments, utilizing environment variables for sensitive information like API keys and tokens.

## Features

*   **Telegram Integration:** Handles Telegram bot updates via webhook.
*   **Gemini LLM:** Integrates with the Gemini language model to generate text-based responses.
*   **Environment-Based Configuration:** Uses `.env` files and environment variables for configuration.
*   **Basic Command Handling:** Implements a `/start` command and handles text input from users.
*   **Inline Keyboard Support:** Uses inline keyboards for user interaction.
*   **Modular Design:** Separates concerns into different modules (e.g., `telegram_package`, `system_layer`, `entrypoint_layer`).
*   **MongoDB Integration:** Includes a MongoDB connector that can be used for database interactions. Currently, this functionality is commented out but can be easily enabled.
*   **Authentication Decorator:** Includes an `authenticator` decorator to wrap bot handlers.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/yaruchyo/telegram_bot_blueprint.git
    cd telegram_bot_blueprint
    ```

2.  **Set up the environment:**

    *   Copy `.env_example` to `.env` and fill in the required environment variables, such as Telegram tokens and the Gemini API key.

        ```bash
        cp .env_example .env
        ```

    *   **Important:**  Make sure to populate `.env` with your actual Telegram bot token and Gemini API key.

3.  **Create a virtual environment (Recommended):**

    You can create a virtual environment using either `venv` (Python's built-in virtual environment module) or `conda`.

    *   **Using `venv` (Python 3.11):**

        ```bash
        python3.11 -m venv venv
        source venv/bin/activate  # On Linux/macOS
        venv\Scripts\activate  # On Windows
        ```

    *   **Using `conda`:**

        ```bash
        conda create --name telegramBotBlueprint python=3.11
        conda activate telegramBotBlueprint
        ```

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    If you chose to use `conda`, ensure the `conda activate telegramBotBlueprint` environment is activated before running the `pip install` command.

## Running the Bot

1.  **Start the application:**

    ```bash
    python run.py
    ```

    Alternatively, using `uvicorn` directly:

    ```bash
    uvicorn run:app --host 0.0.0.0 --port 80 --reload
    ```

    *Note:* The `--reload` flag is useful during development as it automatically restarts the server when code changes are detected.  Remove it for production.

## Configuration

The bot's configuration is managed through environment variables. The following variables are used:

*   `ENV`: Specifies the environment (`development` or `production`).  Defaults to `development` if not set.
*   `TELEGRAM_TOKEN`: Telegram bot token for production.
*   `TELEGRAM_TOKEN_TEST`: Telegram bot token for development.
*   `GEMINI_API_KEY`: API key for the Gemini language model.
*   `MONGO_DB_USER` (optional): MongoDB username.
*   `MONGO_DB_PASS` (optional): MongoDB password.
*   `MONGO_DB_REST_URL` (optional): MongoDB connection string.
*   `MONGO_DB_NAME` (optional): MongoDB database name.

Configuration is handled in `telegram_package/config.py`.  The `ProductionConfig` and `DevelopmentConfig` classes inherit from a base `Config` class and load environment variables using `os.getenv`.

## Using the MongoDB Connector

The project includes a MongoDB connector, located in `telegram_package/system_layer/database_repository/mongo_db.py`. To enable it:

1.  Uncomment the relevant lines in `telegram_package/__init__.py`.
2.  Uncomment the relevant lines in `telegram_package/config.py`.
3.  Provide the necessary MongoDB connection details ( `MONGO_DB_USER`, `MONGO_DB_PASS`, `MONGO_DB_REST_URL`, `MONGO_DB_NAME`) in your `.env` file.

The `MongoDB` class provides methods for common database operations such as inserting, finding, updating, and deleting documents.

## Authentication Decorator

The `telegram_package/repository_layer/decorator.py` file includes an `authenticator` decorator. This decorator can be used to wrap Telegram bot handlers for authentication or other pre-processing tasks.

*   **Functionality:** The `authenticator` decorator wraps a handler function. It creates a `ReplyMethod` object, then executes the handler function with the update, context, and reply_method parameters.  It's designed to be a placeholder for your own authentication logic.

*   **Usage:** To use the `authenticator` decorator, simply apply it to a handler function:

    ```python
    from telegram_package.repository_layer.decorator import authenticator

    @authenticator
    async def my_handler(update: Update, context: ContextTypes.DEFAULT_TYPE, reply_method: ReplyMethod):
        # Your handler logic here
        await reply_method.reply_to_message("Authenticated response")
    ```

## Webhook Setup (Serverless on Vercel)

This bot is designed to be used with Telegram webhooks. You'll need to configure the webhook URL in your Telegram bot settings to point to the `/webhook` endpoint of your application (e.g., `https://your-app-url/webhook`). The `run.py` file handles the `/webhook` endpoint.

To set the webhook, use the following command, replacing `<TELEGRAM TOKEN>` with your bot's token and `<VERCEL URL>` with the URL of your deployed application:

```bash
curl -X GET "https://api.telegram.org/bot<TELEGRAM TOKEN>/setWebhook?url=<VERCEL URL>/webhook"
```

to delete the Telegram webhook: 
```bash
curl -X GET "https://api.telegram.org/<TELEGRAM TOKEN>/deleteWebhook?drop_pending_updates=True"
```

##Notes
*   The MongoDB integration is currently commented out. Follow the instructions above to enable it.
*   The `authenticator` decorator provides a framework for adding authentication to your bot handlers. You'll need to implement your own authentication logic within the decorator.
*   The `vercel.json` file is included for deploying the application to Vercel.
*   Error handling and more advanced features (e.g., conversation management, database interactions) can be added to the bot to enhance its functionality.