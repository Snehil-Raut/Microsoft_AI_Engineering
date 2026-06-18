# 🚗 Vehicle Price Prediction using Linear Regression

Predicting fair market prices for used vehicles using end-to-end Linear Regression, applied to a 1M-row dataset.

## 🌟 Highlights

- End-to-end CRISP-DM pipeline: business understanding → data prep → modeling → evaluation
- Trained on ~953K vehicle records after data cleaning
- Final model: **R² = 0.9517 (95.2% variance explained)**, MAE ≈ $2.07K, RMSE ≈ $2.93K
- Identified and resolved a synthetic data artifact (price floor at $1,500) that was distorting the model
- Mixed encoding strategy: One-Hot Encoding for low-cardinality features, Target Encoding for high-cardinality features
- Multicollinearity checked and resolved using VIF before modeling

## ℹ️ Overview

This project predicts a vehicle's price based on its specifications (mileage, engine HP, transmission, fuel type, drivetrain, body type, etc.), usage history, and condition. The goal is to support a dealership's pricing decisions — flagging underpriced or overpriced listings and identifying which factors most strongly drive resale value.

**Business Requirement:** Can we build a pricing model that predicts a vehicle's fair market price based on its specifications, usage history, and condition — enabling the dealership to flag underpriced/overpriced listings and identify which factors (age, mileage, accidents, brand) most strongly drive resale value?

**Dataset:** [Vehicle Price Prediction (Kaggle)](https://www.kaggle.com/datasets/metawave/vehicle-price-prediction/data) — 1,000,000 rows, 20 columns.

## 🚀 Usage Instructions

The project is built as a Jupyter Notebook (`vehicle_price_prediction.ipynb`) and follows these stages in order:

1. **Load & Explore** — shape, dtypes, null checks, unique value counts, `describe()`
2. **Feature Engineering** — null handling, multicollinearity check (VIF), correlation analysis
3. **Encoding** — One-Hot Encoding + Target Encoding
4. **Feature Scaling** — `StandardScaler`
5. **Model Training** — `LinearRegression` (scikit-learn)
6. **Coefficient Interpretation** — bar chart of feature impact on price
7. **Actual vs Predicted Evaluation** — scatter plots, residual analysis
8. **Model Evaluation** — R², MAE, RMSE
9. **Prediction for new/unseen vehicles**

Open the notebook in VS Code or Jupyter and run cells sequentially.

## ⬇️ Installation Instructions

```bash
pip install -r requirements.txt
```

Requires Python with the packages listed in `requirements.txt` (pandas, numpy, scikit-learn, statsmodels, matplotlib, seaborn, etc.).

## 🛠️ Pipeline Summary

| Step | What Was Done |
|------|----------------|
| Data Understanding | Checked shape (1M rows, 20 cols), dtypes, nulls (`accident_history` had ~75% nulls), unique value counts for `make`, `transmission`, `body_type`, `drivetrain` |
| Data Cleaning | Filled `accident_history` nulls with `"Unknown"`; removed rows where `price == 1500` (synthetic floor, ~4.7% of data) |
| Multicollinearity | Computed VIF; dropped `year` (kept `vehicle_age`) and `mileage_per_year` (kept `mileage`) due to high VIF (>500 and >5 respectively) |
| Encoding | One-Hot Encoding (`drop_first=True`) on `transmission`, `fuel_type`, `drivetrain`, `body_type`, `seller_type`, `accident_history`, `condition`; Target Encoding (train-mean based) on `make`, `model`, `trim`, `exterior_color`, `interior_color` |
| Train-Test Split | 80/20 split before target encoding, to prevent data leakage |
| Scaling | `StandardScaler` — `fit_transform` on train, `transform` on test |
| Modeling | `LinearRegression` from scikit-learn |
| Evaluation | R², MAE, RMSE, Actual vs Predicted scatter plot, Residual plot |

## 📊 Final Model Results

- **R² Score:** 0.9517 (95.2% of price variance explained)
- **MAE:** ~$2.07 thousand
- **RMSE:** ~$2.93 thousand

## ⚠️ Challenges Faced

**1. Synthetic price floor causing skewness**
The target variable `price` showed an unusual spike in its distribution. On inspection, ~46,984 rows (4.7% of the dataset) had `price` exactly equal to $1,500 — far more frequent than any other price point, indicating a synthetic floor/clamp value rather than real-world pricing. This artificial clustering was distorting the price distribution and made it harder for the linear model to fit a clean relationship. Removing these rows improved the model's R² score and reduced distortion in the price distribution.

**2. Log transformation attempted but reduced performance**
Since `price` was still right-skewed even after removing the floor rows, a log transformation (`np.log(y_train)`, `np.log(y_test)`) was tried as a standard fix for skewed targets. After training on the log-transformed target and converting predictions back using `np.exp()`, the R² score dropped significantly (to ~0.77) compared to training directly on the raw `price` (R² ~0.95). Because of this drop, the log transformation was reverted — the final model was retrained using the original (non-log) `y_train`/`y_test`, combined with the $1,500-floor-row removal, which gave the best result.

**3. Heteroscedasticity assumption still not fully resolved**
Even with the best-performing model (no log transform, floor rows removed), the Residual vs Predicted plot still shows signs of heteroscedasticity — the spread of residuals is not constant across the range of predicted prices. The Actual vs Predicted scatter plot also shows some deviation from the ideal best-fit line rather than tightly hugging it. The exact root cause of this remaining pattern is not fully confirmed — it is suspected to relate to the inherent non-linear nature of vehicle pricing (e.g., depreciation curves) that a purely linear model cannot fully capture, but this was not conclusively diagnosed within the scope of this project.

## 🔮 Predicting for a New Vehicle

To predict price for a new car, a single-row DataFrame with the same raw feature columns is built, then passed through the same pipeline used during training:
1. One-Hot Encode using the same columns and `reindex` against `X_train.columns`
2. Target-encode `make`, `model`, `trim`, `exterior_color`, `interior_color` using the saved training-set mean lookup tables (`make_means`, `model_means`, etc.), falling back to `y_train.mean()` for unseen categories
3. Scale using the already-fitted `scaler.transform()`
4. Predict using the trained `model.predict()`

## ✍️ Author

Snehil Raut — Master's in Computer Engineering student. Project built as part of hands-on Linear Regression practice using a real-world Kaggle dataset.