from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(
            self,
            postgres_user: str=None,
            postgres_password: str=None,
            maxtsp_bkpf: str=None,
            maxtsp_rbkp: str=None,
            maxtsp_rseg: str=None,
            maxsync_bkpf: str=None,
            maxsync_rbkp: str=None,
            maxsync_rseg: str=None,
            maxtsp_bkpf_sil: str=None,
            maxtsp_rbkp_sil: str=None,
            maxtsp_rseg_sil: str=None,
            **kwargs
    ):
        self.spark = None
        self.update(
            postgres_user, 
            postgres_password, 
            maxtsp_bkpf, 
            maxtsp_rbkp, 
            maxtsp_rseg, 
            maxsync_bkpf, 
            maxsync_rbkp, 
            maxsync_rseg, 
            maxtsp_bkpf_sil, 
            maxtsp_rbkp_sil, 
            maxtsp_rseg_sil
        )

    def update(
            self,
            postgres_user: str="postgres",
            postgres_password: str="CloudGTM@2024",
            maxtsp_bkpf: str="2000-01-01 01:01:00",
            maxtsp_rbkp: str="2000-01-01 01:01:00",
            maxtsp_rseg: str="2000-01-01 01:01:00",
            maxsync_bkpf: str="2000-01-01 01:01:00",
            maxsync_rbkp: str="2000-01-01 01:01:00",
            maxsync_rseg: str="2000-01-01 01:01:00",
            maxtsp_bkpf_sil: str="2000-01-01 01:01:00",
            maxtsp_rbkp_sil: str="2000-01-01 01:01:00",
            maxtsp_rseg_sil: str="2000-01-01 01:01:00",
            **kwargs
    ):
        prophecy_spark = self.spark
        self.postgres_user = postgres_user
        self.postgres_password = postgres_password
        self.maxtsp_bkpf = maxtsp_bkpf
        self.maxtsp_rbkp = maxtsp_rbkp
        self.maxtsp_rseg = maxtsp_rseg
        self.maxsync_bkpf = maxsync_bkpf
        self.maxsync_rbkp = maxsync_rbkp
        self.maxsync_rseg = maxsync_rseg
        self.maxtsp_bkpf_sil = maxtsp_bkpf_sil
        self.maxtsp_rbkp_sil = maxtsp_rbkp_sil
        self.maxtsp_rseg_sil = maxtsp_rseg_sil
        pass
