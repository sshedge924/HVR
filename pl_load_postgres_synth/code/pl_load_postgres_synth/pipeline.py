from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_load_postgres_synth.config.ConfigStore import *
from pl_load_postgres_synth.functions import *
from prophecy.utils import *
from pl_load_postgres_synth.graph import *

def pipeline(spark: SparkSession) -> None:
    df_ds_cdc_file = ds_cdc_file(spark)
    df_filter_belnr_191 = filter_belnr_191(spark, df_ds_cdc_file)
    ds_postgres_hvr(spark, df_filter_belnr_191)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_load_postgres_synth")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_load_postgres_synth")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_load_postgres_synth", config = Config)(pipeline)

if __name__ == "__main__":
    main()
