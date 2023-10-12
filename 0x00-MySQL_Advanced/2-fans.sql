-- Calculate the total number of non-unique fans for each country origin
SELECT origin, SUM(nb_fans) as nb_fans
FROM bands
GROUP BY origin
ORDER BY nb_fans DESC;
