from service import Service
class UserInterface:
    def meniu(self):
        print("-----------------------------")
        print("1. Gaseste drum.")
        print("2. Incarca date din fisier.")
        print("3. Iesi.")
        print("-----------------------------")

    def run(self, repo):
        service = Service(repo)

        while True:
            self.meniu()
            comanda = input("Comanda dvs este: ")
            if comanda == "3":
                return
            elif comanda == "2":
                service.load()
            elif comanda == "1":
                service.generareSolutie(service.getRepo().getHarta(), 1, 1)
                service.store()
                service.getRepo().setCost(0)
                service.generareSolutie(service.getRepo().getHarta(), service.getRepo().getSursa(), service.getRepo().getDestinatie())
                service.store()
            else:
                print("Comanda invalida!")