from Domain.NrComplex import NrComplex


class RepoNrComplex:
    def __init__(self, lista: list):
        self.__repo = lista

    def add(self, nr: NrComplex):
        """
        Adauga un nr Complex in repository
        :param nr: Numarul complex
        :return: none
        """
        self.__repo.append(nr)

    def add_poz(self, nr: NrComplex, poz: int):
        """
        Adauga un nr Complex in repository pe pozitie specificata
        :param nr: Numarul complex
        :param poz: pozitia pe care se adauga numarul
        :return: none
        """
        self.__repo.insert(poz, nr)

    def delete(self, nr: NrComplex):
        """
        Sterge un nr Complex din repository
        :param nr: Numarul complex
        :return: none
        """
        result = []
        for n in self.get_all():
            if n != nr:
                result.append(n)
        self.set(result)

    def delete_poz(self, poz):
        """
        Sterge un nr Complex de pe o pozitie
        :param poz: pozitia
        :return: none
        """
        self.__repo.pop(poz)

    def update(self, nr_old: NrComplex, nr_new: NrComplex):
        """
        Modifica datele unui numar Complex din repository
        :param nr_old: numarul de modificat
        :param nr_new: noul numar
        :return: none
        """
        poz = self.__repo.index(nr_old)
        self.__repo.pop(poz)
        self.__repo.insert(poz, nr_new)

    def get_size(self):
        """

        :return: Lungimea repository-ului
        """
        return len(self.__repo)

    def get_all(self):
        """

        :return: Repository-ul
        """
        return self.__repo

    def set(self, lista: list):
        """
        Modifica repository-ul cu o lista data
        :param lista: noul repository
        :return:  none
        """
        self.__repo = lista
