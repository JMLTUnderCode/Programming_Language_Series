if __name__ == "__main__":
    X = int(input("\nX = "))
    Y = int(input("Y = "))
    Z = int(input("Z = "))

    print("Asociacion Estatica de metodos:")
    ho = Y+X+1-(Y+X+1)*Y
    po = Y+Y+1-(Y+Y+1)*Y
    cir = 3*Y+Z+1-(3*Y+Z+1)*Y-(Y+Z+1)
    print(f"ho.cus(X+1) = {ho}, po.cus(Y+1) = {po}, cir.cus(Z+1) = {cir}")
    print(f"print = {ho+po+cir}")

    print("\nAsociacion Dinamica de metodos:")
    ho = 2*Y+X-2 + (Y+Z)*Z - ((2*Y+X-2)*(Y+Z)+2*Y+X+1)*(2*Y+X-2) - (Y+X+1)
    po = Y-2 + (Y+Z)*Z - ((Y-2)*(Y+Z)+Y+1)*(Y-2)
    cir = Z-2 + (Y+Z)*Z - ((Z-2)*(Y+Z)+Z+1)*(Z-2)
    print(f"ho.cus(X+1) = {ho}, po.cus(Y+1) = {po}, cir.cus(Z+1) = {cir}")
    print(f"print = {ho+po+cir}\n")