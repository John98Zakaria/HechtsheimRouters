routers = {1: "Fritzbox 7170"}


def usereingabe(gegenstand):
    global routers
    if (gegenstand == "Router"):
        try:
            print("Wahlen Sie einen Router")
            for key,value in routers.items():
                print(f"{key} : {value}")
            r_wahl = int(input())
            if(r_wahl not in routers):
                print("Falsche Wahl")
                return usereingabe("Router")
            return r_wahl
        except ValueError:
            print("Falsche wahl")
            return usereingabe("Router")


while (True):
    router = usereingabe("Router")
    if(router ==1):
        import Fritz7170


