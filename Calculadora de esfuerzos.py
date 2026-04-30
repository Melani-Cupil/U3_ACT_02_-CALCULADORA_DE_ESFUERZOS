import math

def mostrar_introduccion():
    print("      ALGORITMO PARA EL CÁLCULO DE ESFUERZOS NORMALES")
    print("Descripción: Solución a los tres casos de la Tabla 1.")
    print("Este programa solicita la geometría en metros y calcula el")
    print("esfuerzo normal total en los puntos de análisis.")

def calcular_perfil_l():
    print("CÁLCULO DE ESFUERZOS: CASO A (PERFIL L)")
    mx, my = 100.0, 50.0
    try:
        b = float(input("Ingrese base b (m): "))
        h = float(input("Ingrese altura h (m): "))
        t = float(input("Ingrese espesor t (m): "))

        a1, x1, y1 = b*h, b/2, h/2
        bv, hv = b - t, h - t
        a2 = bv * hv
        x2, y2 = b-bv/2, h-hv/2

        area_total = a1 - a2
        cx = ((a1*x1)+(-a2*x2))/area_total
        cy = ((a1*y1)+(-a2*y2))/area_total

        ix1 = (b*(h**3))/12+a1*(x1-cx)**2
        iy1 = (h*(b**3))/12+a1*(y1-cy)**2
        ix2 = (bv*hv**3)/12+a2*(x2-cx)**2
        iy2 = (hv*bv**3)/12+ a2*(y2-cy)**2
        
        ix, iy = ix1 - ix2, iy1 - iy2

        puntos_globales = {
            'a': (0, h), 'b': (t, h), 'c': (0, t), 'd': (t, t),
            'e': (t, t), 'f': (t, t), 'g': (b, t), 'h': (0, 0),
            'i': (0, 0), 'j': (b, 0)
        }

        print(" RESULTADOS GEOMÉTRICOS")
        print(f"Centroide: Cx = {cx}, Cy = {cy}")
        print(f"Inercias:  Ix = {ix}, Iy = {iy}")
        
        print(f"\n{'Punto':<8} | {'Dist X':<15} | {'Dist Y':<15} | {'Total (Pa)':<15} | {'Estado'}")
        print("-" * 75)
        for p, coord in puntos_globales.items():
            
            if p in ['f', 'i']:
                dist_x = 0.0
            else:
                dist_x = coord[0] - cx
                
            if p in ['c', 'd']:
                dist_y = 0.0
            else:
                dist_y = cy - coord[1]

            s_mx, s_my = (-mx * dist_y) / ix, (-my * dist_x) / iy
            total = s_mx + s_my
            estado = "TENSIÓN" if total > 0 else "COMPRESIÓN"
            print(f"{p:<8} | {dist_x:>15.6f} | {dist_y:>15.6f} | {total:>15.2f} | {estado}")
    except Exception as e: print(f"Error: {e}")

