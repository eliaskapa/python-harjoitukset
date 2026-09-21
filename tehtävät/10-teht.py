class Hissi:
    def __init__(self, alin, ylin, siirry_kerrokseen):
        self.ylin = kerros_ylös
        self.alin = kerros_alas
        self.siirry_kerrokseen = 1
    def siirry_kerrokseen(self):
        while siirry_kerrokseen < kerros_ylös:
            siirry_kerrokseen += 1
            print(self.siirry_kerrokseen)
        while siirry_kerrokseen > kerros_alas:
            siirry_kerrokseen -= 1
            print(self.siirry_kerrokseen)


hissi1 = Hissi(1,12)

hissi1(siirry_kerrokseen(5))

print(f"hissi on nyt kerroksessa {siirry_kerrokseen}")





