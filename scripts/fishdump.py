import mysql.connector
import pandas as pd

# Import CSV
data = pd.read_csv (r'/home/carlos/GIT/reef_survey/2.3/data/1-data/FGBS-0800-1100/FishDump.csv')   
df = pd.DataFrame(data)

# Connect to SQL Server
conn = mysql.connector.connect(user='admin', password='team2project',
                              host='my-database.clh7uaufcnt6.us-east-1.rds.amazonaws.com',
                              database='fish_dump')
cursor = conn.cursor()


# Create Table
cursor.execute('''
                create table if not exists fish_dump (
                 id INT  PRIMARY KEY NOT NULL auto_increment,
  region TEXT NOT NULL,
  sub_region TEXT NOT NULL,
  study_area TEXT NOT NULL,
  survey_year INTEGER NOT NULL,
  batch_code TEXT NOT NULL,
  survey_index INTEGER NOT NULL,
  survey_date DATE NOT NULL,
  latitude DECIMAL(9,6) NOT NULL,
  longitude DECIMAL(9,6) NOT NULL,
  management TEXT NOT NULL,
  structure_type TEXT NOT NULL,
  family TEXT NOT NULL,
  scientific_name TEXT NOT NULL,
  common_name TEXT NOT NULL,
  trophic TEXT NOT NULL,
  fish_length DECIMAL(5,2) NOT NULL,
  fish_count INTEGER NOT NULL
);
                
                ''')

#Insert DataFrame to table

for row in df.itertuples():
    cursor.execute('''
                insert ignore into fish_dump (region, sub_region, study_area, survey_year, batch_code, survey_index, survey_date, latitude, longitude, management, structure_type, family, scientific_name, common_name, trophic, fish_length, fish_count)
                values (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)
                ''',
                   (row.Region,
                   row.SubRegion,
                   row.StudyArea,
                   row.SurveyYear,
                   row.BatchCode,
                   row.SurveyIndex,
                   row.SurveyDate,
                   row.Latitude,
                   row.Longitude,
                   row.Management,
                   row.StructureType,
                   row.Family,
                   row.ScientificName,
                   row.CommonName,
                   row.Trophic,
                   row.FishLength,
                   row.FishCount)
                   )
    conn.commit()    
cnx.close()
