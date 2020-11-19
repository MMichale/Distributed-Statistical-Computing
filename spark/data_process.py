
#!/usr/bin/env python3.6
import findspark
findspark.init("/usr/lib/spark-current")
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import os 
import pickle
spark = SparkSession.builder.appName("Python Spark with DataFrame").getOrCreate()
# schema_sdf = StructType([
#         StructField('Year', IntegerType(), True),
#         StructField('Month', IntegerType(), True),
#         StructField('DayofMonth', IntegerType(), True),
#         StructField('DayOfWeek', IntegerType(), True),
#         StructField('DepTime', DoubleType(), True),
#         StructField('CRSDepTime', DoubleType(), True),
#         StructField('ArrTime', DoubleType(), True),
#         StructField('CRSArrTime', DoubleType(), True),
#         StructField('UniqueCarrier', StringType(), True),
#         StructField('FlightNum', StringType(), True),
#         StructField('TailNum', StringType(), True),
#         StructField('ActualElapsedTime', DoubleType(), True),
#         StructField('CRSElapsedTime',  DoubleType(), True),
#         StructField('AirTime',  DoubleType(), True),
#         StructField('ArrDelay',  DoubleType(), True),
#         StructField('DepDelay',  DoubleType(), True),
#         StructField('Origin', StringType(), True),
#         StructField('Dest',  StringType(), True),
#         StructField('Distance',  DoubleType(), True),
#         StructField('TaxiIn',  DoubleType(), True),
#         StructField('TaxiOut',  DoubleType(), True),
#         StructField('Cancelled',  IntegerType(), True),
#         StructField('CancellationCode',  StringType(), True),
#         StructField('Diverted',  IntegerType(), True),
#         StructField('CarrierDelay', DoubleType(), True),
#         StructField('WeatherDelay',  DoubleType(), True),
#         StructField('NASDelay',  DoubleType(), True),
#         StructField('SecurityDelay',  DoubleType(), True),
#         StructField('LateAircraftDelay',  DoubleType(), True)
#     ])
# air = spark.read.options(header='true').schema(schema_sdf).csv("/data/airdelay_small.csv")
# air_1 = air.select(['Arrdelay','Year','Month','DayofMonth','DayOfWeek','DepTime','CRSDepTime','CRSArrTime','UniqueCarrier','ActualElapsedTime','Origin','Dest','Distance'])
# air_1 = air_1.na.drop()
# air_1.coalesce(1).write.option('header','true').csv('data_bicheng')



air = spark.read.options(header='true', inferSchema='true').csv("/user/devel/data_bicheng/")
data = air.withColumn('Arrdelay',F.when(air['Arrdelay'] > 0, 1).otherwise(0))



dummy_info_path = "~/students/2020210972bicheng/spark/_dummy_info.pkl"
dummy_info = pickle.load(open(os.path.expanduser(dummy_info_path), "rb"))



for i in dummy_info['factor_dropped'].keys():
    if len(dummy_info['factor_dropped'][i]) > 0:
        data = data.replace(dummy_info['factor_dropped'][i], 'others', i)




year = [int(i) for i in dummy_info['factor_selected']['Year']]
month = [int(i) for i in dummy_info['factor_selected']['Month']]
dayofweek = [int(i) for i in dummy_info['factor_selected']['DayOfWeek']]
uc = [i for i in dummy_info['factor_selected']['UniqueCarrier']]+['others']
ori = [i for i in dummy_info['factor_selected']['Origin']]+['others']
dest = [i for i in dummy_info['factor_selected']['Dest']]+['others']


exprs_year = [F.when(F.col("Year") == i, 1).otherwise(0).alias('year_'+str(i)) for i in year]
exprs_month = [F.when(F.col("Month") == i, 1).otherwise(0).alias('month_'+str(i)) for i in month]
exprs_dayofweek = [F.when(F.col("DayOfWeek") == i, 1).otherwise(0).alias('dayofweek_'+str(i)) for i in dayofweek]
exprs_uc = [F.when(F.col("UniqueCarrier") == i, 1).otherwise(0).alias('uc_'+i) for i in uc]
exprs_ori = [F.when(F.col("Origin") == i, 1).otherwise(0).alias('ori_'+i) for i in ori]
exprs_dest = [F.when(F.col("Dest") == i, 1).otherwise(0).alias('dest_'+i) for i in dest]

exprs = exprs_year+exprs_month+exprs_dayofweek+exprs_uc+exprs_ori+exprs_dest

data = data.select('Arrdelay','DayofMonth','DepTime','CRSDepTime','CRSArrTime','ActualElapsedTime','Distance',*exprs)
# shape (5423403, 155) 
print((data.count(), len(data.columns)))
# data.coalesce(1).write.option('header','true').csv('2020210972bicheng/dummy_data')



# from pyspark.sql.functions import monotonically_increasing_id
# data = data.withColumn(“id”,monotonically_increasing_id())
# pivoted = data.groupBy("id").pivot("Year").agg(F.lit(1)).na.fill(0)