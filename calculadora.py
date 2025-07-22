sales_list=[]

while True:
    print("\n-----MENÚ DE ANÁLISIS DE VENTAS-----")

    print("\n1. Ingresar lista de ventas (valores enteros positivos) ")
    print("2. Mostrar todas las ventas ingresadas")
    print("3. Calcular la venta más alta y la más baja")
    print("4. Calcular promedio de ventas")
    print("5. Contar cuántos días superaron los Q1000")
    print("6. Clasificar cada venta: alta (>1000), media (500–1000), baja (<500)")
    print("7. Salir")

    option=input("\nSeleccione una opcion: ")

    match option:
        case "1":
            num_sale=input("Cuantos días desea ingresar: ")

            if num_sale.isdigit() and int(num_sale)>0:
                num_sale=int(num_sale)
                i=1
                while num_sale != 0:
                    ingresar_venta=input(f"Ingresar un valor de venta del día {i}: ")

                    if ingresar_venta.isdigit() and int(ingresar_venta)>=0:
                        sales_list.append(int(ingresar_venta))
                        num_sale -= 1
                        i+=1
                    else:
                        print("La cantidad no es válida")
            else:
                print("La cantidad no es válida")

        case "2":
            print("La ventas ingresadas son: ")
            for i in sales_list:
                print(i)


