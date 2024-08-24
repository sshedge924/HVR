from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_sap_hvr_ingest.config.ConfigStore import *
from pl_sap_hvr_ingest.functions import *

def ds_stg_hvr_rseg(spark: SparkSession) -> DataFrame:
    return spark.read.format("parquet").load("dbfs:/mnt/HVR/transaction/*rseg.parquet")
