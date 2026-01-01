TOP_REGIONS_2022 = """
SELECT Region, AVG(Mean_Estimate) AS avg_obesity
FROM obesity_data
WHERE Year = 2022
GROUP BY Region
ORDER BY avg_obesity DESC
LIMIT 5;
"""

TOP_COUNTRIES = """
SELECT Country, AVG(Mean_Estimate) AS avg_obesity
FROM obesity_data
GROUP BY Country
ORDER BY avg_obesity DESC
LIMIT 5;
"""

INDIA_TREND = """
SELECT Year, AVG(Mean_Estimate) AS obesity_rate
FROM obesity_data
WHERE Country = 'India'
GROUP BY Year
ORDER BY Year;
"""

AVG_BY_GENDER = """
SELECT Gender, AVG(Mean_Estimate) AS avg_obesity
FROM obesity_data
GROUP BY Gender;
"""

LEVEL_BY_AGE = """
SELECT Obesity_Level, Age_Group, COUNT(DISTINCT Country) AS country_count
FROM obesity_data
GROUP BY Obesity_Level, Age_Group;
"""

LEAST_RELIABLE = """
SELECT Country, AVG(CI_Width) AS avg_ci
FROM obesity_data
GROUP BY Country
ORDER BY avg_ci DESC
LIMIT 5;
"""

MOST_RELIABLE = """
SELECT Country, AVG(CI_Width) AS avg_ci
FROM obesity_data
GROUP BY Country
ORDER BY avg_ci ASC
LIMIT 5;
"""

AVG_BY_AGE = """
SELECT Age_Group, AVG(Mean_Estimate) AS avg_obesity
FROM obesity_data
GROUP BY Age_Group;
"""

LOW_OBESITY = """
SELECT Country, AVG(Mean_Estimate) AS avg_obesity, AVG(CI_Width) AS avg_ci
FROM obesity_data
GROUP BY Country
HAVING avg_obesity < 25 AND avg_ci < 3
ORDER BY avg_obesity, avg_ci
LIMIT 10;
"""

FEMALE_GT_MALE = """
SELECT f.Country, f.Year,
       (f.Mean_Estimate - m.Mean_Estimate) AS gender_gap
FROM obesity_data f
JOIN obesity_data m
ON f.Country = m.Country AND f.Year = m.Year
WHERE f.Gender = 'Female'
  AND m.Gender = 'Male'
  AND (f.Mean_Estimate - m.Mean_Estimate) > 5;
"""

GLOBAL_TREND = """
SELECT Year, AVG(Mean_Estimate) AS global_avg
FROM obesity_data
GROUP BY Year
ORDER BY Year;
"""
