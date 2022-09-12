import pandas as pd 

# load in the data 

sparcs = pd.read_csv('data/SPARCS_2015.csv')
sparcs

atlas = pd.read_csv('')

#small dataframe in terminal
patients_small = patients[['Id', 'SSN']]
print(patients_small.to_markdown())

patients.columns
medications.columns

patients['Id']
medications['PATIENT']


#enrich medications table with info from patients table
df_patinets_small = patients[['Id', 'CITY', 'STATE', 'COUNTY','ZIP']]
print(df_patinets_small.sample(10).to_markdown())

df_medications_small = medications[['PATIENT','CODE','DESCRIPTION','BASE_COST']]
print(df_medications_small.sample(10).to_markdown())

combined_df = df_medications_small.merge(df_patinets_small, how='left', left_on='PATIENT', right_on='Id')

combined_df.columns
combined_df.to_csv('enrichment/example_data/combined_df.csv')

payers_df = pd.read_csv('enrichment/example_data/payers.csv')
payers_df.columns

payers_df.small = payers_df[['']]

#
med_df = medications[['PATIENT','PAYER','CODE']]
pay_df = payers_df[['Id','CITY']]
pay_df.rename(columns={'CITY':'CITY_PAYER'}, inplace=True)
pat_df = patients[['Id', 'CITY', 'STATE', 'COUNTY','ZIP']]
#first merge
med_pay_df = med_df.merge(pay_df, how='left', left_on='PAYER', right_on='Id')
med_pay_df = med_pay_df.drop(columns=['Id'])
med_pay_df.shape
#Drop duplicates base don patient
med_pay_df_nodups = med_pay_df.drop_duplicates(subset=['PATIENT'])
med_pay_df_nodups
med_pay_df_nodups = med_pay_df.drop(columns=(['CODE']))
#add med pay to pat df
final_df = pat_df.merge(med_pay_df_nodups, how='left', left_on='Id', right_on='PATIENT')


