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
                    ingresar_venta=input(f"Ingresar un valor de venta {i}: ")

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
            sales_in_day=0
            for i in sales_list:
                sales_in_day+=1
                print(f"En el día {sales_in_day} las ventas fueron de Q{i}")

        case "3":
            if len(sales_list)>0:
                max_sale=sales_list[0]
                min_sale=sales_list[0]

                for i in sales_list:
                    if i>max_sale:
                        max_sale=i
                    if i<min_sale:
                        min_sale=i
                print(f"La venta más baja fue de Q{min_sale} y la más alta fue de Q{max_sale} ")

            else:
                print("No hay ventas ingresadas")

        case "4":
            total_sales=0
            for i in sales_list:
                total_sales+=i
            average_sales=total_sales/len(sales_list)
            print(f"El promedio de las ventas fue de Q{round(average_sales,2)}")

        case "5":
            upper_sale_count=0
            for i in sales_list:
                if i>1000:
                    upper_sale_count+=1
                else:
                    continue
            print(f"En {upper_sale_count} días de supero los Q1000 en ventas")

        case "6":
            high_sale=[]
            middle_sale=[]
            low_sale=[]
            for i in sales_list:
                if i>1000:
                    high_sale.append(i)
                elif i<=1000 and i>500:
                    middle_sale.append(i)
                elif i<=500:
                    low_sale.append(i)
            print("Las ventas clasificadas son: ")
            print(f"Ventas altas: {high_sale}")
            print(f"Ventas en la media: {middle_sale}")
            print(f"Ventas bajas: {low_sale}")
        case "7":
            print("\nSaliendo...")
            break
        case _:
            print("Opción no válida, vuelva a intentarlo")