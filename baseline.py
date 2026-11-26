####
""""
Problem
CT body composition is measured on a single slice, usually L3, but many clinical CTs never reach that level. A chest CT misses L3; an abdominal CT may stop above the pelvis. We treat muscle, subcutaneous fat (SAT), visceral fat (VAT) and IMAT as continuous craniocaudal profiles and ask whether the unscanned part can be predicted, with honest uncertainty, from the part that was scanned.
Question and novelty
Main question: how accurately can the unobserved part of a multi-tissue profile be predicted from a partial scan, and does learning the anatomical frame jointly with the prediction, from the image, beat existing curve-completion methods in accuracy and calibration?
1.	New task framing. Body composition as a spatial curve to complete, not one number at a fixed level. Standard completion methods (functional PCA, kNN, Gaussian processes) have not been benchmarked on it.
2.	Learned per-tissue frame (main claim). A monotone warp per tissue, learned jointly with completion. Hypothesis: muscle follows the skeleton, fat follows sex and body type, so one fixed frame (mm or vertebral) is suboptimal.
3.	Image conditioning. The model sees the CT, not only the extracted partial curve; expected gain is largest at low coverage.
4.	Calibrated extrapolation. Prediction intervals that keep nominal coverage as distance from the scan edge grows.
Method
The warps have no ground truth: they are learned only because aligning patients makes the hidden part easier to predict.
1.	Image encoder turns the visible slices into a patient code (body type, scan position).
2.	Warp head maps that code to a monotone warp per tissue, z (mm) → t ∈ [0, 1]: positive softplus increments per bin, cumulatively summed. Per-tissue warp = shared warp + a penalised deviation.
3.	Curve decoder takes (t, patient code) and returns area and variance per tissue, so it can predict outside the scan.
4.	Training: randomly hide a top or bottom block of variable length; Gaussian NLL on the hidden part. Partial scans contribute where measured.
5.	Keeping warps meaningful: smoothness penalty, pull toward the vertebral frame, soft L2 anchors at TotalSegmentator landmarks (T12, L3, L5, acetabulum), few degrees of freedom.
6.	Calibration: conformal prediction on a held-out set, coverage reported against distance from the scan edge.
Build order, each step must beat the last: fixed frame → learned shared warp → per-tissue warp → image input.
•	Baselines: functional PCA completion, registr, kNN curve matching, Gaussian process, direct regression of L3 from the partial scan.
•	Ablations: fixed vs learned frame; shared vs per-tissue warp; curve vs image input; image vs demographics/BMI only.
•	Metrics: completion error against distance from the scan edge, both truncation directions; interval coverage.
•	Real partial scans: 20–30 patients with chest and abdominal CTs close in time; predict from one, check against the other.
•	Clinical readout: L3, T12, acetabular roof, and agreement on sarcopenia classification at standard cut-offs.
"""
