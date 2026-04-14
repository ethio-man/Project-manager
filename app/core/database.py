from sqlmodel import create_engine , Session

DATABASE_URL='postgresql://postgres:3dag5@postgres-db:5432/project'

engine=create_engine(DATABASE_URL,echo=True)

def get_session():
    with Session(engine) as session:
        yield session