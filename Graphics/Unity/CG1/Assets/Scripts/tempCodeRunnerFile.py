num_sides_input = input("¿Cuántos lados del círculo quiere? (Presione Enter para usar el valor predeterminado): ")

num_sides = int(num_sides_input) if num_sides_input else 8  # Define num_sides aquí

if num_sides_input and (num_sides < 4 or num_sides > 360):
    print("El número de lados debe estar entre 3 (excluido) y 360.")
    exit()

radius_input = input("¿De cuánto quiere que sea el radio de la llanta? (Presione Enter para usar el valor predeterminado): ")
width_input = input("¿De qué ancho quiere la llanta? (Presione Enter para usar el valor predeterminado): ")

radius = float(radius_input) if radius_input else 1
width = float(width_input) if width_input else 0.5

vertices = generate_vertices(num_sides, radius, width)
write_obj_file(vertices, num_sides, "./wheel.obj")