from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy import text
from sqlalchemy.orm import Session

from controllers.router import api_router
from db.database import pegar_sessao

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login-form")
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = FastAPI()


@app.get("/api/teste_db", tags=["Teste DB"])
def teste_conexao_db(db: Session = Depends(pegar_sessao)):
    try:
        resultado = db.execute(text("SELECT 1")).scalar()
        return {
            "mensagem": "Conexão com o banco de dados bem-sucedida!",
            "resultado": resultado,
        }
    except Exception as e:
        return {"error": str(e)}


app.include_router(api_router, prefix="/api")
