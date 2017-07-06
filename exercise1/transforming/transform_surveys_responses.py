from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *

import csv
import StringIO

def transformSurveysResponses(sc, sqlContext):
	lines = sc.textFile('hdfs:///user/w205/hospital_compare/surveys_responses.csv')

	parts = lines.map(lambda l: list(csv.reader(StringIO.StringIO(l), delimiter=','))[0])\
			.map(lambda l: [i.replace(' out of 10','') for i in l])

	rawData = parts.map(lambda t: [t[0], t[1], t[4], int(t[30].replace('Not Available','-1')), int(t[31].replace('Not Available','-1')), int(t[32].replace('Not Available','-1'))])

	schemaString = 'provider_number hospital_name state'
	fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()] + [StructField('overall_rating_dim', IntegerType(), True)] + [StructField('rating_base', IntegerType(), True)] + [StructField('rating_consistency', IntegerType(), True)]
	schema = StructType(fields)

	schemaData = sqlContext.createDataFrame(rawData, schema)
	schemaData.registerTempTable('surveys_responses')
	sqlContext.cacheTable('surveys_responses')

	results = sqlContext.sql('SELECT * FROM surveys_responses')
	results.show()

	results.rdd.saveAsTextFile('hdfs:///user/w205/hospital_compare/surveys_responses.txt')
	return
