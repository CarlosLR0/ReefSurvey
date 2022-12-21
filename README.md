# ReefSurveyCreate a repository on GitHub with write permissions for your entire team. Your git repository will be referred to hereafter as <repoBase>/.
Download the latest published version of the data set as a tar.gz archive by following links from the data source page: Biogeographic characterization of fish and benthic communities, Flower Garden Banks, Texas 2006-09-13 to 2012-10-02 (NOAA) Links to an external site.. Note: This data has been superseded for scientific purposes, but is still valid for this assignment.
Using command line tools, unpack the data folder from the downloaded archive to <repoBase>/external/survey/ (you should have, e.g., <repoBase>/external/survey/0-data/).
Create <repoBase>/external/survey/README.md as a Markdown-format file and cite the data archive appropriately (refer to the source URL).
Design a database schema (using your choice of visualization) for the “Fish Dump” sheet of the Excel documents in the <repoBase>/external/survey/0-data/ directory. Note: The data in this file is the same as, but in a different format from, the data in the <repoBase>/external/survey/1-data/ directory that you will parse and store in step 7.
Normalize your database schema to third normal form. Ensure each table has a (potentially composite) primary key and that relationships between tables (where appropriate) are described with foreign keys.
Write a SQL script in <repoBase>/scripts to create required users, permissions, database, and tables according to the schema developed in the last step.

Write a second SQL script in <repoBase>/scripts that DROPs any relevant database, users, etc. currently in the database.

Write a Python script in <repoBase>/scripts that uses the built-in csv library Links to an external site.to convert fish dump data from a CSV file provided as an argument into SQL INSERT statements that correspond to your schema. Your script should not access the database directly.

The converter should do some basic file-format checking (headers should match expected strings, the number of columns per row should be consistent, output statements should be correct, etc.) If your script fails because the input data is incorrect, correct the data, create <repoBase>/external/survey/CHANGES to describe the major changes, and update <repoBase>/external/survey/README.md to point out the existence of CHANGES.

Write a final script that uses a loop to run the converter script on all CSV files in <repoBase>/external/survey/1-data/ and redirects its output to the mysql command line tool to insert the formatted data into the MySQL database.

Write a few SQL queries that show the database was correctly loaded from the CSV files.
