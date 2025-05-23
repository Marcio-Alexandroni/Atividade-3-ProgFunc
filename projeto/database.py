from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ajuste user, senha e host se necessário
DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/ativ3"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
Base = declarative_base()