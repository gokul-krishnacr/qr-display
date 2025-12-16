
---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/gokul-krishnacr/qr-display.git
cd qr-display


---

2️⃣ Create and activate virtual environment
python -m venv venv

Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Apply migrations
python manage.py migrate

5️⃣ Run the server
python manage.py runserver


Open browser:

http://127.0.0.1:8000/

