from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *

from transform_hospitals import *
from transform_procedures import *
from transform_survey_responses import *

sc = SparkContext("local", "transform data")
sqlContext = SQLContext(sc)

transformHospitals(sc, sqlContext)
transformReadmissions(sc, sqlContext)
transformSurveyResponses(sc, sqlContext)
