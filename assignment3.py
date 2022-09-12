import pandas as pd 

# load in the data 

sparcs = pd.read_csv('data/SPARCS_2015.csv')
#cleaning column names
sparcs.columns = sparcs.columns.str.replace('[^A-Za-z0-9]+', '_')
#checking column names
sparcs.columns

atlas = pd.read_csv('data/2015_ADI.csv')
#check column names
atlas.columns

#choosing what data from neighborhood atlas to enrich sparcs data with
sparcs_small = sparcs[['Zip_Code_3_digits', 'Gender', 'Length_of_Stay', 'Type_of_Admission', 'Total_Costs']]
print(sparcs_small.sample(10).to_markdown()) #quick check in terminal

atlas_small = atlas[['ZIPID','GISJOIN', 'ADI_NATRANK', 'ADI_STATERNK']]
print(atlas_small.sample(10).to_markdown()) #quick check in terminal

#merge data
combined_df = sparcs_small.merge(atlas_small, how='left', left_on='Zip_Code_3_digits', right_on='ZIPID')
combined_df = combined_df.drop(columns=['ZIPID'])
#check merged data columns and save as new csv
combined_df.columns
#Drop duplicates based on zip code
combined_df_nodups = combined_df.drop_duplicates(subset=['Zip_Code_3_digits'])
#save merged data without duplicates as new csv
combined_df.to_csv('enriched/combined_df.csv')

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


