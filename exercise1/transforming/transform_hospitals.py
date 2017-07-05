from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *

import csv
import StringIO

def transformHospitals(sc, sqlContext):
        lines = sc.textFile('hdfs:///user/w205/hospital_compare/hospitals.csv')
	# print lines.first()

	# parse and filter data with excluded values
	parts = lines.map(lambda l: list(csv.reader(StringIO.StringIO(l), delimiter=','))[0])
	
	rawData = parts.map(lambda p: (p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10]))
	# print parts.first()
	# print rawData.first()

	# create dataframe, store in temp table
	schemaString = 'provider_id hospital_name address city state zip_code county_name phone_number hospital_type hospital_ownership emergency_services'
	fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()]
	schema = StructType(fields)

	schemaData = sqlContext.createDataFrame(rawData, schema)
	schemaData.registerTempTable('hospitals')

	# query data and save to CSV
	results = sqlContext.sql('SELECT * FROM hospitals')
	results.show()
	# print results.count()

	results.rdd.saveAsTextFile('hdfs:///user/w205/hospital_compare/')
	return
