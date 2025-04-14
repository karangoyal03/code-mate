Step 1: Create Python Virtual Environment

cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

cd ..
npm create vite@latest frontend --template react-ts
cd frontend
npm install