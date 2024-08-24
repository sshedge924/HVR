from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_sap_hvr_hist_load.config.ConfigStore import *
from pl_sap_hvr_hist_load.functions import *

def ds_silver_bkpf_tbl_1(spark: SparkSession) -> DataFrame:
    return spark.read.table("`spark_catalog`.`erp_silver`.`bkpf_tbl`")
