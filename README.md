# Data Analyst assignment

- Python pipeline scripts
  * Required folders
    * Input: Requested CSV files (product_descriptions, product_properties and manufacturers)
    * Output: It must be created before the main script execution
    * Logs: It must be created before the main script execution
  * Pipeline Execution
    * Main Script: nexMart.py (It triggers the solution)
    * Additional Scripts (external functions)
      * solutionLogs.py (Define the parameters and configuration for the LOGS)
      * dataManipulation.py (Functions to clean and format the data)
      * util.py (Functions to be used as utilities for dataframes and others)
      * nexMartAnalysis.py (Functions available for this data challangue based on the source tables)
    * Others: nexMart.YAML (Configuration file which contains parameters to be used within the pipeline)
    
- SQL scripts
  * Source Folder
    * DB -> NexMartDB_manufacturers.sql (Manufacturers table CREATE and INSERT statement from pipeline exported file)
    * DB -> NexMartDB_product_descriptions.sql (Product descriptions table CREATE and INSERT statement from pipeline exported file)
    * DB -> NexMartDB_product_properties.sql (Product properties table CREATE and INSERT statement from pipeline exported file)
  * Solution Folder
    * SQL -> SQL_Temp_Tables.sql (SQL query to create temporary tables to be used to answer the assignment questions)
    * SQL -> SQL_Q1.sql (CTE query to answer the first question)
    * SQL -> SQL_Q2.sql (CTE query to answer the second question)
  
- Power BI Dashboard
  * Main Folder
    * PowerBI -> NexMart_Dashboard.pbix (Solution created in https://app.powerbi.com/ -Trial Version-)

# Question 1

  |Manufacturername|	Total_descriptions|	Total_properties|	Total_records|
  | ---------------| ----------------- | --------------- | ------------ |
  |BOSCH|	                  3|	                  9|	                91|
  |FISCHER|	                3|	                  9|	                 5|
  |FEIN|	                   2|                   9|	                96|

  * The biggest manufacturers with potential in their data quality are Bosch and Fischer, even thought the number of product are different, most of their values remain populated with data, on the other side, Fein could improve its data quality by making few adjustments in some product desctiption.

# Question 2

  |Manufacturername|	   Total_Articles|	    Short Descriptions|	      Long Descriptions|	    Properties Technical Details|	Properties Price Quantity|
  | ---------------| ----------------- | --------------- | ------------ |  ---------------- | ------------ |
  |BOSCH|	                113|	          0.97345|	     0.99115|        0.9823|	          1|
  |FEIN|	                100|	             1|	          1|	              1|	              1|
  |FISCHER|	               5|	             1|	          1|	              1|	              1|
  |GUSTAV KLAUKE GMBH|	  40|	             1|	          1|	              1|	              1|
  |ROTHENBERGER|	        23|	             1|	          1|	              1|	              1|
  |Total|	                281|	            278|	         280|	           279|	           281|

* Mostly the fields with good data quality are the same in all maufacturers.
  * Product description -> "Short Description" and "Long Description" are almost 100% for almost all of the manufacturer. Only Bosch contains less data, but with missing data from 1% to 3% only.
  * Product properties -> "Technical Details" and "Price Quantity" are full of good data quality with ~2% missing values for Bosch only ('Technical Details'). It is important to highlight that 'Technical Details' provides key information regarding the products in order to be used for analysis porpuses.
     
  * Exception: The field "Picture normal reduced" (URL) is 100% populated for Bosh manufacturer compared to the other manufacturers.

# Additional insights

- There are 20 products which have the same id becaue they are duplicated in 'de' and 'en' (I have to define Language as second PK to avoid PK violation)
  ```js
	SELECT 
	m.Manufacturername,
	CASE WHEN p.ETIM = '' THEN 'NO' ELSE 'YES' END AS ETIM,
	CASE WHEN p.ETIM_Features = '' THEN 'NO' ELSE 'YES' END AS ETIM_Features,
	COUNT(DISTINCT p.Articlenumber) AS 'Total Articles'
	FROM product_properties p
	INNER JOIN manufacturers m
	ON p.Manufacturernumber = m.Manufacturernumber
	GROUP BY m.Manufacturername,
	CASE WHEN p.ETIM = 'NO' THEN 1 ELSE 'YES' END,
	CASE WHEN p.ETIM_Features = 'NO' THEN 'YES' ELSE 0 END
	ORDER BY 4 DESC
```
- Gustav Klauke Gmbh is the only manufacturer who contains ETIM and ETIM_Features data, it might be interesting to ask the reason of it. I would ask the business people about the technical or business reason of it in order to add/remove this manufacturer in a deeper analysis.

  ```js
      SELECT 
      m.Manufacturername,
      CASE WHEN p.ETIM = '' THEN 'NO' ELSE 'YES' END AS ETIM,
      CASE WHEN p.ETIM_Features = '' THEN 'NO' ELSE 'YES' END AS ETIM_Features,
      COUNT(DISTINCT p.Articlenumber) AS 'Total Articles'
      FROM product_properties p
      INNER JOIN manufacturers m
      ON p.Manufacturernumber = m.Manufacturernumber
      GROUP BY m.Manufacturername,
      CASE WHEN p.ETIM = 'NO' THEN 1 ELSE 'YES' END,
      CASE WHEN p.ETIM_Features = 'NO' THEN 'YES' ELSE 0 END
      ORDER BY 4 DESC
 ```
# Bonus
- Manufacturer information:
  * The manufacturer table/file should have only 1 key per manufacturer and their names should be normalized plus a creation and updated date to keep control of the changes.
- Product desciption
  * The product description should have the Language field has a 2 primery key because the records can be duplicated in the "Articlenumber" PK. (e.g. The current sample file has 6 records which are duplicated due to the description is transalted to English ('en') and the orginal ('de' is also there)
- Product properties   
  * The product property is missing key information from columns which can be very useful for deeper analysis and break-down structure (e.g. Product category and Technical specifications) and the field 'EAN' might be important to show a valid product in the market but for some product this id does not exist.
  * The product table should contain the unique manufacturer number and in case this is different it should specifiy in the manufacturer table the difference of it (e.g. location, branch, distribution center, etc)
  * The product table should act as a dimension table which contains the key id to connect to the different fact table
- Additional data
  * If it was a real proyect I would include fact tables from a model which contain the product data to work with prices before and after taxation, branches data to work with logistic and distribution data ad location data to work with countries where the products are made.
