# Data Analyst assignment

- Python pipeline scripts
  * Required folders
    Input: Requested CSV files (product_descriptions, product_properties and manufacturers)
    Output: It must be created before the main script execution
    Logs: It must be created before the main script execution
  * Pipeline Execution
    Main Script: nexMart.py (It triggers the solution)
    Additional Scripts (external functions)
      % solutionLogs.py (Define the parameters and configuration for the LOGS)
      % dataManipulation.py (Functions to clean and format the data)
      % util.py (Functions to be used as utilities for dataframes and others)
      % nexMartAnalysis.py (Functions available for this data challangue based on the source tables)
    Others: nexMart.YAML (Configuration file which contains parameters to be used within the pipeline)
    
- SQL scripts
  * Source Folder
    DB -> NexMartDB_manufacturers.sql (Manufacturers table CREATE and INSERT statement from pipeline exported file)
    DB -> NexMartDB_product_descriptions.sql (Product descriptions table CREATE and INSERT statement from pipeline exported file)
    DB -> NexMartDB_product_properties.sql (Product properties table CREATE and INSERT statement from pipeline exported file)
  * Solution Folder
    SQL -> SQL_Temp_Tables.sql (SQL query to create temporary tables to be used to answer the assignment questions)
    SQL -> SQL_Q1.sql (CTE query to answer the first question)
    SQL -> SQL_Q2.sql (CTE query to answer the second question)
  
- Power BI Dashboard
  * Main Folder
    PowerBI -> NexMart_Dashboard.pbix (Solution created in https://app.powerbi.com/ -Trial Version-)

# Question 1

  Manufacturername	Total_descriptions	Total_properties	Total_records
  BOSCH	                  3	                  9	                91
  FISCHER	                3	                  9	                5
  FEIN	                  2	                  9	                96

# Question 2

  Manufacturername	Total_Articles	Short_Desc	  Long_Desc	Technical_details	Price_quantity
  BOSCH	                113	          0.97345	     0.99115	        0.9823	          1
  FEIN	                100	             1	          1	              1	              1
  FISCHER	               5	             1	          1	              1	              1
  GUSTAV KLAUKE GMBH	  40	             1	          1	              1	              1
  ROTHENBERGER	        23	             1	          1	              1	              1
  Total	                281	            278	         280	           279	           281

# Bonus
