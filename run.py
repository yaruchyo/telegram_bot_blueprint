import json
from typing import Dict, Any
from telegram import Update
from telegram_package.entrypoint_layer.bot_router import register_app
from telegram_package import create_app, application

app = create_app()


@app.post("/webhook")
async def webhook(webhook_data: Dict[Any, Any]):
    register_app(application)
    try:
        await application.initialize()
        await application.process_update(
            Update.de_json(
                json.loads(json.dumps(webhook_data, default=lambda o: o.__dict__)),
                application.bot,
            )
        )
    finally:
        await application.shutdown()

@app.get("/")
def index():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)