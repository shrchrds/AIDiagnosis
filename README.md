# AI Medical Diagnostics Assistant

This project is an AI-powered medical diagnostics assistant that helps users analyze symptoms and receive possible diagnoses and recommendations. It consists of a FastAPI backend and a Streamlit frontend.

## Features

- **Symptom Analysis:** Detects the medical category of user-described symptoms.
- **AI Diagnosis:** Uses an AI model to suggest possible diagnoses and next steps.
- **Interactive UI:** Simple Streamlit interface for user interaction.

## Project Structure

```
AIDiagnosis/
├── langserve_backend/
│   ├── disgonostics_graph.py
│   ├── main.py
│   ├── requirements.txt
│   └── tools/
│       ├── diagnosis_tool.py
│       └── symptom_checker.py
│   └── utils/
│       ├── euri_client.py
│       └── test.py
├── streamlit_ui/
│   ├── app.py
│   └── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.10+
- [pip](https://pip.pypa.io/en/stable/)

### Installation

1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd AIDiagnosis
   ```

2. **Install backend dependencies:**
   ```sh
   cd langserve_backend
   pip install -r requirements.txt
   ```

3. **Install frontend dependencies:**
   ```sh
   cd ../streamlit_ui
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Copy `.env` files as needed and set your API keys.

### Running the Application

1. **Start the backend:**
   ```sh
   cd langserve_backend
   uvicorn main:app --reload
   ```

2. **Start the Streamlit frontend:**
   ```sh
   cd ../streamlit_ui
   streamlit run app.py
   ```

3. **Open your browser:**
   - Go to `http://localhost:8501` to use the assistant.

## License

This project is licensed under the [Apache 2.0 License](LICENSE).