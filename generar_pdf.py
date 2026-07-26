from fpdf import FPDF

# Crear PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Título principal
pdf.set_font("Helvetica", "B", 20)
pdf.set_text_color(0, 51, 102)
pdf.cell(0, 15, "NOTACION BIG-O", ln=True, align="C")
pdf.ln(5)

# Subtítulo
pdf.set_font("Helvetica", "I", 12)
pdf.set_text_color(100, 100, 100)
pdf.cell(0, 10, "Guia Completa de Complejidad Temporal", ln=True, align="C")
pdf.ln(3)

# Sección 1: Definición
pdf.set_font("Helvetica", "B", 14)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 10, "Que es Big-O?", ln=True)

pdf.set_font("Helvetica", "", 11)
pdf.multi_cell(0, 5, "La notacion Big-O expresa como el tiempo de ejecucion o la memoria de una operacion crece relativo al tamaño de la entrada (n).\n\nDescribe el PEOR CASO de rendimiento.")
pdf.ln(3)

# Tabla de complejidades
pdf.set_font("Helvetica", "B", 12)
pdf.set_text_color(255, 255, 255)
pdf.set_fill_color(0, 51, 102)
pdf.cell(30, 8, "NOTACION", border=1, fill=True)
pdf.cell(40, 8, "NOMBRE", border=1, fill=True)
pdf.cell(0, 8, "EJEMPLO", border=1, fill=True, ln=True)

pdf.set_font("Helvetica", "", 10)
pdf.set_text_color(0, 0, 0)

data = [
    ("O(1)", "Constante", "Acceder a elemento por indice"),
    ("O(log n)", "Logaritmica", "Busqueda binaria"),
    ("O(n)", "Lineal", "Busqueda secuencial"),
    ("O(n log n)", "Lineal-logaritmica", "Merge sort"),
    ("O(n^2)", "Cuadratica", "Bucles anidados"),
]

for notation, name, example in data:
    pdf.cell(30, 7, notation, border=1)
    pdf.cell(40, 7, name, border=1)
    pdf.cell(0, 7, example, border=1, ln=True)

pdf.ln(5)

# Detalles por complejidad
complexities = [
    ("O(1) - CONSTANTE", "Tiempo siempre igual sin importar el tamaño de entrada.\nEl mas eficiente.\n\nEjemplos:\n- lista[0] (Acceso directo)\n- len(lista) (Obtener largo)\n- diccionario['clave'] (Hash map)"),
    
    ("O(log n) - LOGARITMICA", "El tiempo crece logaritmicamente. Muy eficiente\nincluso con datos grandes.\n\nEjemplos:\n- Busqueda binaria en lista ordenada\n- Operaciones en arboles balanceados\n- Con 1M elementos aprox. 20 operaciones"),
    
    ("O(n) - LINEAL", "El tiempo crece proporcionalmente al tamaño\nde entrada.\n\nEjemplos:\n- for x in lista: print(x)\n- Encontrar maximo/minimo\n- Busqueda en lista sin ordenar"),
    
    ("O(n log n) - LINEAL-LOGARITMICA", "Tipico en ordenamientos eficientes.\n\nEjemplos:\n- Merge Sort\n- Quick Sort (promedio)\n- Con 1M elementos aprox. 20M operaciones"),
    
    ("O(n^2) - CUADRATICA", "El tiempo crece exponencialmente con n.\nMUY INEFICIENTE.\n\nEjemplos:\n- Bubble sort\n- Bucles anidados\n- Con 1M elementos 1 BILLON de operaciones!"),
]

for title, desc in complexities:
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 8, title, ln=True)
    
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(0, 0, 0)
    pdf.multi_cell(0, 4, desc)
    pdf.ln(2)

# Nueva página para ejemplos de código
pdf.add_page()
pdf.set_font("Helvetica", "B", 16)
pdf.set_text_color(0, 51, 102)
pdf.cell(0, 12, "EJEMPLOS DE CODIGO", ln=True)
pdf.ln(5)

# Ejemplo 1: O(1)
pdf.set_font("Helvetica", "B", 11)
pdf.set_text_color(0, 51, 102)
pdf.cell(0, 8, "Ejemplo O(1) - Acceso Constante", ln=True)
pdf.set_font("Helvetica", "", 9)
pdf.set_text_color(80, 80, 80)
pdf.multi_cell(0, 4, "lista = [1, 2, 3, 4, 5]\nprint(lista[0])  # O(1)\ndiccionario['clave'] = valor  # O(1)")
pdf.ln(3)

