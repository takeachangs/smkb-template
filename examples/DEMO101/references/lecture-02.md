---
type: Sample
title: DEMO101 Lecture 2
description: Fictional DEMO101 source for the SMKB workshop; not a real course.
---

# DEMO101 Lecture 2 (Oct 20): Residuals, R², and checking assumptions

## Residuals

The residual for observation i is what the line got wrong:

eᵢ = yᵢ − ŷᵢ

With an intercept in the model, the residuals always sum to zero.

## R²

- SST = Σ (yᵢ − ȳ)², the total variation in y
- SSE = Σ eᵢ², the variation the line does not explain
- R² = 1 − SSE / SST

R² is the fraction of the variation in y explained by x. A high R² does not mean the model is appropriate.

## Assumptions

1. **Linearity:** the relationship between x and y is a straight line.
2. **Independence:** the errors are independent of each other.
3. **Constant variance:** the spread of the errors is the same for all x.
4. **Normality:** the errors are roughly normal.

## Residual plots

Plot residuals against fitted values.

- A random cloud around zero: assumptions look fine.
- A curve: linearity is violated.
- A funnel shape: constant variance is violated.
