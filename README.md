# Sigmoid PU Calculator (GitHub Pages app)

This app accepts **16 columns** of pasted spreadsheet data:

- **p-d block**: `x + 7 columns`
- **d-p block**: `x + 7 columns`

It performs sigmoid fits per column (grey, room_0, room_60, room_120, room_180, room_240, room_300) and computes PU.

## Model and constraints

Sigmoid model:

\[
f(x) = \frac{1}{1 + e^{-((x-x0)/b)}}
\]

Per direction:
- p-d fit uses `b < 1`
- d-p fit uses `b > 0`

## PU formulas

Using your spreadsheet logic:
- `b(PU) = (|b(p-d)| + |b(d-p)|) / 2`
- `x0(PU) = ((x0(p-d) + x0(d-p)) / 2) - 180`

## Input UX

- Uses an Excel-like editable grid (16 columns) to prevent paste shifting.
- Paste directly from Excel/Sheets into any starting cell.
- Grid auto-adds rows if your pasted block is larger than the current size.

## Outputs

For each of the 7 channels, the app reports:
- p-d: `b`, `x0`, `R²`
- d-p: `b`, `x0`, `R²`
- PU: `b`, `x0`

## Copy-friendly output layout

Results are shown in three spreadsheet-style blocks for easy copy/paste:
- **Pre-VR Upright p-d**: rows `b(preVR)`, `x0(preVR)`, `Rsq`
- **Pre-VR Upright d-p**: rows `b(preVR)`, `x0(preVR)`, `Rsq`
- **Pre-VR Upright PU**: rows `b(preVR)`, `x0(preVR)`

Each block also includes a read-only text area with tab-separated values for one-click copy into Excel/Sheets.

## Run locally

```bash
python -m http.server 8000
```

Open `http://localhost:8000`.

## Deploy on GitHub Pages

1. Push this repo to GitHub.
2. Go to **Settings → Pages**.
3. Select **Deploy from a branch** and choose your default branch at `/ (root)`.
4. Save.
