from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
DARABASE_URL = "postgresql://neondb_owner:npg_Orzvoj4wLuI7@ep-odd-boat-anrn2ehf.c-6.us-east-1.aws.neon.tech/neondb?sslmode=require"
engine = create_engine(DARABASE_URL)
SessionLocal = sessionmaker(bind = engine)
Base = declarative_base()
