MAX TAM 10

def ingresar_valores (frente, final, cola, contador):
    if (final + 1) % MAX_TAM frente:
        print("Desbordamiento de la cola")
        return frente, final, cola, contador
    
    elemento int(input("Ingrese un elemento para la cola: "))
    final (final + 1) % MAX TAM
    cola [Final] elemento
    contador +1
    print("Elemento", contador, "agregado a la cola:", elemento)
    return frente, final, cola, contador

def eliminar_elemento(frente, final, contador):
    if frente final:
        print("La cola esta vacia, no se puede eliminar")
        return frente, contador
    
    frente (frente + 1) % MAX TAM
    contador1
    print("Elemento eliminado de la cola.")
    return frente, contador

def imprimir (frente, final, cola):
    print("Elementos de la cola en el orden de ingreso:")
    1 frente $+1$
    while i! Final + 1:
        print(" "+str(cola[i]))
        $i=(i+1)\%MAX\_TAM$
    print()

def main():
    cola [0] MAX TAM
    contador $=0$
    frente $=0$
    final $=8$

    respuesta input("Desea agregar elementos a la cola? (s/n): ").lower()

    while respuesta == "s" and contador < 10:
        frente, final, cola, contador ingresar_valores (frente, final, cola, contador)
        if contador < 10:
            respuesta input("Desea agregar mas elementos a la cola? (s/n): ").lower()

    if frente == final:
        print("La cola esta vacia.")
        return

    primer_elemento cola[(frente + 1) % MAX_TAM]
    print("El primer elemento de la cola es:", primer_elemento)

    frente, contador eliminar_elemento(frente, final, contador)
    imprimir (frente, final, cola)

if __name__ == "_main_":
    main()
