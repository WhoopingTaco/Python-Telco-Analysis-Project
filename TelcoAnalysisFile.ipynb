!pip install numpy
!pip install pandas
!pip install python-calamine
!pip install xlrd

import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

df = pd.read_csv("C:/Users/mudit.000/Downloads/telecom_users-dataset.csv")

# Remove NA columns
df_clean = df.drop(columns=["Unnamed: 0", "Provider", "Age"])

# Convert TotalCharges to numeric
df_clean["TotalCharges"] = pd.to_numeric(df_clean["TotalCharges"], errors="coerce")

# Filter for Non-Senior Citizens
non_seniors = df_clean[df_clean["SeniorCitizen"] == 0]

# 1. Male (Non-Senior Citizens) counts
male_non_seniors = non_seniors[non_seniors["gender"] == "Male"]

male_summary = {
    "Phone Service": (male_non_seniors["PhoneService"] == "Yes").sum(),
    "Internet Service": (male_non_seniors["InternetService"] != "No").sum(),
    "Device Protection": (male_non_seniors["DeviceProtection"] == "Yes").sum(),
    "Streaming TV": (male_non_seniors["StreamingTV"] == "Yes").sum(),
    "Paperless Billing": (male_non_seniors["PaperlessBilling"] == "Yes").sum()
}

# 2. Female (Non-Senior Citizens) counts for specific services
female_non_seniors = non_seniors[non_seniors["gender"] == "Female"]

female_summary = {
    "Phone Service": (female_non_seniors["PhoneService"] == "Yes").sum(),
    "Internet Service": (female_non_seniors["InternetService"] != "No").sum(),
    "Device Protection": (female_non_seniors["DeviceProtection"] == "Yes").sum(),
    "Streaming TV": (female_non_seniors["StreamingTV"] == "Yes").sum(),
    "Paperless Billing": (female_non_seniors["PaperlessBilling"] == "Yes").sum()
}

male_summary, female_summary

summary_df = pd.DataFrame([male_summary, female_summary], index=["Male (Non-Senior)", "Female (Non-Senior)"])

# Combine male and female summaries
summary_table = pd.DataFrame([male_summary, female_summary], index=["Male (Non-Senior)", "Female (Non-Senior)"])

# Convert to tabulated string
tabulated_summary = tabulate(summary_table, headers="keys", tablefmt="fancy_grid")

print(tabulated_summary)



# Plot grouped bar chart
plt.figure(figsize=(10,6))
summary_df.T.plot(kind="bar", figsize=(10,6))

plt.title("Service Subscriptions by Gender (Non-Senior Citizens)", fontsize=14)
plt.ylabel("Number of Subscribers")
plt.xlabel("Services")
plt.xticks(rotation=30)
plt.legend(title="Gender")
plt.tight_layout()
plt.show()

# Display unique values from each column
unique_values = {col: df_clean[col].unique() for col in df_clean.columns}

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Gender distribution
df_clean["gender"].value_counts().plot(kind="bar", ax=axes[0,0], color=["skyblue", "pink"])
axes[0,0].set_title("Gender Distribution")

# Senior Citizen distribution
df_clean["SeniorCitizen"].value_counts().plot(kind="bar", ax=axes[0,1], color=["green", "red"])
axes[0,1].set_title("Senior Citizen vs Non-Senior")

# Internet Service distribution
df_clean["InternetService"].value_counts().plot(kind="bar", ax=axes[1,0], color="orange")
axes[1,0].set_title("Internet Service Types")

# Contract type distribution
df_clean["Contract"].value_counts().plot(kind="bar", ax=axes[1,1], color="purple")
axes[1,1].set_title("Contract Types")

plt.tight_layout()
plt.show()

unique_values

# Unique values table
unique_table_data = []
for col, values in unique_values.items():
    # Convert array to string, limit to first 6 unique values for brevity
    val_list = list(values)
    display_vals = val_list[:6]
    if len(val_list) > 6:
        display_vals.append("...")
    unique_table_data.append([col, ", ".join(map(str, display_vals))])

# Create tabulated string
unique_tabulated = tabulate(unique_table_data, headers=["Column", "Unique Values (sample)"], tablefmt="fancy_grid")

print(unique_tabulated)

import seaborn as sns

# Set style
sns.set(style="whitegrid")

# Create multiple plots
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# 1. Churn rate by Gender
sns.countplot(data=df_clean, x="gender", hue="Churn", ax=axes[0,0], palette="Set2")
axes[0,0].set_title("Churn by Gender")

# 2. Churn rate by Contract type
sns.countplot(data=df_clean, x="Contract", hue="Churn", ax=axes[0,1], palette="Set1")
axes[0,1].set_title("Churn by Contract Type")
axes[0,1].tick_params(axis='x', rotation=20)

# 3. Monthly Charges distribution
sns.histplot(df_clean["MonthlyCharges"], bins=30, kde=True, ax=axes[1,0], color="teal")
axes[1,0].set_title("Distribution of Monthly Charges")

# 4. Correlation heatmap for numeric columns
numeric_df = df_clean[["tenure", "MonthlyCharges", "TotalCharges"]].dropna()
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=axes[1,1])
axes[1,1].set_title("Correlation Heatmap")

plt.tight_layout()
plt.show()
