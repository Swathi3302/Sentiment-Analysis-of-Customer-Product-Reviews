# Sentiment AI

A lightweight sentiment-analysis web application with a Starlette API and a responsive HTML, CSS, and JavaScript frontend. Uploaded CSV reviews are classified as positive, neutral, or negative with NLTK VADER, then summarized by product.

## Project files

- `server.py` â€” Starlette API, sentiment analysis, and static-file server
- `app.py` â€” cross-platform Python launcher
- `app.bat` â€” Windows launcher
- `static/index.html` â€” application interface
- `static/styles.css` â€” responsive styling
- `static/app.js` â€” frontend flow, API requests, and charts
- `200_reviews.csv` â€” bundled sample dataset
- `requirements.txt` â€” runtime dependencies

## Run locally

1. Install Python 3.10 or newer.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the application on Windows by double-clicking `app.bat`, or run:

   ```bash
   python app.py
   ```

4. Open <http://localhost:8000>.

## CSV format

The CSV should contain a text column whose name includes `review`, `text`, `comment`, or `feedback`. A product column is optional; names containing `product`, `item`, `name`, or `category` are detected automatically.

