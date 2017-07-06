SELECT
  state,
    ROUND(SUM(score)/COUNT(score),3)
    AS avg_score
  FROM readmissions
  WHERE score <> -1
  GROUP BY state
  ORDER BY avg_score DESC
  LIMIT 10

SELECT
  state,
  	SUM(CASE WHEN comp_national = 'Better than the National Rate' THEN 1 ELSE 0 END)
  		AS num_better,
  	SUM(CASE WHEN comp_national = 'Worse than the National Rate' THEN 1 ELSE 0 END)
  		AS num_worse,
  	COUNT(*) AS total_measures,
  	ROUND(100 * (SUM(CASE WHEN comp_national = 'Better than the National Rate' THEN 1 ELSE 0 END) -
  			SUM(CASE WHEN comp_national = 'Worse than the National Rate' THEN 1 ELSE 0 END)) / COUNT(*), 1)
  	  AS outperform_ratio
  FROM readmissions
  WHERE score <> -1
  GROUP BY state
  ORDER BY outperform_ratio DESC
  LIMIT 10
