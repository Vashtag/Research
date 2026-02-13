# Sigmoid Batch Fitter (GitHub Pages app)

This repository includes a browser app (`index.html`) that fits your 8-column table using:

\[
f(x) = \frac{1}{1 + e^{-((x-x0)/b)}}
\]
with `a = 1`.

## Input UX (Excel-like grid)

- The app now uses an **editable 8-column grid** instead of one textbox.
- You can paste directly from Excel/Sheets into any starting cell.
- Paste preserves row/column alignment and auto-adds rows when needed.
- Column 1 is `x`; columns 2..8 are the series to fit.

## Modes

- **p-d**: constraint `b < 1`
- **d-p**: constraint `b > 0`

The app reports per column (2..8) versus column 1:
- `b`
- `x0`
- `R²`
- `SSE`
- `n`

## Run locally

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`.

## Deploy on GitHub Pages

1. Push this repo to GitHub.
2. Go to **Settings → Pages**.
3. Under **Build and deployment**, choose:
   - Source: **Deploy from a branch**
   - Branch: your default branch, folder `/ (root)`
4. Save. GitHub will publish `index.html` as your app.
