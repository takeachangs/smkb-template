---
type: Sample
title: DEMO101 Lecture 3
description: Fictional DEMO101 source for the SMKB workshop; not a real course.
---

# DEMO101 Lecture 3 (Oct 27): Inference for the slope

*Posted slides. You missed this lecture.*

## Why inference

b₁ is computed from one sample. A different sample would give a different slope. We want to know how sure we are about the true slope β₁.

## Standard error of the slope

- s² = SSE / (n − 2), the estimate of the error variance (uses SSE from Lecture 2)
- SE(b₁) = s / √Sxx (uses Sxx from Lecture 1)

## Confidence interval

b₁ ± t* × SE(b₁)

where t* comes from the t distribution with n − 2 degrees of freedom.

## Hypothesis test

- H₀: β₁ = 0 (no linear relationship)
- Test statistic: t = b₁ / SE(b₁), with n − 2 degrees of freedom
- A small p-value is evidence that the slope is not zero.

## Connection

If the 95% confidence interval for β₁ does not contain 0, the test at the 5% level rejects H₀.
