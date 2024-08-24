from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(
            self,
            postgres_user: str=None,
            postgres_password: str=None,
            bron_bkpf_maxtsp: int=None,
            bron_rbkp_maxtsp: int=None,
            bron_rseg_maxtsp: int=None,
            maxsync_bkpf: int=None,
            maxsync_rbkp: int=None,
            maxsync_rseg: int=None,
            slvr_bkpf_maxtsp: int=None,
            slvr_rbkp_maxtsp: int=None,
            slvr_rseg_maxtsp: int=None,
            gold_invoices_maxtsp: int=None,
            **kwargs
    ):
        self.spark = None
        self.update(
            postgres_user, 
            postgres_password, 
            bron_bkpf_maxtsp, 
            bron_rbkp_maxtsp, 
            bron_rseg_maxtsp, 
            maxsync_bkpf, 
            maxsync_rbkp, 
            maxsync_rseg, 
            slvr_bkpf_maxtsp, 
            slvr_rbkp_maxtsp, 
            slvr_rseg_maxtsp, 
            gold_invoices_maxtsp
        )

    def update(
            self,
            postgres_user: str="postgres",
            postgres_password: str="CloudGTM@2024",
            bron_bkpf_maxtsp: int=0,
            bron_rbkp_maxtsp: int=0,
            bron_rseg_maxtsp: int=0,
            maxsync_bkpf: int=0,
            maxsync_rbkp: int=0,
            maxsync_rseg: int=0,
            slvr_bkpf_maxtsp: int=0,
            slvr_rbkp_maxtsp: int=0,
            slvr_rseg_maxtsp: int=0,
            gold_invoices_maxtsp: int=0,
            **kwargs
    ):
        prophecy_spark = self.spark
        self.postgres_user = postgres_user
        self.postgres_password = postgres_password
        self.bron_bkpf_maxtsp = self.get_int_value(bron_bkpf_maxtsp)
        self.bron_rbkp_maxtsp = self.get_int_value(bron_rbkp_maxtsp)
        self.bron_rseg_maxtsp = self.get_int_value(bron_rseg_maxtsp)
        self.maxsync_bkpf = self.get_int_value(maxsync_bkpf)
        self.maxsync_rbkp = self.get_int_value(maxsync_rbkp)
        self.maxsync_rseg = self.get_int_value(maxsync_rseg)
        self.slvr_bkpf_maxtsp = self.get_int_value(slvr_bkpf_maxtsp)
        self.slvr_rbkp_maxtsp = self.get_int_value(slvr_rbkp_maxtsp)
        self.slvr_rseg_maxtsp = self.get_int_value(slvr_rseg_maxtsp)
        self.gold_invoices_maxtsp = self.get_int_value(gold_invoices_maxtsp)
        pass
