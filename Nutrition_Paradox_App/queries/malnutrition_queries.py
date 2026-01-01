AVG_BY_AGE = """
SELECT Age_Group, AVG(Mean_Estimate) AS avg_malnutrition
FROM malnutrition_data
GROUP BY Age_Group;
"""

TOP_COUNTRIES = """
SELECT Country, AVG(Mean_Estimate) AS avg_malnutrition
FROM malnutrition_data
GROUP BY Country
ORDER BY avg_malnutrition DESC
LIMIT 5;
"""

AFRICA_TREND = """
SELECT Year, AVG(Mean_Estimate) AS avg_malnutrition
FROM malnutrition_data
WHERE Region = 'Africa'
GROUP BY Year
ORDER BY Year;
"""

AVG_BY_GENDER = """
SELECT Gender, AVG(Mean_Estimate) AS avg_malnutrition
FROM malnutrition_data
GROUP BY Gender;
"""

LEVEL_CI = """
SELECT Malnutrition_Level, Age_Group, AVG(CI_Width) AS avg_ci
FROM malnutrition_data
GROUP BY Malnutrition_Level, Age_Group;
"""

INCREASING = """
SELECT Country,
       MAX(Mean_Estimate) - MIN(Mean_Estimate) AS change
FROM malnutrition_data
GROUP BY Country
HAVING change > 0;
"""

MIN_MAX_YEAR = """
SELECT Year,
       MIN(Mean_Estimate) AS min_malnutrition,
       MAX(Mean_Estimate) AS max_malnutrition
FROM malnutrition_data
GROUP BY Year;
"""

HIGH_CI = """
SELECT Country, Year, CI_Width
FROM malnutrition_data
WHERE CI_Width > 5;
"""
