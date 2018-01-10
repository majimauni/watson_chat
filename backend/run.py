from src import create_app
from flask_cors import CORS

app = create_app()
CORS(app)

app.run(host='0.0.0.0', port=8080)
