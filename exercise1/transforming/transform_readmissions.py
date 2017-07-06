from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *

import csv
import StringIO

def transformReadmissions(sc, sqlContext):
	lines = sc.textFile('hdfs:///user/w205/hospital_compare/readmissions.csv')

	parts = lines.map(lambda l: list(csv.reader(StringIO.StringIO(l), delimiter=','))[0])

	rawData = parts.map(lambda p: (p[0], p[1], p[4], p[8], p[9], p[10], float(p[12].replace('Not Available','-1'))))

	schemaString = 'provider_id hospital_name state measure_name measure_id comp_national'
	fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()] + [StructField('score', FloatType(), True)]
	schema = StructType(fields)

	schemaData = sqlContext.createDataFrame(rawData, schema)
	schemaData.registerTempTable('readmissions')
	sqlContext.cacheTable('readmissions')

	results = sqlContext.sql('SELECT * FROM readmissions')
	results.show()

	results.rdd.saveAsTextFile('hdfs:///user/w205/hospital_compare/readmissions.txt')
	return


	
