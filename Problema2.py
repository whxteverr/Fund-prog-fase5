# Matriz del menú: [Nombre del producto, Categoría, Precio base]
menu = [
    ["Bandeja paisa",      "Platos fuertes", 38000],
    ["Sopa de mondongo",   "Sopas",          22000],
    ["Churrasco",          "Platos fuertes", 45000],
    ["Limonada de coco",   "Bebidas",         9000],
    ["Tres leches",        "Postres",        14000],
    ["Ajiaco",             "Sopas",          28000],
    ["Jugo natural",       "Bebidas",         7000],
]

# Parámetros de la promoción
CATEGORIA_OBJETIVO = "Platos fuertes"
UMBRAL = 40000
DESCUENTO = 0.15


def calcular_precio_final(precio_base, categoria,
                          categoria_objetivo=CATEGORIA_OBJETIVO,
                          umbral=UMBRAL,
                          descuento=DESCUENTO):
    """Devuelve el precio final aplicando el descuento si el producto
    pertenece a la categoría objetivo Y su precio base supera el umbral."""
    if categoria == categoria_objetivo and precio_base > umbral:
        return precio_base * (1 - descuento)
    return precio_base


def mostrar_menu(matriz):
    print(f"{'Producto':<20}{'Precio base':>14}{'Precio final':>16}")
    print("-" * 50)
    for nombre, categoria, precio_base in matriz:
        precio_final = calcular_precio_final(precio_base, categoria)
        marca = "  (promo 15%)" if precio_final < precio_base else ""
        print(f"{nombre:<20}${precio_base:>12,.0f}${precio_final:>14,.0f}{marca}")


mostrar_menu(menu)