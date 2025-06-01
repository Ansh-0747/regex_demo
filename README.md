
# 🧑‍💻 Regex Pattern Matching & Replacement Web App

This project is a **Django + React web application** that allows users to:
- Upload **CSV/Excel files**.
- Specify a **natural language description** to identify text patterns.
- Use **LLM (Local or API)** to convert natural language into a regex pattern.
- Replace the matched patterns in the text columns with a specified replacement.

## 🚀 Project Structure
```
regex_app/
├── api/
│   ├── migrations/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py          # Backend logic for file processing and regex conversion
│   └── urls.py
├── regex_app/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py

regex-frontend/
├── public/
├── src/
│   ├── App.js            # React frontend with upload and input fields
│   └── index.js
├── package.json
```

## 🛠️ Setup Instructions

### 🔹 Backend (Django)
1. **Install Dependencies**:
```bash
pip install -r requirements.txt
```
2. **Run Migrations**:
```bash
python manage.py migrate
```
3. **Start Server**:
```bash
python manage.py runserver
```

### 🔹 Frontend (React)
1. **Install Dependencies**:
```bash
cd regex-frontend
npm install
```
2. **Start React App**:
```bash
npm start
```

## 📥 Usage
1. Open the web app at **http://localhost:3000**.
2. Upload a **CSV/Excel file** with a text column (e.g., "Email").
3. Enter:
   - **Column Name**: Name of the column containing text.
   - **Description**: e.g., "find email addresses".
   - **Replacement**: e.g., "REDACTED".
4. Click **Upload & Process**.
5. View the processed data with replacements applied.

## 🧠 Regex Generation (LLM Integration)
- **Local GPT4All Model**:
   - Place `ggml-gpt4all-j-v1.3-groovy.bin` in `regex_app/models/`.
   - GPT4All converts descriptions into regex patterns.
- **Optional Fallback**:
   - You can hardcode common patterns (e.g., emails, phone numbers) in `views.py`.

## 📦 Requirements
- **Backend**:
   - Python 3.x
   - Django
   - djangorestframework
   - pandas
   - openpyxl
   - gpt4all (or alternative like transformers, Hugging Face API)
- **Frontend**:
   - React
   - Axios

## 🧪 Testing
- Test API directly via **Postman/cURL**:
   - `/api/regex/` – Convert description to regex.
   - `/api/upload/` – Upload file and apply replacements.
- Or use the **frontend UI** to test end-to-end.

### Example `curl` requests:
```bash
curl -X POST http://localhost:8000/api/regex/   -H "Content-Type: application/json"   -d '{"description": "find email addresses"}'

curl -X POST http://localhost:8000/api/upload/   -F "file=@test.csv"   -F "pattern=\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b"   -F "replacement=REDACTED"   -F "column=Email"
```

## 🎬 Demo
![Demo Screenshot](demo.png) <!-- Replace with your screenshot -->
<!-- Optional: Add a demo video -->
[![Watch Demo](https://img.youtube.com/vi/your-demo-video-id/0.jpg)](https://www.youtube.com/watch?v=your-demo-video-id)


## 📜 License
MIT License. Feel free to contribute and improve!

## 💡 Contributing
1. Fork the repo
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Create a new Pull Request

## 🔗 Links
- [Django](https://www.djangoproject.com/)
- [React](https://reactjs.org/)
