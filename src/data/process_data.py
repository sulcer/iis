import pandas as pd

df_1 = pd.read_csv("data/raw/students_scores.csv")
df_2 = pd.read_excel('data/raw/students.xlsx')

df = pd.merge(df_1, df_2, left_index=True, right_index=True)

df.drop(columns=['Unnamed: 0_x'], inplace=True)
df.drop(columns=['Unnamed: 0_y'], inplace=True)

df['AVG_subject'] = (df['STEM_subjects'] + df['H_subjects']) / 2

df.to_csv("data/processed/current_data.csv", index=False)
