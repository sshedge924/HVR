from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_sap_hvr_hist_load.config.ConfigStore import *
from pl_sap_hvr_hist_load.functions import *

def ref_RBKP(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("belnr").alias("doc_number"), 
        col("gjahr").alias("fiscal_year"), 
        col("mandt").alias("client_id"), 
        col("ctxkrs").alias("curr_exch_rate"), 
        col("makzn").alias("amount_loc_currency"), 
        col("lotkz").alias("lot_type_ind"), 
        col("fityp").alias("fin_tran_type"), 
        col("ort01").alias("location"), 
        col("pfach").alias("po_box"), 
        col("budat").alias("doc_posting_date"), 
        col("beznk").alias("bank_ac_num"), 
        col("brnch").alias("branch_code"), 
        col("stjah").alias("fis_year"), 
        col("cputm").alias("data_entry_time"), 
        col("kursx").alias("exch_rate"), 
        col("txjcd_bnk").alias("bank_tran_code"), 
        col("copy_user").alias("user_who_copied"), 
        col("stkzn").alias("stock_transfer_ind"), 
        col("pstlz").alias("postal_code"), 
        col("xcpdk").alias("xcomp_code_post_ind"), 
        col("inv_tran").alias("inv_tran_entry"), 
        col("secco").alias("sec_cost_centre"), 
        col("fdtag").alias("fix_asset_tag_num"), 
        col("xegdr").alias("ext_goods_rcpt_ind"), 
        col("fdlev").alias("fix_asset_level"), 
        col("assign_next_date").alias("tran_next_date"), 
        col("prepay_status"), 
        col("xblnr").alias("ref_document_num"), 
        col("xinve").alias("investment_ind"), 
        col("kursf").alias("exch_rate_for_curr_tran"), 
        col("qsshb").alias("prepay_loc_curr_amt"), 
        col("prepay_awkey").alias("prepay_key"), 
        col("name3").alias("third_name"), 
        col("uzawe").alias("prepay_ref"), 
        col("lieffn").alias("foreign_curr_amt"), 
        col("xrech").alias("reversal_doc_ind"), 
        col("copy_by_year").alias("doc_copiedto_year"), 
        col("rmwwr").alias("doc_curr_amt"), 
        col("lifnr").alias("vendor_num"), 
        col("xmwst").alias("tax_salespurch_ind"), 
        col("mwskz_bnk").alias("bank_tran_taxcode"), 
        col("bupla").alias("bus_place_bank_tran"), 
        col("bvtyp").alias("bank_tran_type"), 
        col("txkrs").alias("exch_rate_tax_coll"), 
        col("qsfbt").alias("for_curr_tax_amt"), 
        col("knumvl").alias("vendor_ac_num"), 
        col("assign_end_date"), 
        col("xautakz").alias("auto_pay_ind"), 
        col("wwert").alias("doc_val_local_curr"), 
        col("bukrs").alias("company_code"), 
        col("copy_to_belnr").alias("tgt_doc_num_forcopying"), 
        col("wmwst2").alias("local_curr_tax_amt"), 
        col("zlspr").alias("payment_method"), 
        col("esrre").alias("esr_refr_num"), 
        col("wskto").alias("withholding_tax_amt"), 
        col("stceg").alias("tax_exempt_code"), 
        col("stras").alias("street_address"), 
        col("cpudt").alias("last_change_date"), 
        col("filkd").alias("billing_doc_type"), 
        col("zuonr").alias("assignment_num"), 
        col("frgkz").alias("for_trade_ind"), 
        col("egmld").alias("elect_data__intchg_ind"), 
        col("rebzj").alias("withholding_tax_ind"), 
        col("qsskz").alias("spl_gl_tran_tax_ind"), 
        col("zfbdt").alias("pay_ref_date"), 
        col("j_1kftind").alias("spl_tax_treat_ind"), 
        col("rebzg").alias("ref_doc_num"), 
        col("landl").alias("country_key"), 
        col("reindat").alias("invoice_rcpt_date"), 
        col("ivtyp").alias("invoice_type"), 
        col("j_1kftbus").alias("bus_area_taxpurpose"), 
        col("regio").alias("tran_region"), 
        col("zbd3t").alias("amt_locl_currency"), 
        col("j_1tpbupl").alias("tax_base_amt"), 
        col("wmwst1").alias("tax_amt_local_curr"), 
        col("dtaws").alias("tran_date"), 
        col("kidno").alias("cust_iden_um"), 
        col("vgart").alias("tran_type"), 
        col("zbd2t").alias("tran_amt"), 
        col("vatdate").alias("vat_calc_date"), 
        col("blart").alias("doc_type"), 
        col("name2").alias("second_name"), 
        col("j_1kfrepre").alias("repr_key"), 
        col("knumve").alias("vendor_acc_num"), 
        col("stcd4").alias("tax_num4"), 
        col("stcdt").alias("tax_regn_num_date"), 
        col("lzbkz").alias("pay_meth_ind"), 
        col("logsys").alias("logical_sys"), 
        col("pskto").alias("pay_block_key"), 
        col("zbd2p").alias("percent_tax_disc2"), 
        col("stcd2").alias("entity_tax_iden"), 
        col("esrnr").alias("esr_ref_num"), 
        col("makzmw").alias("for_curr_amt"), 
        col("arkuen").alias("local_currency_amount"), 
        col("stblg").alias("doc_num_forclearing"), 
        col("zbd1t").alias("amt_curr1"), 
        col("xref3").alias("ref_info"), 
        col("zbd1p").alias("percent_curr1"), 
        col("ername").alias("name_entry_creator"), 
        col("lieffmw").alias("amt_local_currency"), 
        col("copy_to_year").alias("data_copiedto_year"), 
        col("spras").alias("lang_key"), 
        col("xrbtx").alias("ref_doc_text"), 
        col("bankl").alias("bank_key"), 
        col("stkzu").alias("spl_gl_ind"), 
        col("zlsch").alias("pay_method_code"), 
        col("hbkid").alias("house_bank_id"), 
        col("empfg").alias("emp_group"), 
        col("mwskz2").alias("tax_code2"), 
        col("bkont").alias("bank_acc_no"), 
        col("j_1bnftype").alias("bus_partner_type"), 
        col("repart").alias("recon_partner"), 
        col("saprl").alias("sap_rel_status"), 
        col("assign_status"), 
        col("usnam").alias("user_name"), 
        col("erfpr").alias("type_of_doc_ind"), 
        col("arkuemw").alias("local_curr+amt"), 
        col("bldat").alias("document_date"), 
        col("stkza").alias("special_gl_ind"), 
        col("gsber").alias("business_area"), 
        col("bankn").alias("bank_account_num"), 
        col("stcd1").alias("tax_number"), 
        col("zbfix").alias("fixed_asset_ind"), 
        col("name1").alias("name_entity"), 
        col("zterm").alias("payment_terms"), 
        col("empfb").alias("emp_feedback_ind"), 
        col("diekz").alias("tax_discount_ind"), 
        col("rbstat").alias("rebate_status"), 
        col("pstl2").alias("postal_code2"), 
        col("bktxt").alias("bank_text"), 
        col("anred").alias("sal_title_person"), 
        col("mwskz1").alias("tax_category"), 
        col("tcode").alias("tran_code_identifier"), 
        col("copy_by_belnr").alias("document_num_copy"), 
        col("stcd3").alias("tax_iden_num3"), 
        col("hkont").alias("account_number"), 
        col("name4"), 
        col("esrpz").alias("spl_payment_ind"), 
        col("dtams").alias("local_curr_amt"), 
        col("erfnam").alias("name_entry_creator2"), 
        col("bkref").alias("tran_bank_ref_num"), 
        col("banks").alias("tran_bank_name"), 
        col("waers").alias("tran_currency_code"), 
        col("land1").alias("tran_country_code"), 
        col("sgtxt").alias("tran_desc_details"), 
        col("_fivetran_deleted"), 
        date_format(col("_fivetran_synced"), "yyyy-MM-dd HH:mm:ss").alias("_fivetran_synced"), 
        date_format(current_timestamp(), "yyyy-MM-dd HH:mm:ss").alias("_loadtimestamp"), 
        split(input_file_name(), "/")[4].alias("_filename"), 
        substring(split(input_file_name(), "/")[4], 1, 14).cast(LongType()).alias("_file_timestamp")
    )
