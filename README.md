# Sigmoid Batch Fitter (GitHub Pages app)

This repository includes a browser app (`index.html`) that fits your pasted 8-column table using:

\[
f(x) = \frac{1}{1 + e^{-((x-x0)/b)}}
\]
with `a = 1`.

## Modes

- **p-d**: constraint `b < 1`
- **d-p**: constraint `b > 0`

The app reports per column (2..8) versus column 1:
- `b`
- `x0`
- `R²`
- `SSE`
- `n`

## Input format

Paste tab-separated values exactly like your spreadsheet:
- 8 columns total
- first column is `x`
- next 7 columns are response columns
- blank cells are treated as missing values

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
