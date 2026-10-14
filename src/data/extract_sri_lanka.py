
from pathlib import Path

import numpy as np
import pandas as pd
import rasterio
from rasterio.windows import from_bounds

ROOT = Path(__file__).resolve().parents[2]

raster_path = (
    ROOT / "data" / "raw"
    / "chirps-v3.0.rnl.2024.01.01.tif"
)

output_path = (
    ROOT / "data" / "processed"
    / "rainfall_sri_lanka_2024-01-01.csv"
)

# Approximate Sri Lanka bounding box
west, south, east, north = 79.5160, 5.9187, 81.8792, 9.8358

with rasterio.open(raster_path) as src:
    window = from_bounds(
        west, south, east, north, src.transform
    ).round_offsets().round_lengths()

    data = src.read(1, window=window, masked=False)
    transform = src.window_transform(window)

    rows, cols = np.indices(data.shape)
    xs, ys = rasterio.transform.xy(
        transform, rows, cols, offset="center"
    )

    values = data.ravel()
    latitudes = np.asarray(ys).ravel()
    longitudes = np.asarray(xs).ravel()

    # Exclude the known missing-data sentinel.
    valid = np.isfinite(values) & (values != -9999)

    df = pd.DataFrame({
        "date": "2024-01-01",
        "latitude": latitudes[valid],
        "longitude": longitudes[valid],
        "rainfall_value": values[valid],
    })

output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False)

print("CSV saved:", output_path)
print("Valid records:", len(df))
print(df.head())
