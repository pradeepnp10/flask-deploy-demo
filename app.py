from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Deployed with GitHub Actions + EC2 + Gunicorn!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
