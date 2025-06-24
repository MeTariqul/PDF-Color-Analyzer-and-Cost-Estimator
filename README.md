# PDF Color Analyzer & Print Cost Estimator

A FastAPI backend for printing shops that analyzes uploaded PDFs in memory, estimates printing costs based on color and B&W pages, and returns a cost summary. No files are stored on disk.

## Features
- Upload PDF files (processed in memory, not stored)
- Detects color vs. B&W pages using PyMuPDF
- Calculates printing cost dynamically
- Simple REST API

## Requirements
- Python 3.8+
- See `requirements.txt`

## Installation
```bash
pip install -r requirements.txt
```

## Running the Server
```bash
uvicorn main:app --reload
```

## API Usage
### POST /calculate-cost
Upload a PDF and get a cost estimate.

**Request:**
- `file`: PDF file (form-data)

**Example (using curl):**
```bash
curl -X POST -F "file=@test.pdf" http://localhost:8000/calculate-cost
```

**Response:**
```json
{
  "total_cost": "$12.50",
  "page_breakdown": {"color_pages": 10, "bw_pages": 5, "total_pages": 15},
  "message": "PDF processed in memory (not stored)."
}
```

## Customization
- Edit `PRICES` in `main.py` to change per-page costs.

## Notes
- For more advanced color detection, integrate Pillow or OpenCV.
- No authentication is included by default. 