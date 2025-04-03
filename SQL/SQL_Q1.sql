WITH data_quality_manufacturers AS (
SELECT 
p.Manufacturernumber,
d.Articlenumber,
d.Language,
d.Total_descriptions,
p.Total_properties
FROM descriptions_data_quality d
INNER JOIN properties_data_quality p
ON d.Articlenumber = p.Articlenumber
WHERE d.Language = 'de'
),
data_validation_manufacturers AS (
	SELECT
  m.Manufacturername,
  d.Articlenumber,
  d.Total_descriptions,
  d.Total_properties
  FROM data_quality_manufacturers d
  INNER JOIN manufacturers m
  ON m.Manufacturernumber = d.Manufacturernumber
)
SELECT Manufacturername,
       Total_descriptions,
       Total_properties,
       COUNT(*) AS Total_records
       FROM (
	       SELECT Manufacturername,
		      Total_descriptions,
                      Total_properties,
                      RANK() OVER (PARTITION BY Manufacturername ORDER BY Total_descriptions DESC, Total_properties DESC)
         AS quality_rank
         FROM data_validation_manufacturers)
WHERE quality_rank = 1
GROUP BY Manufacturername, Total_descriptions, Total_descriptions
ORDER BY 2 DESC, 3 DESC
