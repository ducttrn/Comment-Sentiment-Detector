# Comment Sentiment Detector
[![Build Status](https://travis-ci.com/billtrn/Comment-Sentiment-Detector.svg?branch=master)](https://travis-ci.com/billtrn/Comment-Sentiment-Detector)
[![Coverage Status](https://coveralls.io/repos/github/billtrn/Comment-Sentiment-Detector/badge.svg?branch=master)](https://coveralls.io/github/billtrn/Comment-Sentiment-Detector?branch=master)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/billtrn/Comment-Sentiment-Detector/blob/master/LICENSE)

A web application powered by Machine Learning capable of determining the sentiment of a comment.

![interface](https://github.com/billtrn/Comment-Sentiment-Detector/blob/master/img/interface.png?raw=true)

## 📚 Table of contents

- [Technical stack](#-technical-stack)
  - [Frontend](#-frontend)
  - [Backend](#-backend)
- [Features](#-features)
- [Run with Docker](#-run-with-docker)
- [Installation](#-installation)
- [Usage](#-usage)
- [Todo](#-to-do)
- [License](#-license)

## 🛠 Technical stack
### 🖍️ Frontend
- Framework: [Bootstrap](https://getbootstrap.com/)
### ⚙ Backend
- Programming language(s): [Python](https://www.python.org/)
- App framework: [Flask](http://flask.palletsprojects.com/en/1.1.x/)
- Distributed memory caching: [Memcached](https://memcached.org/)
- Data processing and Machine Learning: [sklearn](https://scikit-learn.org/), [numpy](https://numpy.org/), [pandas](https://pandas.pydata.org/)
- HTTP Load Balancing: [NGINX](https://www.nginx.com/)
- Deployment: [Docker](https://www.docker.com/), [AWS](https://aws.amazon.com/)


## 🚀 Features
- [Preprocess](main/engines/preprocess.py) a data file of natural language sentences
- [Train](main/engines/train.py) a Machine Learning model based on the processed data
- [Evaluate](main/engines/evaluate.py) natural language sentences to extract sentiments and confidence scores

## 🐳 Run with Docker
```
$ docker-compose up
```
The application can be found at http://localhost:5000/


## ⬇ Installation

#### 0. Prerequisites
Make sure you have installed these following prerequisites on your computer:
- Python 3.6 or later.
You can download different versions of Python here:
http://www.python.org/getit/
- `pip`
- `virtualenv`

#### 1. Install and activate virtual environment
```
$ virtualenv venv --python=python3.8
$ source venv/bin/activate
```

#### 2. Install requirements
```
pip install -r requirements.txt
```

### 3. Run the application:
```
$ python run.py
```

## 🤟 Usage
Comment Sentiment Detector can be used either as a web application, APIs, or scripts.
- Web application: The application can be found at http://localhost:5000/
- APIs: APIs for backend usage can be found [here](main/controllers/api). For example, send a `POST` request to `/api/v1/sentiments/predict` to evaluate sentiment of a text, example request body:
```json
{
  "text": "this is awesome!"
}
```
A JSON object with the detected sentiment and confidence score will be returned.
- Scripts: [preprocess data](main/engines/preprocess.py), [train model](main/engines/train.py)


## 📋 To-do
- Implement APIs for preprocessing data and training model
- Provide detailed API specs for backend usage
## 📄 License

[MIT](./LICENSE)
