from main import models, engine

models.Base.metadata.create_all(bind=engine)
