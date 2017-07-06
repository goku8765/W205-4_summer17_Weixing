from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *
from pyspark.sql.functions import *

import os
dir = os.path.dirname(__file__)

# BEST HOSPITALS

def bestHospitals(sc, sqlContext):
	filename = os.path.join(dir, 'best_hospitals/best_hospitals.sql')
	fd = open(filename)
	sqlScript = fd.read()
	fd.close

	results = sqlContext.sql(sqlScript)
	results.show()


# BEST STATES

def bestStates(sc, sqlContext):
	filename = os.path.join(dir, 'best_states/best_states.sql')
	fd = open(filename)
	sqlScript = fd.read()
	fd.close

	results = sqlContext.sql(sqlScript)
	results.show()
	

# VARIABILITY OF PROCEDURES

def hospitalVariability(sc, sqlContext):
	filename = os.path.join(dir, 'hospital_variability/hospital_variability.sql')
	fd = open(filename)
	sqlScript = fd.read()
	fd.close

	results = sqlContext.sql(sqlScript)
	results.show()


# HOSPITALS AND PATIENTS

def hospitalPatients(sc, sqlContext):
	filename = os.path.join(dir, 'hospitals_and_patients/hospitals_and_patients.sql')
	fd = open(filename)
	sqlScript = fd.read()
	fd.close

	results = sqlContext.sql(sqlScript)
	results.show()
	
