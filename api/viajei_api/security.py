from datetime import datetime, timedalta 
from zoneinfo import ZoneInfo

from jwt import encode

SECRET_KEY = 'your- very-secret-and-exclusive-key'
ALGORITHM = 'HS256'
ACCESS_TOKEN_ESPIRE_MINUTES = 30

def create_token(dados: dict):
   para_codificar = dados.copy()
    # BR = UTC-03
    expira = datetime.now(
      tz=ZoneInfo('UTC') +
      timedelta(minutes=ACCESS_TOKEN_ESPIRE_MINUTES)

    )
   
   para_codificar.update({'exp': expira})
   jwt_codificado = encode(para_codificar,
   CHAVE_SECRETA, 
   algoritm=ALGORITHM
)
   
   return jwt_codificado