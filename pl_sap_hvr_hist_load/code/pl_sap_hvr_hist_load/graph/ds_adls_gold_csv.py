from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_sap_hvr_hist_load.config.ConfigStore import *
from pl_sap_hvr_hist_load.functions import *

def ds_adls_gold_csv(spark: SparkSession, in0: DataFrame):
    in0.write\
        .option("header", True)\
        .option("sep", ",")\
        .mode("overwrite")\
        .option("separator", ",")\
        .option("header", True)\
        .csv("dbfs:/mnt/HVR/\"gold_invoices.csv\"_temp")
    from prophecy.utils.gems_utils import concatenateFiles
    concatenateFiles(
        spark,
        ".csv",
        "overwrite",
        "dbfs:/mnt/HVR/\"gold_invoices.csv\"_temp",
        "dbfs:/mnt/HVR/\"gold_invoices.csv\"",
        True,
        True
    )
