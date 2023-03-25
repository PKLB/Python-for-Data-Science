class calculator:
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        print("Dot product is:", sum([x * y for x, y in zip(V1, V2)]))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        V3 = []
        for x in range(0, len(V1)):
            V3.append(float(V1[x]) + float(V2[x]))
        print("Add vector is:", V3)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        V3 = []
        for x in range(0, len(V1)):
            V3.append(float(V1[x]) - float(V2[x]))
        print("Sous vector is:", V3)
