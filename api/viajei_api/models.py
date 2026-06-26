from deteti import datetime

from sqlalchemy import func

from sqlalchemy.orm import mapped, mapped_as_dataclass, registry, mapped_column

table_registry = registry()

@mapped_as_dataclass(table_registry)
class user ():

    __tablename__ = 'user'

    id: mapped[int] =mapped_column(init=False, primary_key=True)
    emai: mapped[str] = mapped_column(unique=True)
    password: mapped[str]
    created_at: mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
        
    )
