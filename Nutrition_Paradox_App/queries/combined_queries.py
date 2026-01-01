COUNTRY_COMPARE = """
SELECT o.Country,
       AVG(o.Mean_Estimate) AS obesity,
       AVG(m.Mean_Estimate) AS malnutrition
FROM obesity_data o
JOIN malnutrition_data m ON o.Country = m.Country
WHERE o.Country IN ('India','United States','Brazil','Nigeria','China')
GROUP BY o.Country;
"""

GENDER_COMPARE = """
SELECT o.Gender,
       AVG(o.Mean_Estimate) AS obesity,
       AVG(m.Mean_Estimate) AS malnutrition
FROM obesity_data o
JOIN malnutrition_data m ON o.Gender = m.Gender
GROUP BY o.Gender;
"""

REGION_COMPARE = """
SELECT o.Region,
       AVG(o.Mean_Estimate) AS obesity,
       AVG(m.Mean_Estimate) AS malnutrition
FROM obesity_data o
JOIN malnutrition_data m ON o.Region = m.Region
WHERE o.Region IN ('Africa','Americas Region')
GROUP BY o.Region;
"""

OB_UP_MAL_DOWN = """
SELECT o.Country,
       MAX(o.Mean_Estimate) - MIN(o.Mean_Estimate) AS obesity_change,
       MAX(m.Mean_Estimate) - MIN(m.Mean_Estimate) AS malnutrition_change
FROM obesity_data o
JOIN malnutrition_data m ON o.Country = m.Country
GROUP BY o.Country
HAVING obesity_change > 0 AND malnutrition_change < 0;
"""

AGE_TREND = """
SELECT o.Year, o.Age_Group,
       AVG(o.Mean_Estimate) AS obesity,
       AVG(m.Mean_Estimate) AS malnutrition
FROM obesity_data o
JOIN malnutrition_data m
ON o.Year = m.Year AND o.Age_Group = m.Age_Group
GROUP BY o.Year, o.Age_Group
ORDER BY o.Year;
"""
