import os, platform, socket
from flask import Flask

app = Flask(__name__)


@app.get("/")
def hello():
    return f"Hello from Wadiup · Python {platform.python_version()} · Flask · {socket.gethostname()}\n"


if __name__ == "__main__":
    # Wadiup sets PORT; no Dockerfile needed (requirements.txt + main.py are detected).
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
