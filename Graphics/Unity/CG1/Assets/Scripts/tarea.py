# Programa para generar un archivo .obj de una rueda de carro
# Cristina González - A01025667
import math

# Función para generar los vertices de la rueda que recibe como parámetroos el número de lados, el radio y el ancho
def generateVertices(numSides, radius, width):
    vertices = [] 
    for i in range(2): # Bucle para generar los vertices de la cara superior e inferior
        widthOff = round(-width / 2, 5) if i == 1 else round(width / 2, 5) # Se calcula el ancho de la cara
        vertices.append([widthOff, 0, 0]) # Se agrega el origen de la cara
        for j in range(numSides): # Bucle para generar los vertices de la cara
            y = round(radius * math.sin(math.radians(360 / numSides * (j + 1))), 5) 
            z = round(radius * math.cos(math.radians(360 / numSides * (j + 1))), 5)
            vertices.append([widthOff, y, z])
    return vertices

# Función para calcular las caras de la rueda que recibe como parámetro el número de lados
def generateFaces(numSides):
    faces = []
    for i in range(numSides): # Bucle para generar las caras de la rueda
        if i < numSides - 1: # Se verifica si es el último elemento 
            faces.append([1, 3 + i, 2 + i])
            faces.append([numSides + 2, numSides + 3 + i, numSides + 4 + i])
            faces.append([2 + i, 3 + i, numSides + 3 + i])
            faces.append([3 + i, numSides + 4 + i, numSides + 3 + i])
        else: # Se conecta el último elemento con el primero
            faces.append([1, 2, 2 + i])
            faces.append([numSides + 2, numSides + 3 + i, numSides + 3])
            faces.append([2 + i, 2, numSides + 3 + i])
            faces.append([2, numSides + 3, numSides + 3 + i])
    return faces

# Función para calcular las normales de la rueda que recibe como parámetros los vertices, el índice del primer vértice, el índice del segundo vértice y el índice del tercer vértice
def findNormal(vertices, i, j, z):
    A = [vertices[j][0] - vertices[i][0], # Se calcula el vector A
         vertices[j][1] - vertices[i][1],
         vertices[j][2] - vertices[i][2]]
    B = [vertices[z][0] - vertices[i][0], # Se calcula el vector B
         vertices[z][1] - vertices[i][1],
         vertices[z][2] - vertices[i][2]]
    w = [A[1] * B[2] - A[2] * B[1], # Se calcula el vector normal
         A[2] * B[0] - A[0] * B[2],
         A[0] * B[1] - A[1] * B[0]]
    return [round(w[0], 5), round(w[1], 5), round(w[2], 5)]

# Función para generar las normales de la rueda que recibe como parámetros los vertices y el número de lados
def generateNormals(vertices, numSides):
    normals = []
    for i in range(numSides): # Bucle para generar las normales de la rueda
        if i < numSides - 1: # Se verifica si es el último elemento
            normals.append(findNormal(vertices, 0, i + 2, i + 1))
            normals.append(findNormal(vertices, numSides + 1, numSides + 2 + i, numSides + 3 + i))
            normals.append(findNormal(vertices, 1 + i, 2 + i, numSides + 2 + i))
            normals.append(findNormal(vertices, 2 + i, numSides + 3 + i, numSides + 2 + i))
        else: # Se conecta el último elemento con el primero
            normals.append(findNormal(vertices, 0, 1, 1 + i))
            normals.append(findNormal(vertices, numSides + 1, numSides + 2 + i, numSides + 2))
            normals.append(findNormal(vertices, 1 + i, 1, numSides + 2 + i))
            normals.append(findNormal(vertices, 1, numSides + 2, numSides + 2 + i))
    return normals

# Función para general el archivo .obj de la rueda que recibe como parámetros los vertices, el número de lados y el path del archivo
def generateFile(vertices, numSides, filePath):
    normals = generateNormals(vertices, numSides) # Se calculan las normales
    faces = generateFaces(numSides) # Se calculan las caras
    output = []
    for vertex in vertices: # Se agregan los vertices al archivo
        output.append(f"v {vertex[0]:.5f} {vertex[1]:.5f} {vertex[2]:.5f}\n")
    output.append("\n")
    for normal in normals: # Se agregan las normales al archivo
        output.append(f"vn {normal[0]:.5f} {normal[1]:.5f} {normal[2]:.5f}\n")
    output.append("\n")
    for i in range(len(faces)): # Se agregan las caras al archivo
        output.append(f"f {faces[i][0]}//{i + 1} {faces[i][1]}//{i + 1} {faces[i][2]}//{i + 1}\n")
    with open(filePath, "w") as file:
        file.writelines(output) # Se escribe el archivo


numSides = int(input("Ingrese la cantidad de lados para la rueda: ") or 8) # Se pide la cantidad de lados y si no se ingresa nada se asigna 8
if not 4 <= numSides <= 360: # Se verifica que la cantidad de lados sea válida
    print("La cantidad de lados debe ser entre 3 y 360.")
    exit()
radius = float(input("Ingrese el radio de la rueda: ") or 1) # Se pide el radio y si no se ingresa nada se asigna 1
width = float(input("Ingrese el ancho de la rueda: ") or 0.5) # Se pide el ancho y si no se ingresa nada se asigna 0.5
vertices = generateVertices(numSides, radius, width) # Se calculan los vertices
generateFile(vertices, numSides, "./rueda.obj") # Se genera el archivo


