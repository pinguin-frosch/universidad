db.peliculas.insertMany([
    {
        "titulo": "Cadena perpetua",
        "resumen": "Andy Dufresne es encarcelado por matar a su esposa y al amante de esta. Tras una dura adaptación, intenta mejorar las condiciones de la prisión y dar esperanza a sus compañeros.",
        "generos": ["Drama"],
        "directores": {
            "cantidad": 1,
            "lista": ["Frank Darabont"]
        },
        "fecha_de_lanzamiento": new Date(1995, 2, 24),
        "actores": {
            "cantidad": 6,
            "lista": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler", "Clancy Brown", "Gil Bellows"]
        },
        "comentarios": 0
    },
    {
        "titulo": "El padrino",
        "resumen": "El envejecido patriarca de una dinastía del crimen organizado en la ciudad de Nueva York de la posguerra transfiere el control de su imperio clandestino a su reacio hijo menor.",
        "generos": ["Crimen", "Drama"],
        "directores": {
            "cantidad": 1,
            "lista": ["Francis Ford Coppola"]
        },
        "fecha_de_lanzamiento": new Date(1972, 10, 20),
        "actores": {
            "cantidad": 5,
            "lista": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton", "Richard S. Castellano"]
        },
        "comentarios": 0
    },
    {
        "titulo": "El caballero oscuro",
        "resumen": "Cuando la amenaza conocida como el Joker causa estragos y el caos en Gotham City, Batman debe aceptar una de las mayores pruebas psicológicas y físicas para luchar contra la injusticia.",
        "generos": ["Acción", "Crimen", "Drama", "Suspenso"],
        "directores": {
            "cantidad": 1,
            "lista": ["Christopher Nolan"]
        },
        "fecha_de_lanzamiento": new Date(2008, 8, 13),
        "actores": {
            "cantidad": 4,
            "lista": ["Christian Bale", "Heath Ledger", "Aaron Eckhart", "Michael Caine"]
        },
        "comentarios": 0
    },
    // TODO: aumentar los comentarios
    {
        "titulo": "El padrino: parte II",
        "resumen": "Se retratan los inicios de la vida y la carrera de Vito Corleone en el Nueva York de los años 20, mientras su hijo, Michael, amplía y refuerza su control sobre el sindicato del crimen familiar.",
        "generos": ["Crimen", "Drama"],
        "directores": {
            "cantidad": 1,
            "lista": ["Franis Ford Coppola"]
        },
        "fecha_de_lanzamiento": new Date(1975, 10, 13),
        "actores": {
            "cantidad": 4,
            "lista": ["Al Pacino", "Robert De Niro", "Robert Duvall", "Diane Keaton"]
        },
        "comentarios": 0
    },
    {
        "titulo": "12 hombres sin piedad",
        "resumen": "Un miembro del jurado trata de evitar un error judicial obligando al resto del jurado a reconsiderar las pruebas.",
        "generos": ["Crimen", "Drama"],
        "directores": {
            "cantidad": 1,
            "lista": ["Sidney Lumet"]
        },
        "fecha_de_lanzamiento": new Date(1957, 4, 10),
        "actores": {
            "cantidad": 8,
            "lista": ["Henry Fonda", "Lee J. Cobb", "Martin Balsam", "John Fiedler", "E.G. Marshall", "Jack Klugman", "Edward Binns", "Jack Warden"]
        },
        "comentarios": 0
    },
    {
        "titulo": "La lista de Schindler",
        "resumen": "En la Polonia ocupada por los alemanes durante la Segunda Guerra Mundial, el industrial Oskar Schindler se preocupa por sus trabajadores judíos tras presenciar su persecución por los nazis.",
        "generos": ["Biografía", "Drama", "Historia"],
        "directores": {
            "cantidad": 1,
            "lista": ["Steven Spielberg"]
        },
        "fecha_de_lanzamiento": new Date(1994, 3, 4),
        "actores": {
            "cantidad": 5,
            "lista": ["Liam Neeson", "Ralph Fiennes", "Ben Kingsley", "Caroline Goodall", "Jonathan Sagall"]
        },
        "comentarios": 0
    },
    {
        "titulo": "El señor de los anillos: el retorno del rey",
        "resumen": "Gandalf y Aragorn lideran el mundo de los hombres contra la armada de Sauron para distraer su atención de Frodo y Sam, quienes se aproximan al Monte del Destino con el Anillo Único.",
        "generos": ["Acción", "Aventura", "Drama", "Fantasía"],
        "directores": {
            "cantidad": 1,
            "lista": ["Peter Jackson"]
        },
        "fecha_de_lanzamiento": new Date(2003, 12, 17),
        "actores": {
            "cantidad": 5,
            "lista": ["Elijah Wood", "Viggo Mortensen", "Ian McKellen", "Orlando Bloom", "Sean Astin"]
        },
        "comentarios": 0
    },
    {
        "titulo": "Pulp Fiction",
        "resumen": "Las vidas de dos mafiosos, un boxeador, la esposa de un gánster y un par de bandidos se entrelazan en cuatro historias de violencia y redención.",
        "generos": ["Crimen", "Drama"],
        "directores": {
            "cantidad": 1,
            "lista": ["Quentin Tarantino"]
        },
        "fecha_de_lanzamiento": new Date(1995, 1, 13),
        "actores": {
            "cantidad": 8,
            "lista": ["John Travolta", "Uma Thurman", "Samuel L. Jackson", "Bruce Willis", "Tim Roth", "Amanda Plummer", "Laura Lovelace", "Phil LaMarr"]
        },
        "comentarios": 0
    },
    {
        "titulo": "El señor de los anillos: la comunidad del anillo",
        "resumen": "Un hobbit de la Comarca y ocho compañeros emprenden un viaje para destruir el poderoso Anillo Único y salvar la Tierra Media del Señor Oscuro Sauron.",
        "generos": ["Acción", "Aventura", "Drama", "Fantasía"],
        "directores": {
            "cantidad": 1,
            "lista": ["Peter Jackson"]
        },
        "fecha_de_lanzamiento": new Date(2001, 12, 19),
        "actores": {
            "cantidad": 5,
            "lista": ["Elijah Wood", "Viggo Mortensen", "Ian McKellen", "Orlando Bloom", "Sean Astin"]
        },
        "comentarios": 0
    },
    {
        "titulo": "El bueno, el feo y el malo",
        "resumen": "Durante la Guerra de Secesión, tres cazarrecompensas se lanzan a la búsqueda de un tesoro que ninguno puede localizar sin la ayuda de los otros dos.",
        "generos": ["Aventura", "Del oeste"],
        "directores": {
            "cantidad": 1,
            "lista": ["Sergio Leone"]
        },
        "fecha_de_lanzamiento": new Date(1968, 8, 7),
        "actores": {
            "cantidad": 5,
            "lista": ["Clint Eastwood", "Eli Wallach", "Lee Van Cleef", "Aldo Giuffrè", "Luigi Pistilli"]
        },
        "comentarios": 0
    },
    // TODO: aumentar los comentarios
    {
        "titulo": "Forrest Gump",
        "resumen": "Las presidencias de Kennedy y Johnson, los acontecimientos de Vietnam, el Watergate y otros eventos históricos se desarrollan a través de la perspectiva de un hombre de Alabama con un coeficiente intelectual de 75.",
        "generos": ["Drama", "Romance"],
        "directores": {
            "cantidad": 1,
            "lista": ["Robert Zemeckis"]
        },
        "fecha_de_lanzamiento": new Date(1994, 9, 23),
        "actores": {
            "cantidad": 6,
            "lista": ["Tom Hanks", "Robin Wright", "Gary Sinise", "Sally Field", "Rebecca Williams", "Michael Conner Humphreys"]
        },
        "comentarios": 0
    },
    {
        "titulo": "El club de la lucha",
        "resumen": "Un oficinista insomne y un desentendido fabricante de jabones forman un club de lucha clandestino que se convierte en mucho más.",
        "generos": ["Drama"],
        "directores": {
            "cantidad": 1,
            "lista": ["David Fincher"]
        },
        "fecha_de_lanzamiento": new Date(1999, 11, 5),
        "actores": {
            "cantidad": 8,
            "lista": ["Brad Pitt", "Edward Norton", "Meat Loaf", "Zach Grenier", "Richmond Arquette", "David Andrews", "George Maguire", "Eugenie Bondurant"]
        },
        "comentarios": 0
    },
    {
        "titulo": "Origen",
        "resumen": "A un ladrón que roba secretos corporativos a través del uso de la tecnología de compartir sueños, se le da la tarea de implantar una idea en la mente de un jefe de una gran empresa.",
        "generos": ["Acción", "Aventura", "Ciencia ficción", "Suspenso"],
        "directores": {
            "cantidad": 1,
            "lista": ["Christopher Nolan"]
        },
        "fecha_de_lanzamiento": new Date(2010, 8, 6),
        "actores": {
            "cantidad": 4,
            "lista": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page", "Ken Watanabe"]
        },
        "comentarios": 0
    },
    {
        "titulo": "El señor de los anillos: las dos torres",
        "resumen": "Mientras Frodo y Sam se acercan a Mordor con la ayuda del astuto Gollum, la comunidad dividida se enfrenta al nuevo aliado de Sauron, Saruman, y a sus hordas de Isengard.",
        "generos": ["Acción", "Aventura", "Drama", "Fantasía"],
        "directores": {
            "cantidad": 1,
            "lista": ["Peter Jackson"]
        },
        "fecha_de_lanzamiento": new Date(2002, 12, 18),
        "actores": {
            "cantidad": 5,
            "lista": ["Elijah Wood", "Viggo Mortensen", "Ian McKellen", "Orlando Bloom", "Sean Astin"]
        },
        "comentarios": 0
    },
    {
        "titulo": "El imperio contraataca",
        "resumen": "Tras ser brutalmente dominados los rebeldes por el Imperio en el planeta helado Hoth, Luke Skywalker comienza su entrenamiento jedi con Yoda, mientras sus amigos son perseguidos por Darth Vader y el cazarrecompensas Boba Fett.",
        "generos": ["Acción", "Aventura", "Fantasía", "Ciencia ficción"],
        "directores": {
            "cantidad": 1,
            "lista": ["Irvin Kershner"]
        },
        "fecha_de_lanzamiento": new Date(1980, 10, 3),
        "actores": {
            "cantidad": 6,
            "lista": ["Mark Hamill", "Harrison Ford", "Carrie Fisher", "Billy Dee Williams", "Anthony Daniels", "David Prowse"]
        },
        "comentarios": 0
    },
    {
        "titulo": "Matrix",
        "resumen": "Cuando una bella desconocida lleva al hacker Neo a un inframundo prohibido, descubre la impactante verdad: la vida que conoce es un elaborado engaño de una ciberinteligencia malvada.",
        "generos": ["Acción", "Ciencia ficción"],
        "directores": {
            "cantidad": 2,
            "lista": ["Lana Wachowski", "Lilly Wachowski"]
        },
        "fecha_de_lanzamiento": new Date(1999, 6, 23),
        "actores": {
            "cantidad": 4,
            "lista": ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss", "Hugo Weaving"]
        },
        "comentarios": 0
    },
    {
        "titulo": "Uno de los nuestros",
        "resumen": "La historia de Henry Hill y su vida en la mafia, abarcando su relación con su esposa Karen Hill y sus socios mafiosos Jimmy Conway y Tommy DeVito en el sindicato del crimen italoamericano.",
        "generos": ["Biografía", "Crimen", "Drama"],
        "directores": {
            "cantidad": 1,
            "lista": ["Martin Scorsese"]
        },
        "fecha_de_lanzamiento": new Date(1990, 10, 19),
        "actores": {
            "cantidad": 5,
            "lista": ["Robert De Niro", "Ray Liotta", "Joe Pesci", "Lorraine Bracco", "Paul Sorvino"]
        },
        "comentarios": 0
    },
    {
        "titulo": "Alguien voló sobre el nido del cuco",
        "resumen": "Un criminal alega locura para ser enviado a un centro de salud mental, donde se rebela contra la opresiva enfermera y moviliza a los pacientes, a quienes tienen atemorizados.",
        "generos": ["Drama"],
        "directores": {
            "cantidad": 1,
            "lista": ["Milos Forman"]
        },
        "fecha_de_lanzamiento": new Date(1990, 10, 19),
        "actores": {
            "cantidad": 4,
            "lista": ["Jack Nicholson", "Louise Fletcher", "Michael Berryman", "Peter Brocco"]
        },
        "comentarios": 0
    },
    {
        "titulo": "Seven",
        "resumen": "Dos detectives, un novato y un veterano, dan caza a un asesino en serie cuyo móvil son los siete pecados capitales.",
        "generos": ["Crimen", "Drama", "Misterio", "Suspenso"],
        "directores": {
            "cantidad": 1,
            "lista": ["David Fincher"]
        },
        "fecha_de_lanzamiento": new Date(1996, 1, 10),
        "actores": {
            "cantidad": 5,
            "lista": ["Morgan Freeman", "Brad Pitt", "Kevin Spacey", "Andrew Kevin Walker", "Daniel Zacapa"]
        },
        "comentarios": 0
    },
    {
        "titulo": "Los siete samuráis",
        "resumen": "Un pueblo pobre atacado por bandidos recluta a siete samuráis desempleados para que les ayuden a defenderse.",
        "generos": ["Acción", "Drama"],
        "directores": {
            "cantidad": 1,
            "lista": ["Akira Kurosawa"]
        },
        "fecha_de_lanzamiento": new Date(1954, 4, 26),
        "actores": {
            "cantidad": 4,
            "lista": ["Toshirô Mifune", "Takashi Shimura", "Keiko Tsushima", "Kamatari Fujiwara"]
        },
        "comentarios": 0
    },
    {
        "titulo": "Qué bello es vivir",
        "resumen": "Un ángel es enviado desde el cielo para ayudar a un hombre de negocios desesperadamente frustrado, mostrándole cómo habría sido la vida si él nunca hubiera existido.",
        "generos": ["Drama", "Familiar", "Fantasía", "Romance"],
        "directores": {
            "cantidad": 1,
            "lista": ["Frank Capra"]
        },
        "fecha_de_lanzamiento": new Date(1947, 1, 7),
        "actores": {
            "cantidad": 5,
            "lista": ["James Stewart", "Donna Reed", "Lionel Barrymore", "Thomas Mitchell", "Henry Travers"]
        },
        "comentarios": 0
    },
    {
        "titulo": "El silencio de los corderos",
        "resumen": "Una joven cadete del FBI busca la ayuda de un asesino caníbal y manipulador encarcelado con el fin de atrapar a otro asesino en serie, un loco que despelleja a sus víctimas.",
        "generos": ["Crimen", "Drama", "Suspenso"],
        "directores": {
            "cantidad": 1,
            "lista": ["Jonathan Demme"]
        },
        "fecha_de_lanzamiento": new Date(1991, 9, 6),
        "actores": {
            "cantidad": 5,
            "lista": ["Jodie Foster", "Anthony Hopkins", "Kasi Lemmons", "Scott Glenn", "Anthony Heald"]
        },
        "comentarios": 0
    },
    {
        "titulo": "Ciudad de dios",
        "resumen": "En un barrio pobre de Rio, los caminos de dos niños se cruzan mientras uno quiere ser fotógrafo y el otro capo.",
        "generos": ["Crimen", "Drama"],
        "directores": {
            "cantidad": 2,
            "lista": ["Fernando Meirelles", "Kátia Lund"],
        },
        "fecha_de_lanzamiento": new Date(2003, 1, 31),
        "actores": {
            "cantidad": 5,
            "lista": ["Alexandre Rodrigues", "Leandro Firmino", "Douglas Silva", "Jonathan Haagensen", "Seu Jorge"]
        },
        "comentarios": 0
    },
    {
        "titulo": "Salvar al soldado Ryan",
        "resumen": "Tras el desembarco de Normandía, un grupo de soldados estadounidenses cruza las líneas enemigas para rescatar a un paracaidista cuyos hermanos han muerto en combate.",
        "generos": ["Drama", "Bélico"],
        "directores": {
            "cantidad": 1,
            "lista": ["Steven Spielberg"],
        },
        "fecha_de_lanzamiento": new Date(1998, 9, 18),
        "actores": {
            "cantidad": 6,
            "lista": ["Tom Hanks", "Matt Damon", "Tom Sizemore", "Edward Burns", "Barry Pepper", "Adam Goldberg"]
        },
        "comentarios": 0
    },
    {
        "titulo": "La milla verde",
        "resumen": "Las vidas de los guardias del corredor de la muerte se ven afectadas por uno de sus reclusos: un hombre negro acusado de asesinato y violación de niños, pero que tiene un misterioso don.",
        "generos": ["Crimen", "Drama", "Fantasía", "Misterio"],
        "directores": {
            "cantidad": 1,
            "lista": ["Frank Darabont"],
        },
        "fecha_de_lanzamiento": new Date(2000, 2, 18),
        "actores": {
            "cantidad": 7,
            "lista": ["Tom Hanks", "Michael Clarke Duncan", "David Morse", "Bonnie Hunt", "James Cromwell", "Michael Jeter", "Graham Greene"]
        },
        "comentarios": 0
    },
    {
        "titulo": "Interstellar",
        "resumen": "Un equipo de exploradores viaja a través de un agujero de gusano en el espacio en un intento de garantizar la supervivencia de la humanidad.",
        "generos": ["Aventura", "Drama", "Ciencia ficción"],
        "directores": {
            "cantidad": 1,
            "lista": ["Christopher Nolan"],
        },
        "fecha_de_lanzamiento": new Date(2014, 11, 7),
        "actores": {
            "cantidad": 5,
            "lista": ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain", "Mackenzie Foy", "Ellen Burstyn"]
        },
        "comentarios": 0
    },
    {
        "titulo": "La guerra de las galaxias",
        "resumen": "Luke Skywalker une sus fuerzas con un caballero jedi, un piloto fanfarrón, un wookiee y dos droides para salvar a la galaxia de la estación espacial del Imperio, a la vez que intenta rescatar a la princesa Leia del malvado Darth Vader.",
        "generos": ["Acción", "Aventura", "Fantasía", "Ciencia ficción"],
        "directores": {
            "cantidad": 1,
            "lista": ["George Lucas"],
        },
        "fecha_de_lanzamiento": new Date(1977, 11, 7),
        "actores": {
            "cantidad": 6,
            "lista": ["Mark Hamill", "Harrison Ford", "Carrie Fisher", "Alec Guinness", "Peter Cushing", "Anthony Daniels"]
        },
        "comentarios": 0
    },
    {
        "titulo": "Terminator 2: el juicio final",
        "resumen": "Un cyborg, idéntico al que fracasó en su intento de matar a Sarah Connor, debe proteger ahora a su hijo adolescente John de un cyborg más avanzado y poderoso.",
        "generos": ["Acción", "Fantasía"],
        "directores": {
            "cantidad": 1,
            "lista": ["James Cameron"],
        },
        "fecha_de_lanzamiento": new Date(1991, 12, 5),
        "actores": {
            "cantidad": 4,
            "lista": ["Arnold Schwarzenegger", "Linda Hamilton", "Edward Furlong", "Robert Patrick"]
        },
        "comentarios": 0
    },
    {
        "titulo": "Regreso al futuro",
        "resumen": "Marty McFly, un estudiante de secundaria de 17 años, es enviado accidentalmente treinta años al pasado en un DeLorean que viaja en el tiempo, inventado por su gran amigo, el excéntrico científico Doc Brown.",
        "generos": ["Aventura", "Comedia", "Ciencia ficción"],
        "directores": {
            "cantidad": 1,
            "lista": ["Robert Zemeckis"],
        },
        "fecha_de_lanzamiento": new Date(1985, 12, 2),
        "actores": {
            "cantidad": 4,
            "lista": ["Michael J. Fox", "Christopher Lloyd", "Lea Thompson", "Crispin Glover"]
        },
        "comentarios": 0
    },
    {
        "titulo": "El viaje de Chihiro",
        "resumen": "Durante el traslado de su familia a los suburbios, una niña de 10 años de edad deambula por un mundo gobernado por dioses, brujas y espíritus, y donde los humanos se convierten en bestias.",
        "generos": ["Animación", "Aventura", "Familiar", "Fantasía", "Misterio"],
        "directores": {
            "cantidad": 1,
            "lista": ["Hayao Miyazaki"],
        },
        "fecha_de_lanzamiento": new Date(2002, 10, 25),
        "actores": {
            "cantidad": 4,
            "lista": ["Daveigh Chase", "Suzanne Pleshette", "Miyu Irino", "Rumi Hiigari"]
        },
        "comentarios": 0
    },
])

