from sqlalchemy import create_engine

def get_engine():
    return create_engine(
        "mysql+pymysql://okrkj9Aqr6VZPb8.root:UkgRlt2NTpXZY999@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/Nutrition?ssl_ca=/etc/ssl/certs/ca-certificates.crt&ssl_verify_cert=true&ssl_verify_identity=true"
    )
