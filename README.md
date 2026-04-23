# Complaint Analysis System

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)

A comprehensive NLP-powered web application for analyzing, classifying, and managing customer complaints. The system leverages machine learning and natural language processing to automatically categorize complaints, detect sentiment, and extract key insights from customer feedback.

## 🎯 Features

- **User Authentication**: Secure login and registration system
- **Complaint Classification**: Automatic categorization using TF-IDF and Logistic Regression
- **Sentiment Analysis**: Real-time sentiment detection (positive, negative, neutral)
- **Keyword Extraction**: Automatic identification of important terms
- **Priority Detection**: Smart prioritization of complaints
- **Dashboard Analytics**: Visual analytics and complaint metrics
- **Database Management**: Persistent data storage with SQLite
- **Responsive UI**: Modern and user-friendly interface

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Database](#database)
- [API Endpoints](#api-endpoints)
- [Troubleshooting](#troubleshooting)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## 🔧 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.11 or higher
- pip (Python package manager)
- Git

## 📁 Project Structure

```
complaint_analysis_system/
├── app.py                 # Main Flask application
├── model.py              # ML model training and prediction
├── database.py           # Database operations
├── utils.py              # Utility functions
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
├── dataset/
│   └── complaints.csv    # Training dataset
├── static/
│   ├── script.js         # Frontend JavaScript
│   └── style.css         # Frontend styles
├── templates/
│   ├── login.html        # Login page
│   ├── register.html     # Registration page
│   ├── complaints.html   # Complaints list page
│   ├── submit_complaint.html  # Complaint submission form
│   └── dashboard.html    # Analytics dashboard
└── model.pkl             # Trained ML model (generated)
```

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/complaint-analysis-system.git
cd complaint-analysis-system
```

### 2. Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download Required NLP Models

```bash
python -m spacy download en_core_web_sm
```

### 5. Train the ML Model

```bash
python model.py
```

This command will:
- Read the training data from `dataset/complaints.csv`
- Train the TF-IDF vectorizer and Logistic Regression model
- Save `model.pkl` and `vectorizer.pkl` for predictions

## 🚀 Usage

### Running the Application

```bash
python app.py
```

The application will start on `http://127.0.0.1:5000`

### Access the Application

Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

### Features Walkthrough

1. **Register**: Create a new user account
2. **Login**: Sign in with your credentials
3. **Submit Complaint**: Fill out the complaint form with details
4. **View Complaints**: See all submitted complaints with analysis
5. **Dashboard**: View analytics and sentiment trends

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root directory (optional):

```env
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///complaints.db
```

### Application Settings

- **Debug Mode**: Enabled by default (disable for production)
- **Database**: SQLite (configurable in `database.py`)
- **ML Model**: Trained on complaint categories

## 🗄️ Database

The application uses SQLite for data persistence. The database is automatically created on first run.

### Database Schema

- **users**: User authentication data
- **complaints**: Submitted complaints with metadata
- **analysis**: ML analysis results

Initialize or reset the database:

```python
python -c "from database import init_db; init_db()"
```

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home page |
| GET | `/register` | Registration page |
| POST | `/register` | Create new user |
| GET | `/login` | Login page |
| POST | `/login` | User authentication |
| GET | `/dashboard` | View analytics |
| GET | `/complaints` | List all complaints |
| POST | `/submit` | Submit new complaint |
| GET | `/logout` | User logout |

## 🔍 Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'numpy._core'`

**Solution**: Regenerate the model files
```bash
python model.py
```

### Issue: Flask app won't start

**Solution**: Check if port 5000 is available or specify a different port:
```bash
python -c "app.run(port=5001)"
```

### Issue: Database locked error

**Solution**: Delete the database file and restart:
```bash
rm complaints.db
python app.py
```

## 🌐 Deployment

### Deploy on Render

1. Push your code to GitHub
2. Create a new Web Service on [Render](https://render.com)
3. Configure the following:

**Build Command:**
```bash
pip install -r requirements.txt && python -m spacy download en_core_web_sm
```

**Start Command:**
```bash
gunicorn app:app
```

4. Add environment variables in Render dashboard
5. Deploy!

### Deploy on Heroku

```bash
heroku create your-app-name
git push heroku main
heroku open
```

### Deploy on AWS

1. Use AWS Elastic Beanstalk
2. Follow AWS EB deployment guide for Python Flask apps

## 📊 Model Information

- **Vectorizer**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Classifier**: Logistic Regression
- **NLP Library**: spaCy 3.7.2, NLTK, TextBlob
- **Training Data**: `dataset/complaints.csv`

## 📝 Requirements

All dependencies are listed in `requirements.txt`:

- Flask==3.0.0
- scikit-learn==1.4.0
- pandas==2.2.0
- numpy==1.26.0
- spacy==3.7.2
- nltk==3.8.1
- textblob==0.17.1

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Support

For issues, questions, or suggestions, please open an [issue](https://github.com/yourusername/complaint-analysis-system/issues) on GitHub.

## 🙏 Acknowledgments

- Flask documentation
- scikit-learn community
- spaCy NLP library
- All contributors and users
