class Hissi:
    def __init__(self, alin, ylin, siirry_kerrokseen):
        self.ylin = kerros_ylös
        self.alin = kerros_alas
        self.siirry_kerrokseen = 1
    def siirry_kerrokseen(self, kohdekerros):
        while siirry_kerrokseen < kohdekerros:
            self.kerros_ylös()
        while siirry_kerrokseen > kohdekerros:
            self.kerros_alas()
            


hissi1 = Hissi(1,12)

hissi1(siirry_kerrokseen(5))

print(f"hissi on nyt kerroksessa {siirry_kerrokseen}")





