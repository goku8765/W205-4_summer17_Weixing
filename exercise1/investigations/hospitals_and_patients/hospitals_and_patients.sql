SELECT
	hospital_name,
	overall_rating_dim,
	rating_base,
	rating_consistency,
	rating_base + rating_consistency
    AS rating_combine
  FROM surveys_responses
  WHERE overall_rating_dim <> -1 AND rating_base <> -1 AND rating_consistency <> -1
  GROUP BY hospital_name
  ORDER BY rating_combine DESC
  LIMIT 10
