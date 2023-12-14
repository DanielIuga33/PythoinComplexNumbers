from Repository.RepoNrComplex import RepoNrComplex
from Service.ServiceNrComplex import ServiceNrComplex
from UI.UserInterface import UserInterface


def main():
    lista = []
    repo = RepoNrComplex(lista)
    srv = ServiceNrComplex(repo)
    ui = UserInterface(srv)

    ui.run_menu()


if __name__ == '__main__':
    main()
