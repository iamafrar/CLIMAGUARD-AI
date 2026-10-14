
from pathlib import Path

import numpy as np
import rasterio
from rasterio.windows import from_bounds

file_path = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "raw"
    / "chirps-v3.0.rnl.2024.01.01.tif"
)

# Approximate bounding box for Sri Lanka
west, south, east, north = 79.5, 5.5, 82.5, 10.0

print("CLIMAGUARD AI - Sri Lanka Rainfall Check")
print("=" * 45)

with rasterio.open(file_path) as src:
    print("No-data metadata:", src.nodata)
    print("Band data type:", src.dtypes[0])
    print("Scale:", src.scales[0])
    print("Offset:", src.offsets[0])

    window = from_bounds(
        west, south, east, north, src.transform
    ).round_offsets().round_lengths()

    data = src.read(1, window=window, masked=False)

    # CHIRPS rainfall rasters commonly use -9999
    # as a missing-data sentinel; verify this against
    # the product documentation before final analysis.
    valid = data[np.isfinite(data) & (data != -9999)]

    print("Sri Lanka window shape:", data.shape)
    print("Total pixels:", data.size)
    print("Missing/sentinel pixels:", np.count_nonzero(data == -9999))
    print("Other non-finite pixels:", np.count_nonzero(~np.isfinite(data)))

    if valid.size:
        print("Valid pixel count:", valid.size)
        print("Minimum:", float(valid.min()))
        print("Maximum:", float(valid.max()))
        print("Mean:", float(valid.mean()))
    else:
        print("No valid values found in this window")

print("\nCheck completed")
