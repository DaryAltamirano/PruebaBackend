import methods as me
print("{}El lago musical{}".format("/"*20,"\\"*20))


repeat=""
while True:
    sound= input("(0 : Salir) Introduce {}el sonido : ".format(repeat)).strip().lower()
    if(me.isValid(sound)):
        print("resultado : {}".format(me.sound_missing(sound)))
        repeat=""
    elif(sound == "0"):
        break
    else:
        repeat="de nuevo "

print("{}Gracias por jugar{}".format("/"*20,"\\"*20))   