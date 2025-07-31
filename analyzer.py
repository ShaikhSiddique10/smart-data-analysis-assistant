import pandas as pd

def summarize_data(df):
    summary = {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "missing": df.isnull().sum().to_dict(),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "summary": df.describe().to_dict()
    }
    return summary

def top_insight(df):
    insights = []

    # 1. Missing Values Insight
    missing = df.isnull().sum()
    missing = missing[missing > 0].sort_values(ascending=False)
    if not missing.empty:
        top_missing = missing.index[0]
        insights.append(f"🔍 Column **'{top_missing}'** has the most missing values: {missing.iloc[0]}.")

    # 2. Dominant Categorical Values
    cat_cols = df.select_dtypes(include='object').columns
    for col in cat_cols:
        top_val = df[col].value_counts().idxmax()
        count = df[col].value_counts().max()
        insights.append(f"📊 Most frequent value in **'{col}'** is **'{top_val}'** ({count} times).")

    # 3. High Correlation
    num_df = df.select_dtypes(include='number')
    if num_df.shape[1] >= 2:
        corr = num_df.corr().abs()
        corr.values[[range(len(corr))]*2] = 0  # Zero diagonal
        max_corr = corr.unstack().sort_values(ascending=False).drop_duplicates()
        if not max_corr.empty and max_corr.iloc[0] > 0.7:
            col_pair = max_corr.index[0]
            insights.append(f"📈 High correlation ({max_corr.iloc[0]:.2f}) between **'{col_pair[0]}'** and **'{col_pair[1]}'**.")

    # 4. Numeric Summary (Mean Outliers)
    for col in num_df.columns:
        mean = df[col].mean()
        max_val = df[col].max()
        min_val = df[col].min()
        if abs(max_val - mean) > 2 * df[col].std():
            insights.append(f"⚠️ Column **'{col}'** has large variation (mean: {mean:.2f}, max: {max_val}, min: {min_val}).")

    return "\n\n".join(insights) if insights else "No actionable insights found in current dataset."
