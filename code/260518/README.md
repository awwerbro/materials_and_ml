# 2026-05-18: Smoothing Experimental Data

Supporting material for the May 18, 2026 MatSci+ML Data Club discussion on smoothing experimental data, with emphasis on Total Variation methods and Whittaker-Eilers smoothing.

## Related meeting material

- [Meeting notes](../../meetings/2026-05-18.md)
- [Slides (PowerPoint)](../../meetings/260518.pptx)

## Contents

- `sinusoid.ipynb`: Synthetic noisy sinusoid examples for comparing smoothing methods.
- `XRD_signal.ipynb`: XRD-oriented examples, including shoulder-peak behavior under smoothing.
- `data/`: Input example XRD data (`before`/`after`).
- `figures/`: Exported figures used in the discussion (convolution, Savitzky-Golay, Whittaker, CVE, and XRD comparisons).

## Notes

- The examples compare moving average/convolution baselines with regularized methods.
- Parameter selection is part of the method discussion, especially for lambda in Whittaker-Eilers style smoothing.
