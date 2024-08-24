from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_sap_hvr_ingest.config.ConfigStore import *
from pl_sap_hvr_ingest.functions import *

def ds_silver_rbkp_tbl(spark: SparkSession, in0: DataFrame):
    in0.write\
        .format("delta")\
        .option("path", "dbfs:/mnt/HVR/silver/rbkp_tbl")\
        .mode("error")\
        .saveAsTable("`spark_catalog`.`erp_silver`.`rbkp_tbl`")
