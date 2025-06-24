from fastapi import FastAPI, UploadFile, File, HTTPException
import fitz  # PyMuPDF
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

# Pricing configuration (customize as needed)
PRICES = {
    "color_page": 0.50,  # $0.50 per color page
    "bw_page": 0.10,     # $0.10 per B&W page
}

app = FastAPI(title="PDF Color Analyzer & Print Cost Estimator")

def analyze_pdf_colors(pdf_bytes: bytes) -> dict:
    """Analyze PDF for color usage (CMYK/RGB/grayscale)."""
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    color_pages = 0
    bw_pages = 0
    total_pages = doc.page_count

    for page in doc:
        # Heuristic: If page has images or colored drawings, count as color
        is_color = False
        # Check images
        if page.get_images():
            is_color = True
        # Check drawings (shapes, lines, fills)
        for drawing in page.get_drawings():
            if drawing.get("color", 0) != 0:
                is_color = True
                break
        # Check text color (advanced, optional)
        text_blocks = page.get_text("dict").get("blocks", [])
        for block in text_blocks:
            if "lines" in block:
                for line in block["lines"]:
                    for span in line["spans"]:
                        if span.get("color", 0) != 0:
                            is_color = True
                            break
        if is_color:
            color_pages += 1
        else:
            bw_pages += 1
    return {"color_pages": color_pages, "bw_pages": bw_pages, "total_pages": total_pages}

@app.post("/calculate-cost")
async def calculate_cost(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDFs are supported.")
    try:
        pdf_bytes = await file.read()
        analysis = analyze_pdf_colors(pdf_bytes)
        total_cost = (
            analysis["color_pages"] * PRICES["color_page"] +
            analysis["bw_pages"] * PRICES["bw_page"]
        )
        return JSONResponse({
            "total_cost": f"${total_cost:.2f}",
            "page_breakdown": analysis,
            "message": "PDF processed in memory (not stored)."
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Mount static files after API routes
app.mount("/", StaticFiles(directory=".", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 