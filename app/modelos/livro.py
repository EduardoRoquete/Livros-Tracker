from app.modelos.status_livro import StatusLivro


class Livro:

    def __init__(self, nome_livro: str, capitulo: int, autor: str, avaliacao: float, status: StatusLivro = StatusLivro.LENDO, id: int | None = None):
        self.__nome_livro = ""
        self.__capitulo = None
        self.__autor = None
        self.__avaliacao = None
        self.__status = status
        self.__id = id

        self.nome_livro = nome_livro
        self.capitulo = capitulo
        self.autor = autor
        self.avaliacao = avaliacao
        self.status = status

    @property
    def nome_livro(self):
        return self.__nome_livro

    @nome_livro.setter
    def nome_livro(self, valor_nome_livro: str):

        if valor_nome_livro.strip():
            self.__nome_livro = valor_nome_livro

        raise ValueError(f"Não são aceitos livros com nome vazio!")

    @property
    def capitulo(self):
        return self.__capitulo

    @capitulo.setter
    def capitulo(self, valor_capitulo: float):

        if valor_capitulo >= 0:
            self.__capitulo = valor_capitulo

        raise ValueError("Só são aceitos valores não negativos!")

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, valor_autor:str):

        if valor_autor.strip():
            self.__autor = valor_autor

        raise ValueError(f"Não são aceitos autores com nome vazio!")

    @property
    def avaliacao(self):
        return self.__avaliacao

    @avaliacao.setter
    def avaliacao(self, valor_avaliacao:float):

        if 0.0 <= valor_avaliacao <= 5.0:
            self.__avaliacao = valor_avaliacao

        raise ValueError(f"Não foi possível avaliar. Valor '{valor_avaliacao}' deve estar entre 0 e 5!")

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, valor_status:StatusLivro):

        if isinstance(valor_status, StatusLivro):
            self.__status = valor_status

        raise ValueError(f"Status '{valor_status}' não é um status compatível!")

    @property
    def id(self):
        return self.__id