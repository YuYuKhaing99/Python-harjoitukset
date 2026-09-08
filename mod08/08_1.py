vuodenajan = [
             "talvi", "talvi", "kevät",
             "kevät", "kevät", "kesä",
             "kesä", "kesä", "syksy",
             "syksy", "syksy", "talvi"
               ]

num =int(input("Anna kuukauden numero 1-12: "))
tulos = vuodenajan[num-1]
print("Anettu numeron vuodenajan on:",tulos)