# merge_datasets.py
import pandas as pd

# Load datasets
df_assistant = pd.read_csv('nasatlx_assistant.csv')
df_current = pd.read_csv('nasatlx_current.csv')

# Add dataset_type column
df_assistant['dataset_type'] = 'assistant'
df_current['dataset_type'] = 'current'

# Merge datasets
merged_df = pd.concat([df_assistant, df_current], ignore_index=True)

# Save merged dataset
merged_df.to_csv('mergedNasatlx.csv', index=False)
print("Merged dataset saved!")