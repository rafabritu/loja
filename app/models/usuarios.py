import db

class usuarios(db.loja):
    __tablename__ = "usuarios"
    
    id: Mapped[int] = mapped_column(primary_key=true)
    nome: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    telefone: Mapped[str] = mapped_column(String(13))
    senha: Mapped[str] = mapped_column(String(20))