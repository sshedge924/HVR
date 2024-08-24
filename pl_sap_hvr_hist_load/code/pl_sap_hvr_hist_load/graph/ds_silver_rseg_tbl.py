from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_sap_hvr_hist_load.config.ConfigStore import *
from pl_sap_hvr_hist_load.functions import *

def ds_silver_rseg_tbl(spark: SparkSession, in0: DataFrame):
    in0.write\
        .format("delta")\
        .option("path", "dbfs:/mnt/HVR/silver/rseg_tbl")\
        .mode("overwrite")\
        .saveAsTable("`spark_catalog`.`erp_silver`.`rseg_tbl`")
