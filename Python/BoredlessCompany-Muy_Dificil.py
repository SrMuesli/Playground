destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil","Cairo, Egypt", "Madrid, Spain"]    # Destinos a los que se viaja.

attractions = [[] for destination in destinations]      # Esto crea "Arrays" vacíos por cada destino, así ahi se pueden guardar las atracciones.

test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]      # Viajero de ejemplo.

#   Esto es para comprobar en que posicion de index está la ciudad a la que quiere ir el viajero.
#   Ese index lo usaremos mas adelante <3

def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

#   Esto lo dejo comentado, porque no le veo mucho sentido que "exista" puesto que está pensado para usarse en "bases de datos"
#def get_traveler_location(traveler):
#    traveler_destination = traveler[1]
#    traveler_destination_index = get_destination_index(traveler_destination)
#    return traveler_destination_index

#   Esto es para añadir atracciones a los lugares de destino.
#   Las atracciones se añaden a la lista, en orden, dependiendo de "en que ciudad están esas atracciones"

def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
        attractions_for_destination = attractions[destination_index].append(attraction)
    except SyntaxError:
        return

add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])                             # Añade a "Los Angeles" la atraccion "Venice Beach" con la etiqueta de "playa"
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])       # Añade a "Paris" la atraccion "Arc de Triomphe"
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])                          # Añade a "Paris" la atraccion "the Louvre" con las etiquetas "museo" y "arte"
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])            # Añade a "Shanghai" la atraccion " Yu Garden""
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])                        # Añade a "Shanghai" la atraccion "Yuz Museum"
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]]) # Añade a "Shanghai" la atraccion "Oriental Pearl Tower"
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])                            # Añade a "Los Angeles" la atraccion "LACMA" etiquetado como "arte" y "museo"
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])                             # Añade a 
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
add_attraction("Madrid, Spain", ["el Prado", ["museum"]])
add_attraction("Madrid, Spain", ["Casa de Campo", ["natural park"]])
add_attraction("Madrid, Spain", ["el Retiro", ["natural park"]])
add_attraction("Madrid, Spain", ["Catedral de Santa María la Real de la Almudena", ["religious place"]])
add_attraction("Madrid, Spain", ["plaza de Toros de Las Ventas", ["bullring"]])
add_attraction("Madrid, Spain", ["Parque Warner Madrid", ["amusement park"]])

#   Esto es para buscar atracciones con la etiqueta que busca el cliente
#   Busca en la lista de atracciones que atracciones hay con index de la ciudad que quiere ir
#   Después busca cuales tienen la misma etiqueta que lo que busca el cliente
#   Y añade todo eso a una "lista" temporal, la cual será devuelta a quien llame esta funcion
#   Por ejemplo, si el cliente busca "arte" en "Los Angeles" esto le tiene que decir que lo que busca es "LACMA"

def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    for attraction in attractions_in_city:
        possible_attraction = attraction
        attraction_tags = attraction[1]
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])
    return attractions_with_interest

#   Aqui coge los datos del cliente, y llama a las funciones necesarias para encontrar las atracciones que el cliente busca
#   Una vez tiene los datos de lo que busca el cliente, lo que hace es construir una frase con la que mostrar esos datos al cliente

def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": "
    for i in range(len(traveler_attractions)):
        if traveler_attractions[-1] == traveler_attractions[i]:
            interests_string += "the " + traveler_attractions[i] + "."
        else:
            interests_string += "the " + traveler_attractions[i] + ", "
    return interests_string

smills_spain = get_attractions_for_traveler(["Claudia Ferreira", "Madrid, Spain", ["natural park"]])

print(smills_spain)