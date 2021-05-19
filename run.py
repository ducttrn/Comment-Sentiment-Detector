import os

from main.app import app

# Retrieve environment configurations
_host = str(os.getenv("HOST", "0.0.0.0"))
_port = int(os.getenv("PORT", 5000))

# Execute the application given that this file is run
# as the entrance script.
if __name__ == "__main__":
    app.run(host=_host, port=_port)
