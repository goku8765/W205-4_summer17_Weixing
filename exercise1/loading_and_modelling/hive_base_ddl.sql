DROP TABLE hospitals;
CREATE EXTERNAL TABLE hospitals(
provider_id string,
hospital_name string,
address string,
city string,
state string,
zip_code string,
county_name string,
phone_number string,
hospital_type string,
hospital_ownership string,
emergency_services string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES(
"separatorChar" = ",",
"quoteChar" = "'",
"escapeChar" = '\\'
)
STORED AS TEXTFILE
LOCATION '/user/w205/hospital_compare';



DROP TABLE effective_care;
CREATE EXTERNAL TABLE effective_care(
provider_id string,
hospital_name string,
address string,
city string,
state string,
zip_code string,
county_name string,
phone_number string,
condition string,
measure_id string,
measure_name string,
score int,
sample int,
footnote string,
measure_start_date string,
measure_end_date string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES(
"separatorChar" = ",",
"quoteChar" = "'",
"escapeChar" = '\\'
)
STORED AS TEXTFILE
LOCATION '/user/w205/hospital_compare';



DROP TABLE readmissions;
CREATE EXTERNAL TABLE readmissions
(
provider_id string,
hospital_name string,
address string,
city string,
state string,
zip_code string,
county_name string,
phone_number string,
measure_name string,
measure_id string,
compared_to_national string,
denominator int,
score double,
lower_estimate double,
higher_estimate double,
measure_start_date string,
measure_end_date string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES(
"separatorChar" = ",",
"quoteChar" = "'",
"escapeChar" = '\\'
)
STORED AS TEXTFILE
LOCATION '/user/w205/hospital_compare';



DROP TABLE survey_responses;
CREATE EXTERNAL TABLE survey_responses(
provider_number string,
hospital_name string,
address string,
city string,
state string,
zip_code string,
county_name string,
comm_nurses_achieve string,
comm_nurses_improve string,
comm_nurses_dim string,
comm_docs_achieve string,
comm_docs_improve string,
comm_docs_dim string,
responsive_achieve string,
responsive_improve string,
responsive_dim string,
pain_mgmt_achieve string,
pain_mgmt_improve string,
pain_mgmt_dim string,
comm_meds_achieve string,
comm_meds_improve string,
comm_meds_dim string,
clean_achieve string,
clean_improve string,
clean_dim string,
discharge_achieve string,
discharge_improve string,
discharge_dim string,
overall_rating_achieve string,
overall_rating_improve string,
overall_rating_dim string,
hcahps_base_score string,
hcahps_consistency_score string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES(
"separatorChar" = ",",
"quoteChar" = "'",
"escapeChar" = '\\'
)
STORED AS TEXTFILE
LOCATION '/user/w205/hospital_compare';



DROP TABLE measures;
CREATE EXTERNAL TABLE measures(
measure_name string,
measure_id string,
measure_start_quarter string,
measure_start_date string,
measure_end_quarter string,
measure_end_date string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES(
"separatorChar" = ",",
"quoteChar" = "'",
"escapeChar" = '\\'
)
STORED AS TEXTFILE
LOCATION '/user/w205/hospital_compare';
