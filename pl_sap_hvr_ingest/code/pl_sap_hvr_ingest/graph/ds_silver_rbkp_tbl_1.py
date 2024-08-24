from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_sap_hvr_ingest.config.ConfigStore import *
from pl_sap_hvr_ingest.functions import *

def ds_silver_rbkp_tbl_1(spark: SparkSession) -> DataFrame:
    return spark.read.table("`spark_catalog`.`erp_silver`.`rbkp_tbl`")
