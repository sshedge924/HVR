from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_load_postgres_synth.config.ConfigStore import *
from pl_load_postgres_synth.functions import *

def filter_belnr_191(spark: SparkSession, in0: DataFrame) -> (DataFrame):

    try:
        registerUDFs(spark)
    except NameError:
        print("registerUDFs not working")

    in0.createOrReplaceTempView("in0")
    df1 = spark.sql("SELECT * FROM in0\r\nWHERE belnr like '191%'")

    return df1