# Ejemplo 2: O(n)
pdf.set_font("Helvetica", "B", 11)
pdf.set_text_color(0, 51, 102)
pdf.cell(0, 8, "Ejemplo O(n) - Busqueda Lineal", ln=True)
pdf.set_font("Helvetica", "", 9)
pdf.set_text_color(80, 80, 80)
pdf.multi_cell(0, 4, "def buscar(lista, objetivo):\n    for elemento in lista:\n        if elemento == objetivo:\n            return True\n    return False")
pdf.ln(3)

# Ejemplo 3: O(n²)
pdf.set_font("Helvetica", "B", 11)
pdf.set_text_color(0, 51, 102)
pdf.cell(0, 8, "Ejemplo O(n^2) - EVITAR", ln=True)
pdf.set_font("Helvetica", "", 9)
pdf.set_text_color(80, 80, 80)
pdf.multi_cell(0, 4, "def comparar_pares(lista):\n    for i in lista:\n        for j in lista:\n            print(i, j)")
pdf.ln(3)

# Tabla comparativa
pdf.ln(5)
pdf.set_font("Helvetica", "B", 11)
pdf.set_text_color(0, 51, 102)
pdf.cell(0, 8, "Comparativa de Rendimiento", ln=True)

pdf.set_font("Helvetica", "B", 9)
pdf.set_text_color(255, 255, 255)
pdf.set_fill_color(0, 51, 102)
pdf.cell(25, 6, "n=1000", border=1, fill=True)
pdf.cell(25, 6, "O(1)", border=1, fill=True)
pdf.cell(25, 6, "O(logn)", border=1, fill=True)
pdf.cell(25, 6, "O(n)", border=1, fill=True)
pdf.cell(25, 6, "O(nlogn)", border=1, fill=True)
pdf.cell(0, 6, "O(n^2)", border=1, fill=True, ln=True)

pdf.set_font("Helvetica", "", 9)
pdf.set_text_color(0, 0, 0)
pdf.cell(25, 6, "Ops", border=1)
pdf.cell(25, 6, "1", border=1)
pdf.cell(25, 6, "~10", border=1)
pdf.cell(25, 6, "1,000", border=1)
pdf.cell(25, 6, "~10,000", border=1)
pdf.cell(0, 6, "1,000,000", border=1, ln=True)

pdf.ln(5)
pdf.set_font("Helvetica", "B", 12)
pdf.set_text_color(255, 0, 0)
pdf.cell(0, 8, "REGLA DE ORO: Elige O(1) u O(log n) cuando sea posible.", ln=True)
pdf.set_font("Helvetica", "", 10)
pdf.set_text_color(200, 0, 0)
pdf.multi_cell(0, 5, "Evita O(n^2) especialmente con datos grandes.\nLa diferencia de rendimiento es ENORME.")

# Nueva página - Conclusiones
pdf.add_page()
pdf.set_font("Helvetica", "B", 16)
pdf.set_text_color(0, 51, 102)
pdf.cell(0, 12, "CONCLUSION Y RECOMENDACIONES", ln=True)
pdf.ln(5)

pdf.set_font("Helvetica", "", 11)
pdf.set_text_color(0, 0, 0)
pdf.multi_cell(0, 5, "1. PRIORIZA SIEMPRE O(1):\nUsa acceso directo cuando sea posible (arrays con indice, hash maps).\n\n2. BUSQUEDA BINARIA (O(log n)):\nSi tienes datos ordenados, busqueda binaria es excelente.\n\n3. OPERACIONES LINEALES (O(n)):\nAceptable para procesar todos los datos una sola vez.\n\n4. EVITA O(n^2):\nBucles anidados son mala idea con datos grandes.\nUsa algoritmos mas eficientes (merge sort, quick sort).\n\n5. RECUERDA:\nEl tamaño de entrada IMPORTA:\n- 10 elementos: casi no hay diferencia\n- 1,000 elementos: diferencia notable\n- 1,000,000 elementos: O(n^2) es IMPOSIBLE")

# Guardar PDF
pdf.output("Big_O_Guia_Completa.pdf")
print("✓ PDF creado exitosamente: Big_O_Guia_Completa.pdf")
