from yacs.config import CfgNode as CN


def get_default_config():
    cfg = CN()

    # ログイン情報
    cfg.user = CN()
    cfg.user.companyid = "SAMPLE_COMPANY_ID"
    cfg.user.email = "sample@sample.com"
    cfg.user.password = "sample-password"

    # 勤務時間
    cfg.attendance = CN()
    cfg.attendance.start = [10,0]
    cfg.attendance.end = [18,45]

    return cfg
