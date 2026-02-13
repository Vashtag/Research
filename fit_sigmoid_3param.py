"""Fit 3-parameter sigmoid with a fixed a=1 for each data column vs x.

Model: y = a/(1 + exp(-(x-x0)/b)), with a fixed to 1.
Constraint: b < 1.
"""

from __future__ import annotations

import math

X_VALUES = [
    -90, -75, -60, -45, -30, -15, 0, 15, 30, 45, 60,
    75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225,
]

DATA_COLUMNS = {
    "4-grey": [None, 1.0, 1.0, 0.75, 0.75, 1.0, 1.0, 0.875, 0.875, 0.75, 0.75, 0.375, 0.25, 0.125, 0.125, 0.125, 0.0, None, None, None, None, None],
    "5-room_0": [None, None, None, 1.0, 1.0, None, 1.0, 0.875, 1.0, 0.875, 0.875, 0.75, 0.25, 0.25, 0.375, 0.0, None, None, None, None, None, None],
    "6-room_60": [None, None, None, None, None, 1.0, 0.875, 1.0, 0.875, 1.0, 0.75, 0.75, 0.5, 0.375, 0.375, 0.25, 0.0, None, None, None, None, None],
    "7-room_120": [None, None, 1.0, 1.0, 0.875, 0.875, 0.875, 1.0, 1.0, 1.0, 0.75, 0.375, 0.25, 0.25, 0.125, 0.125, None, None, None, None, None, None],
    "8-room_180": [None, None, 1.0, 1.0, 1.0, 1.0, 1.0, 0.75, 0.625, 0.625, 0.5, 0.125, 0.25, 0.25, 0.125, 0.125, None, None, None, None, None, None],
    "9-room_240": [None, None, None, 1.0, 1.0, 1.0, 1.0, 0.875, 0.875, 0.75, 0.625, 0.25, 0.625, 0.25, 0.0, 0.125, 0.0, 0.0, 0.0, None, None, None],
    "10-room_300": [None, None, 1.0, 0.875, 1.0, 0.875, 0.75, 0.75, 0.875, 0.875, 0.875, 0.5, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, None, None, None, None],
}


def sigmoid(x: float, b: float, x0: float) -> float:
    z = -(x - x0) / b
    if z > 60:
        return 0.0
    if z < -60:
        return 1.0
    return 1.0 / (1.0 + math.exp(z))


def sse(data: list[tuple[float, float]], b: float, x0: float) -> float:
    err = 0.0
    for xv, yv in data:
        diff = sigmoid(xv, b, x0) - yv
        err += diff * diff
    return err


def fit_column(data: list[tuple[float, float]]) -> tuple[float, float, float]:
    best_err, best_b, best_x0 = float("inf"), -1.0, 0.0

    # Coarse search.
    for bi in range(-800, 4):
        if bi == 0:
            continue
        b = bi / 4.0
        if b >= 1.0:
            continue
        for x0 in range(-150, 301):
            err = sse(data, b, float(x0))
            if err < best_err:
                best_err, best_b, best_x0 = err, b, float(x0)

    # Local refinement.
    step_b, step_x0 = 5.0, 5.0
    while step_b > 1e-4:
        improved = False
        for db in (0.0, -step_b, step_b):
            for dx0 in (0.0, -step_x0, step_x0):
                cand_b = best_b + db
                if abs(cand_b) < 1e-9 or cand_b >= 1.0:
                    continue
                cand_x0 = best_x0 + dx0
                err = sse(data, cand_b, cand_x0)
                if err < best_err:
                    best_err, best_b, best_x0 = err, cand_b, cand_x0
                    improved = True
        if not improved:
            step_b /= 2.0
            step_x0 /= 2.0

    return best_b, best_x0, best_err


def main() -> None:
    print("column,b,x0,sse,n")
    for name, values in DATA_COLUMNS.items():
        paired = [
            (X_VALUES[i], values[i])
            for i in range(len(X_VALUES))
            if values[i] is not None
        ]
        b, x0, err = fit_column(paired)
        print(f"{name},{b:.6f},{x0:.6f},{err:.6f},{len(paired)}")


if __name__ == "__main__":
    main()
