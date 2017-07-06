from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *

import csv
import StringIO

def transformHospitals(sc, sqlContext):
        lines = sc.textFile('hdfs:///user/w205/hospital_compare/hospitals.csv')
        
	parts = lines.map(lambda l: list(csv.reader(StringIO.StringIO(l), delimiter=','))[0])
	
	rawData = parts.map(lambda t: (t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9], t[10]))

	# create dataframe
	schemaString = 'provider_id hospital_name address city state zip_code county phone_number hospital_type hospital_ownership emergency_services'
	fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()]
	schema = StructType(fields)

	schemaData = sqlContext.createDataFrame(rawData, schema)
	schemaData.registerTempTable('hospitals')

	results = sqlContext.sql('SELECT * FROM hospitals')
	results.show()

	results.rdd.saveAsTextFile('hdfs:///user/w205/hospital_compare/hospitals.txt')
	return
