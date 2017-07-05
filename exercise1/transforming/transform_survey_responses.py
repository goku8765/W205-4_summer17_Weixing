from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *

import csv
import StringIO

### TRANSFORM SURVEY RESPONSES DATA

def transformSurveyResponses(sc, sqlContext):
	lines = sc.textFile('hdfs:///user/w205/hospital_compare/survey_responses.csv')
	print lines.first()

	exclude = []
	
	# parse and filter data with excluded values
	parts = lines.map(lambda l: list(csv.reader(StringIO.StringIO(l), delimiter=','))[0]) \
			.map(lambda l: [i.replace(' out of 10','') for i in l]) \
			.filter(lambda l: not any (x in l for x in exclude))

	rawData = parts.map(lambda p: [p[0], p[1], p[4], int(p[30].replace('Not Available','-1'))])
	# print parts.first()
	# print rawData.first()

	# create schema
	schemaString = 'provider_number hospital_name state'
	fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()] + [StructField('overall_rating_dim', IntegerType(), True)]
	schema = StructType(fields)

	# create dataframe, store in temp table
	schemaData = sqlContext.createDataFrame(rawData, schema)
	schemaData.registerTempTable('survey_results')
	sqlContext.cacheTable('survey_results')

	# query data and save to CSV
	results = sqlContext.sql('SELECT * FROM survey_results')
	results.show()
	# print results.count()

	results.rdd.saveAsTextFile('hdfs:///user/w205/hospital_compare/survey_results.csv')
	return
