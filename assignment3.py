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
#check merged data columns 
combined_df.columns
#Drop duplicates based on zip code
combined_df_nodups = combined_df.drop_duplicates(subset=['Zip_Code_3_digits'])
#save merged data without duplicates as new csv
combined_df.to_csv('enriched/combined_df.csv')