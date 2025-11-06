# Insurance-prediction-API

# Insurance Category Prediction API

This project is a **FastAPI-based machine learning API** that predicts **insurance premium categories** based on user input data.
It uses a trained model built with `scikit-learn` and can run both locally and in a **Docker container**.

---

## Features

* Fast and lightweight API using **FastAPI**
* Integrated ML model for prediction
* **Dockerized** for easy deployment
* Interactive Swagger UI for testing

---

## Project Structure

```
insurance-category-prediction-api/
│
├── app.py                     # Main FastAPI app
├── model/
│   ├── model_fastapi.pkl      # Trained model
│   └── predict.py             # Prediction logic
│
├── schema/
│   ├── user_input.py          # Input schema
│   └── prediction_response.py # Output schema
│
├── requirements.txt           # Dependencies
└── Dockerfile                 # Docker configuration
```

---

## Run Locally (Without Docker)

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/insurance-category-prediction-api.git
   cd insurance-category-prediction-api
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate   # for Windows
   # or
   source venv/bin/activate   # for Linux/macOS
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the API:

   ```bash
   uvicorn app:app --reload
   ```

5. Open in browser:

   ```
   http://127.0.0.1:8000/docs
   ```

---

## Run with Docker

1. Build the image:

   ```bash
   docker build -t saharshdock/insurance-premium-api .
   ```

2. Run the container:

   ```bash
   docker run -p 8000:8000 saharshdock/insurance-premium-api
   ```

3. Open in browser:

   ```
   http://localhost:8000/docs
   ```

---

## API Endpoint

| Method | Endpoint   | Description                                      |
| :----- | :--------- | :----------------------------------------------- |
| POST   | `/predict` | Returns the predicted insurance premium category |

**Example Input:**

```json
{
  "age": 35,
  "bmi": 28.5,
  "region": "southwest",
  "smoker": "no"
}
```

**Example Output:**

```json
{
  "predicted_category": "Medium Risk"
}
```

---

## Built With

* Python 3.11
* FastAPI
* Uvicorn
* scikit-learn
* Docker
