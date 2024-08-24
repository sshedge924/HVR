from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_load_postgres_synth.config.ConfigStore import *
from pl_load_postgres_synth.functions import *

def ds_postgres_hvr(spark: SparkSession, in0: DataFrame):
    in0.write\
        .format("jdbc")\
        .option("url", "jdbc:40.67.234.61://localhost:5432/GTMSAP_REPLICA")\
        .option("dbtable", "bkpf")\
        .option("user", f"{Config.postgres_user}")\
        .option("password", f"{Config.postgres_password}")\
        .option("driver", "v42.7.3")\
        .mode("append")\
        .save()
