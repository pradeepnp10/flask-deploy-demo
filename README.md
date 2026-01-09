# Flask Deploy Demo

A simple Flask application demonstrating deployment using Docker, Gunicorn, and Nginx with CI/CD integration.

## 📋 Overview

This project is a minimal Flask application designed to showcase deployment best practices with:
- **Flask** - Web framework
- **Gunicorn** - WSGI HTTP Server for production
- **Docker** - Containerization
- **Nginx** - Reverse proxy (for production deployment)
- **GitHub Actions** - CI/CD pipeline (as mentioned in the app response)
- **AWS EC2** - Cloud deployment target

## 🏗️ Project Structure

```
flask-deploy-demo/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker container configuration
├── default            # Nginx reverse proxy configuration
└── README.md          # This file
```

## 🚀 Features

- Simple Flask application with a home route
- Production-ready Gunicorn WSGI server configuration
- Docker containerization for easy deployment
- Nginx reverse proxy setup for load balancing and static file serving

## 📦 Dependencies

- `flask` - Web framework
- `gunicorn` - Production WSGI server

## 🛠️ Setup & Installation

### Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd flask-deploy-demo
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```
   
   The application will be available at `http://localhost:8000`

### Docker Deployment

1. **Build the Docker image**
   ```bash
   docker build -t flask-deploy-demo .
   ```

2. **Run the container**
   ```bash
   docker run -p 8000:8000 flask-deploy-demo
   ```
   
   The application will be available at `http://localhost:8000`

## 🌐 Production Deployment

### With Nginx Reverse Proxy

The `default` file contains the Nginx configuration for reverse proxying:

1. **Copy Nginx configuration** (on your server)
   ```bash
   sudo cp default /etc/nginx/sites-available/flask-deploy-demo
   sudo ln -s /etc/nginx/sites-available/flask-deploy-demo /etc/nginx/sites-enabled/
   ```

2. **Restart Nginx**
   ```bash
   sudo nginx -t  # Test configuration
   sudo systemctl restart nginx
   ```

3. **Run the Flask app** (using Docker or directly)
   ```bash
   docker run -d -p 8000:8000 --name flask-app flask-deploy-demo
   ```

The application will be accessible through Nginx on port 80, which will proxy requests to the Flask app on port 8000.

## 🔧 Configuration

### Gunicorn Configuration

The Dockerfile uses the following Gunicorn settings:
- `-w 2` - 2 worker processes
- `-b 0.0.0.0:8000` - Bind to all interfaces on port 8000
- `app:app` - Application module and instance

### Port Configuration

- **Flask/Gunicorn**: Port 8000
- **Nginx**: Port 80 (HTTP)

## 🚢 Deployment to AWS EC2

1. **Launch an EC2 instance** (Ubuntu recommended)

2. **Install Docker and Nginx**
   ```bash
   sudo apt update
   sudo apt install -y docker.io nginx
   sudo systemctl start docker
   sudo systemctl enable docker
   ```

3. **Clone and build the application**
   ```bash
   git clone <repository-url>
   cd flask-deploy-demo
   sudo docker build -t flask-deploy-demo .
   ```

4. **Run the container**
   ```bash
   sudo docker run -d -p 8000:8000 --name flask-app flask-deploy-demo
   ```

5. **Configure Nginx** (see Production Deployment section above)

6. **Configure Security Groups**
   - Allow inbound traffic on port 80 (HTTP)
   - Allow inbound traffic on port 22 (SSH)

## 🔄 CI/CD with GitHub Actions

Based on the application's response message, this project is set up for automated deployment using GitHub Actions to EC2. The typical workflow would:

1. Push code to the repository
2. GitHub Actions triggers the workflow
3. Builds Docker image
4. Deploys to EC2 instance
5. Updates the running container

## 📝 API Endpoints

- `GET /` - Returns a welcome message about the deployment setup

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available for educational purposes.

## 👤 Author

Flask Deploy Demo Project

---

**Note**: This is a demo project showcasing deployment best practices. For production use, consider adding:
- Environment variable management
- Database integration
- Logging configuration
- Health check endpoints
- SSL/TLS certificates (HTTPS)
- Monitoring and alerting
- Load balancing for multiple instances

