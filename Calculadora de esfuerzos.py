import math

def mostrar_introduccion():
    print("      ALGORITMO PARA EL CÁLCULO DE ESFUERZOS NORMALES")
    print("Este programa calcula las propiedades geométricas")
    print("(centroide e inercia) y el esfuerzo normal total en distintos")
    print("puntos de análisis para tres tipos de secciones transversales.")
    print("Muestra si cada punto se encuentra en tensión o compresión.")

def imprimir_resultados(cx, cy, ix, iy, puntos, mx, my):
    """Función unificada con columna de Estado (Tensión/Compresión)"""
    print(f"\n--- RESULTADOS GEOMÉTRICOS ---")
    print(f"Centroide: Cx = {cx} m")
    print(f"Centroide: Cy = {cy} m")
    print(f"Inercias:  Ix = {ix} m^4")
    print(f"Inercias:  Iy = {iy} m^4")
    
    print(f"\n{'Punto':<6} | {'Dist X':<15} | {'Dist Y':<15} | {'Total (Pa)':<18} | {'Estado'}")
    print("-" * 85)
    
    for p, coord in puntos.items():
        dx = coord[0] - cx
        dy = coord[1] - cy
        
        s_mx = (-mx * dy) / ix
        s_my = (-my * dx) / iy
        total = s_mx + s_my
        
      
        estado = "TENSIÓN" if total > 0 else "COMPRESIÓN"
        if abs(total) < 1e-12: estado = "NEUTRO"
        
        print(f"{p:<6} | {dx:>15.6f} | {dy:>15.6f} | {total:>18.4f} | {estado}")

def caso_a():
    print("\n--- CONFIGURACIÓN: CASO A (PERFIL L) ---")
    b = float(input("Ingrese base b (m): "))
    h = float(input("Ingrese altura h (m): "))
    t = float(input("Ingrese espesor t (m): "))
    mx, my = 100.0, 50.0

    a1, x1, y1 = b * t, b / 2, t / 2
    a2, x2, y2 = t * (h - t), t / 2, t + (h - t) / 2

    at = a1 + a2
    cx, cy = (a1*x1 + a2*x2) / at, (a1*y1 + a2*y2) / at

    ix = ((b*t**3)/12 + a1*(y1-cy)**2) + ((t*(h-t)**3)/12 + a2*(y2-cy)**2)
    iy = ((t*b**3)/12 + a1*(x1-cx)**2) + (((h-t)*t**3)/12 + a2*(x2-cx)**2)

    puntos = {
        'a': (0, h), 'b': (t, h), 'c': (0, t), 'd': (t, t),
        'g': (b, t), 'h': (0, 0), 'i': (t, 0), 'j': (b, 0)
    }
    imprimir_resultados(cx, cy, ix, iy, puntos, mx, my)

def caso_b():
    print("\n--- CONFIGURACIÓN: CASO B (PERFIL I) ---")
    b = float(input("Ingrese base b (m): "))
    h = float(input("Ingrese altura h (m): "))
    t = float(input("Ingrese espesor t (m): "))
    mx, my = 100.0, 50.0

    cx, cy = 0.0, 0.0
    a_patin, a_alma = b * t, t * (h - 2*t)
    y_patin = (h/2) - (t/2)
    
    ix = 2*((b*t**3)/12 + a_patin*y_patin**2) + (t*(h-2*t)**3)/12
    iy = 2*((t*b**3)/12) + ((h-2*t)*t**3)/12

    puntos = {
        'a': (-b/2, -h/2), 'b': (0, -h/2), 'c': (b/2, -h/2),
        'd': (-b/2, -(h-2*t)/2), 'e': (-t/2, -(h-2*t)/2), 'f': (t/2, -(h-2*t)/2),
        'g': (b/2, -(h-2*t)/2), 'h': (-t/2, 0), 'i': (t/2, 0),
        'j': (-b/2, (h-2*t)/2), 'k': (-t/2, (h-2*t)/2), 'l': (t/2, (h-2*t)/2),
        'm': (b/2, (h-2*t)/2), 'n': (-b/2, h/2), 'ñ': (0, h/2), 'o': (b/2, h/2)
    }
    imprimir_resultados(cx, cy, ix, iy, puntos, mx, my)

def caso_c():
    print("\n--- CONFIGURACIÓN: CASO C (CIRCULAR HUECO) ---")
    r_int = float(input("Ingrese radio interior (m): "))
    r_ext = float(input("Ingrese radio exterior (m): "))
    mx, my = 100.0, 50.0

    cx, cy = 0.0, 0.0
    ix = (math.pi * (r_ext**4 - r_int**4)) / 4
    iy = ix

    puntos = {
        'a': (0, -r_ext), 'b': (0, -r_int), 'c': (-r_ext, 0), 'd': (-r_int, 0),
        'e': (r_int, 0), 'f': (r_ext, 0), 'g': (0, r_int), 'h': (0, r_ext)
    }
    imprimir_resultados(cx, cy, ix, iy, puntos, mx, my)

def principal():
    mostrar_introduccion()
    while True:
        print("\nOpciones:")
        print("1. Caso A | 2. Caso B | 3. Caso C | 4. Salir")
        sel = input("Seleccione (1-4): ")
        if sel == '1': caso_a()
        elif sel == '2': caso_b()
        elif sel == '3': caso_c()
        elif sel == '4': break
        else: print("Error.")

if __name__ == "__main__":
    principal()
