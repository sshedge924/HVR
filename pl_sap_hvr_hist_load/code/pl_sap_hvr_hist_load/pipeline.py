from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_sap_hvr_hist_load.config.ConfigStore import *
from pl_sap_hvr_hist_load.functions import *
from prophecy.utils import *
from pl_sap_hvr_hist_load.graph import *

def pipeline(spark: SparkSession) -> None:
    df_ds_stg_hvr_rseg = ds_stg_hvr_rseg(spark)
    df_ds_stg_hvr_bkpf = ds_stg_hvr_bkpf(spark)
    df_ref_BKPF = ref_BKPF(spark, df_ds_stg_hvr_bkpf)
    df_filter_deleted_records = filter_deleted_records(spark, df_ref_BKPF)
    df_ds_stg_hvr_rbkp = ds_stg_hvr_rbkp(spark)
    df_ref_RBKP = ref_RBKP(spark, df_ds_stg_hvr_rbkp)
    ds_rbkp_tbl(spark, df_ref_RBKP)
    df_ref_RSEG = ref_RSEG(spark, df_ds_stg_hvr_rseg)
    ds_rseg_tbl(spark, df_ref_RSEG)
    ds_bkpf_tbl(spark, df_filter_deleted_records)
    df_ds_bkpf_tbl_1 = ds_bkpf_tbl_1(spark)
    df_ref_silver_BKPF = ref_silver_BKPF(spark, df_ds_bkpf_tbl_1)
    df_ds_rbkp_tbl_1 = ds_rbkp_tbl_1(spark)
    df_ref_silver_RBKP = ref_silver_RBKP(spark, df_ds_rbkp_tbl_1)
    ds_silver_rbkp_tbl(spark, df_ref_silver_RBKP)
    ds_silver_bkpf_tbl(spark, df_ref_silver_BKPF)
    df_ds_rseg_tbl_1 = ds_rseg_tbl_1(spark)
    df_ref_silver_RSEG = ref_silver_RSEG(spark, df_ds_rseg_tbl_1)
    ds_silver_rseg_tbl(spark, df_ref_silver_RSEG)
    df_ds_silver_rbkp_tbl_1 = ds_silver_rbkp_tbl_1(spark)
    df_ds_silver_rseg_tbl_1 = ds_silver_rseg_tbl_1(spark)
    df_ds_silver_bkpf_tbl_1 = ds_silver_bkpf_tbl_1(spark)
    df_join_documents = join_documents(spark, df_ds_silver_bkpf_tbl_1, df_ds_silver_rbkp_tbl_1, df_ds_silver_rseg_tbl_1)
    ds_gold_invoices_tbl(spark, df_join_documents)
    ds_adls_gold_csv(spark, df_join_documents)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_sap_hvr_ingest")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_sap_hvr_hist_load")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_sap_hvr_hist_load", config = Config)(pipeline)

if __name__ == "__main__":
    main()