def calcular_perfil_i():
    # CASO B - PERFIL I (Asegurando punto i)
    print("\n   CÁLCULO DE ESFUERZOS: CASO B (PERFIL I)")
    mx, my = 100.0, 50.0
    try:
        b = float(input("Ingrese base b (m): "))
        h = float(input("Ingrese altura h (m): "))
        t = float(input("Ingrese espesor t (m): "))

        a1, x1, y1 = b * t, 0, (h / 2) - (t / 2)
        a2, x2, y2 = t * (h - 2*t), 0, 0
        a3, x3, y3 = b * t, 0, -((h / 2) - (t / 2))

        area_total = a1 + a2 + a3
        cx, cy = (a1*x1 + a2*x2 + a3*x3) / area_total, (a1*y1 + a2*y2 + a3*y3) / area_total

        ix = ((b * t**3 / 12) + a1 * (y1 - cy)**2) + ((t * (h - 2*t)**3 / 12) + a2 * (y2 - cy)**2) + ((b * t**3 / 12) + a3 * (y3 - cy)**2)
        iy = ((t * b**3 / 12) + a1 * (x1 - cx)**2) + (((h - 2*t) * t**3 / 12) + a2 * (x2 - cx)**2) + ((t * b**3 / 12) + a3 * (x3 - cx)**2)

        puntos = {
            'a': (-b/2, -h/2), 'b': (0, -h/2), 'c': (b/2, -h/2),
            'd': (-b/2, -(h-2*t)/2), 'e': (-t/2, -(h-2*t)/2), 'f': (t/2, -(h-2*t)/2),
            'g': (b/2, -(h-2*t)/2), 'h': (-t/2, 0), 'i': (t/2, 0),
            'j': (-b/2, (h-2*t)/2), 'k': (-t/2, (h-2*t)/2), 'l': (t/2, (h-2*t)/2),
            'm': (b/2, (h-2*t)/2), 'n': (-b/2, h/2), 'ñ': (0, h/2), 'o': (b/2, h/2)
        }

        print(" RESULTADOS GEOMÉTRICOS")
        print(f"Centroide: Cx = {cx}, Cy = {cy}")
        print(f"Inercias:  Ix = {ix}, Iy = {iy}")
        
        print(f"\n{'Punto':<6} | {'Dist X':<15} | {'Dist Y':<15} | {'Total (Pa)':<15} | {'Estado'}")
        print("-" * 75)
        for p, coord in puntos.items():
            dx, dy = coord[0] - cx, coord[1] - cy
            sigma = ((-mx * dy) / ix) + ((-my * dx) / iy)
            estado = "TENSIÓN" if sigma > 0 else "COMPRESIÓN"
            print(f"{p:<6} | {dx:>15.6f} | {dy:>15.6f} | {sigma:>15.2f} | {estado}")
    except Exception as e: print(f"Error: {e}")

def calcular_perfil_circular():
    # CASO C - CIRCULAR HUECO
    print("\n   CÁLCULO DE ESFUERZOS: CASO C (CIRCULAR HUECO)")
    mx, my = 100.0, 50.0
    try:
        r_int = float(input("Ingrese radio int (m): "))
        r_ext = float(input("Ingrese radio ext (m): "))

        cx, cy = 0.0, 0.0
        ix = (math.pi * (r_ext**4 - r_int**4)) / 4
        iy = ix

        puntos = {
            'a': (0, -r_ext), 'b': (0, -r_int), 'c': (-r_ext, 0), 'd': (-r_int, 0),
            'e': (r_int, 0), 'f': (r_ext, 0), 'g': (0, r_int), 'h': (0, r_ext)
        }

        print(" RESULTADOS GEOMÉTRICOS")
        print(f"Centroide: Cx = {cx}, Cy = {cy}")
        print(f"Inercias:  Ix = {ix}, Iy = {iy}")

        print(f"\n{'Punto':<6} | {'Dist X':<15} | {'Dist Y':<15} | {'Total (Pa)':<15} | {'Estado'}")
        print("-" * 75)
        for p, coord in puntos.items():
            dx, dy = coord[0] - cx, coord[1] - cy
            total = ((-mx * dy) / ix) + ((-my * dx) / iy)
            estado = "TENSIÓN" if total > 0 else "COMPRESIÓN"
            print(f"{p:<6} | {dx:>15.6f} | {dy:>15.6f} | {total:>15.2f} | {estado}")
    except Exception as e: print(f"Error: {e}")

def menu():
    mostrar_introduccion()
    while True:
        print("\n MENÚ DE SELECCIÓN")
        print("1. Caso A (Perfil L)")
        print("2. Caso B (Perfil I)")
        print("3. Caso C (Circular Hueco)")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1': calcular_perfil_l()
        elif opcion == '2': calcular_perfil_i()
        elif opcion == '3': calcular_perfil_circular()
        elif opcion == '4': 
            print("Finalizando programa..."); break
        else: print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
