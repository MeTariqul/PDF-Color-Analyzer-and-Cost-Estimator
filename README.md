# PDF Print Cost Calculator

A responsive web application to calculate printing costs for PDF files based on user-specified page types (Black & White or Color).

---

## 🚀 Features
- **Upload a PDF** and automatically count its pages
- **Specify page types**: All B&W, All Color, or custom ranges (e.g., 1–5 Color, rest B&W)
- **Instant bill calculation** with clear breakdown:
  - Total pages
  - B&W pages and cost
  - Color pages and cost
  - Grand total
- **Responsive design** (works on mobile and desktop)

---

## 🛠️ Setup Instructions

1. **Clone or copy this project** to your machine.
2. **Activate the virtual environment** (already present as `venv`):
   ```sh
   .\venv\Scripts\activate
   ```
3. **Install dependencies** (if not already):
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the app**:
   ```sh
   python app.py
   ```
5. **Open your browser** and go to:
   - [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 📖 User Manual

### 1. Upload PDF
- Click the **"Upload PDF"** button and select your PDF file.
- The app will count the total number of pages.

### 2. Specify Page Types
- Choose how to assign page types:
  - **All Black & White**: All pages are B&W (4৳ per page)
  - **All Color**: All pages are color (6৳ per page)
  - **Specify Ranges**: Add custom ranges (e.g., pages 1–3 Color, 4–10 B&W)
    - Click **"Add Range"** to add a new range
    - Set the start/end page and type (Color or B&W)
    - Remove a range with the red × button

### 3. Calculate Bill
- Click **"Calculate Bill"**
- See a detailed summary:
  - Total pages
  - B&W pages and cost
  - Color pages and cost
  - Grand total (in ৳)

---

## 💡 Notes
- Only PDF files are supported.
- Uploaded files are deleted after page counting.
- You can use this app on both desktop and mobile browsers.

---

## 📦 Deployment
- For production, use a WSGI server (e.g., Gunicorn) and configure static file serving.
- You can deploy on platforms like Heroku, PythonAnywhere, or your own server.

---

## 📝 License
This project is for educational/demo purposes. Modify and use as you wish! 