SELECT
  measure_name, measure_id,
    ROUND(SQRT(AVG(score*score)-AVG(score)*AVG(score)),3)
    AS se_score
FROM readmissions
WHERE score <> -1
GROUP BY measure_name, measure_id
ORDER by se_score DESC
LIMIT 10'
