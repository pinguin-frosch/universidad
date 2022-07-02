db.comentarios.deleteMany({})
db.comentarios.insertMany([
    {
        "usuario": {
            "nombre": "Ned Stark",
            "correo": "sean_bean@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dc0"),
        "fecha": new Date(2022, 2, 13, 17, 34, 23),
        "comentario": "Una de las películas americanas más ambiciosas y brillantemente ejecutadas",
        "modificaciones": {
            "veces_modificado": 0,
            "comentarios_anteriores": [""]
        }
    },
    {
        "usuario": {
            "nombre": "Robert Baratheon",
            "correo": "mark_addy@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dc7"),
        "fecha": new Date(2022, 3, 14, 20, 20, 3),
        "comentario": "Mis más sinceras felicitaciones a Zemeckis por este peliculón que se ha convertido en una de mis películas preferidas. Pero sobre todo, felicitaciones a Hanks que nos ofrece una de las interpretaciones más magníficas y realistas de la historia del cine y que sin duda ha conseguido un segundo oscar bien merecido.\nTal vez la moraleja de la historia sea que hasta un \"tonto\", puede triunfar en la vida, y desde luego es una graciosa y tierna obra de arte. He leído que a Tom Hanks le costó mucho quiterse ese acento de retrasado después de rodar la película, y no me extraña, porque desde luego convence hasta al público más exigente.\nComo ya he dicho esta película es una joya y aunque la veas una y otra vez, te sigues riendo en las partes cómicas y te sigues emocionando en las escenas más dramáticas.\n¡PELICULÓN!",
        "modificaciones": {
            "veces_modificado": 0,
            "comentarios_anteriores": [""]
        }
    },
    {
        "usuario": {
            "nombre": "Jaime Lannister",
            "correo": "nikolaj_coster-waldau@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dc7"),
        "fecha": new Date(2022, 4, 28, 14, 23, 5),
        "comentario": "Maravillosa película que confirma a Robert Zemeckis como el gran director que es.\nLa historia de Forrest Gump, es tierna y dura a la par, emociona sin apelar a sentimentalismos facilones y baratos. Realiza un recorrido por la historia norteamericana reciente de un modo muy original, diferente a lo visto hasta la fecha.\nFabuloso Tom Hanks (una vez más) en su papel, simplemente genial, hace un trabajo perfecto, emocionante y contenido. También destacable el buen hacer de Gary Sinise (gracias a este papel casi le podemos perdonar la infumable \"Misión a Marte\").\nEn definitiva una película que no se puede pasar de ver. Muy recomendable.",
        "modificaciones": {
            "veces_modificado": 0,
            "comentarios_anteriores": [""]
        }
    },
    {
        "usuario": {
            "nombre": "Jaime Lannister",
            "correo": "nikolaj_coster-waldau@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dcd"),
        "fecha": new Date(2021, 11, 8, 23, 12, 54),
        "comentario": "Genial película de la mafia, lo más completo del cine moderno en cuanto a expresar lo que viene siendo un gangster y todos sus movimientos clásicos en la familia. Buenísima \nNo hace falta saber mucho para encontrar fácilmente el ingrediente Scorsese. \nLas interpretaciones están bordadas en especial la profundidad y credibilidad de Liotta, te cuenta desde que tengo uso de razón quería ser un gangster... y cuando termina todavía tienes grabada esta frase.",
        "modificaciones": {
            "veces_modificado": 1,
            "comentarios_anteriores": ["Sin duda una de las mejores películas de Scorsese y del cine negro.\nMartin Scorsese consigue plasmar en el guión todo lo necesario para que nos engullamos de pleno en el mundo de la mafia."]
        }
    },
    {
        "usuario": {
            "nombre": "Sansa Stark",
            "correo": "sophie_turner@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dc3"),
        "fecha": new Date(2021, 8, 21, 12, 43, 2),
        "comentario": "Cuando se realiza una trilogía, normalmente el punto flaco suele ser la tercera parte, pues las ideas se acaban, y se recurre a repetir lo bueno de las primeras entregas, con la consiguiente falta de originalidad. Y sobre todo en las películas épicas, donde se suele dejar de lado la parte íntima de los personajes, para llevarlos hacia grandes batallas y gestas que serán dignas de recordar por los siglos de los siglos, amén. Pero Peter Jackson no. En el guión de esta película, los personajes sienten, respiran, y evolucionan, y todo ello en un grandísimo mundo épico que no escatima ni un ápice de espectacularidad.",
        "modificaciones": {
            "veces_modificado": 1,
            "comentarios_anteriores": ["Soberbía producción de Jackson, lo tiene todo."]
        }
    },
    {
        "usuario": {
            "nombre": "Melisandre",
            "correo": "carice_van_houten@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dc5"),
        "fecha": new Date(2021, 8, 21, 12, 43, 2),
        "comentario": "Y aquí comenzó la última gran trilogía del cine. De una belleza arrebatadora y una fuerza torrencial, La Comunidad del Anillo no defraudó, y confirmó a Peter Jackson como uno de los grandes directores de nuestra época.",
        "modificaciones": {
            "veces_modificado": 0,
            "comentarios_anteriores": []
        }
    },
    {
        "usuario": {
            "nombre": "Catelyn Stark",
            "correo": "michelle_fairley@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dc6"),
        "fecha": new Date(2021, 12, 9, 12, 4, 2),
        "comentario": "Mi película favorita de mi director favorito protagonizada por mi actor favorito. No puedo pedirle más. El mejor western jamás filmado. Obra maestra indudable. Y todo ello, no siendo más que lo que era el cine del genio italiano: una ensalada de tiros.",
        "modificaciones": {
            "veces_modificado": 0,
            "comentarios_anteriores": []
        }
    },
    {
        "usuario": {
            "nombre": "Jon Snow",
            "correo": "kit_harington@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dc8"),
        "fecha": new Date(2022, 3, 9, 20, 20, 52),
        "comentario": "Me remito a la primera regla del club de la lucha que es no hablar del club de la lucha",
        "modificaciones": {
            "veces_modificado": 0,
            "comentarios_anteriores": []
        }
    },
    {
        "usuario": {
            "nombre": "Bronn",
            "correo": "jerome_flynn@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dd0"),
        "fecha": new Date(2021, 7, 7, 4, 45, 14),
        "comentario": "Antes de realizar la crítica de este monumental film, he querido volver a verlo. Tres horas y veinte minutos de auténtico cine. Los siete samuráis es posiblemente la película más famosa, vista y reconocida del maestro Kurosawa.",
        "modificaciones": {
            "veces_modificado": 1,
            "comentarios_anteriores": ["Si el cine fuera una ciencia y existiera algún artefacto que nos permitiera constatar empíricamente el valor real de “Los siete samuráis”, lo más probable es que la peli de Kurosawa pulverizara completamente dicha maquinita. Sí, sí, no es coña. Las máquinas suelen estar programadas para trabajar a según qué niveles, y cuando las sobrecargas demasiado -lógicamente- se joden."]
        }
    },
    {
        "usuario": {
            "nombre": "Jaime Lannister",
            "correo": "nikolaj_coster-waldau@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dda"),
        "fecha": new Date(2022, 1, 1, 23, 43, 9),
        "comentario": "Cima del arte de los dibujos animados, esta película de Miyazaki provoca un encantamiento que parecía reservado a la época dorada de los estudios Disney. Supera de largo a las escuelas japonesas corrientes, que en su estilo serial y amanerado cuelan de matute mensajes violentos y un extraño tratamiento de las figuras infantiles. Si dicho estilo no gusta, se puede no obstante emprender confiadamente el viaje junto a Chihiro, porque no tiene nada que ver. Va por un rumbo propio, artísticamente original y auténtico.",
        "modificaciones": {
            "veces_modificado": 0,
            "comentarios_anteriores": []
        }
    },
    {
        "usuario": {
            "nombre": "Viserys Targaryen",
            "correo": "harry_lloyd@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dc8"),
        "fecha": new Date(2022, 5, 2, 17, 3, 43),
        "comentario": "Imagina que eres un famoso pintor y un rico duque propietario de un museo te encarga un cuadro de grandes dimensiones. Cuando te dispones a la tarea, tienes una imagen global de lo que quieres plasmar en el lienzo y tienes las directrices generales que te ha dado el duque. Pero eres consciente de que, una vez lo termines, no será exactamente igual, detalle por detalle, a lo que imaginas ahora, pues sabes que las grandes obras no se conciben en un día, sino que son el resultado de un proceso dinámico en el que cada nueva pincelada te da pistas sobre la siguiente. Sólo te queda empezar, aceptando que en el arte, como en la vida misma, no puedes controlarlo todo. Hay que dejarse llevar para evolucionar.",
        "modificaciones": {
            "veces_modificado": 0,
            "comentarios_anteriores": []
        }
    },
    {
        "usuario": {
            "nombre": "Tyrion Lannister",
            "correo": "peter_dinklage@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dcc"),
        "fecha": new Date(2022, 4, 18, 3, 45, 28),
        "comentario": "Matrix es una de esas películas que llegan, arrasan en taquilla y revolucionan su género sin despeinarse. Y todo esto teniendo en cuenta que sus creadores, los hmnos. Washowsky, no habían hecho nada demasiado espectacular antes (igual pasó con Shyamalan cuando hizo \"El Sexto sentido\").",
        "modificaciones": {
            "veces_modificado": 1,
            "comentarios_anteriores": ["La primera película del siglo XXI y la que cambió la manera de hacer cine de acción. Más que impactantes efectos especiales, ciberelectrónica y filosofía de Platón se entremezclan en un cóctel explosivo que golpea al espectador y le deja con la gratificante sensación de que acaba de ver algo que no había visto antes, y que además es realmente bueno."]
        }
    },
    {
        "usuario": {
            "nombre": "Jeor Mormont",
            "correo": "james_cosmo@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dd3"),
        "fecha": new Date(2021, 12, 4, 21, 23, 42),
        "comentario": "Madre mía... la verdad es que Fernando Meirelles acojona. El jardinero fiel es valiente y honesta, pero es que Ciudad de Dios encima es real. Contemplar cómo la vida humana vale menos que un real y filmarlo de esa manera es digno tanto de aplauso como de posterior jaqueca. Innovador en la técnica y con un pulso narrativo excelente, todavía el tipo se apoya en un montaje ¿feroz? para adentrarnos en un mundo que sólo imaginábamos, y por supuesto, ninguno de nosotros suponía que fuese tan malo. Sólo de oídas. Pero cuando descubres que ver y oír son dos verbos distintos... pues te cagas pata abajo.",
        "modificaciones": {
            "veces_modificado": 0,
            "comentarios_anteriores": []
        }
    },
    {
        "usuario": {
            "nombre": "Jeor Mormont",
            "correo": "james_cosmo@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dd3"),
        "fecha": new Date(2022, 3, 4, 17, 54, 00),
        "comentario": "Madre mía... la verdad es que Fernando Meirelles acojona. El jardinero fiel es valiente y honesta, pero es que Ciudad de Dios encima es real. Contemplar cómo la vida humana vale menos que un real y filmarlo de esa manera es digno tanto de aplauso como de posterior jaqueca. Innovador en la técnica y con un pulso narrativo excelente, todavía el tipo se apoya en un montaje ¿feroz? para adentrarnos en un mundo que sólo imaginábamos, y por supuesto, ninguno de nosotros suponía que fuese tan malo. Sólo de oídas. Pero cuando descubres que ver y oír son dos verbos distintos... pues te cagas pata abajo.",
        "modificaciones": {
            "veces_modificado": 0,
            "comentarios_anteriores": []
        }
    },
    {
        "usuario": {
            "nombre": "Jorah Mormont",
            "correo": "iain_glen@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dc8"),
        "fecha": new Date(2021, 8, 23, 23, 54, 35),
        "comentario": "Videoclip fascistoide e infantil. Narrado con una voz en \"off\" que nos tortura durante toda la película.Con recursos cinematográficos de verguenza ajena: personajes que nos hablan directamente, voz en \"off\" constante para suplir la carencia de narración visual, final \"deus ex machine\" para intentar salir al paso, trampas por doquier...",
        "modificaciones": {
            "veces_modificado": 0,
            "comentarios_anteriores": []
        }
    },
    {
        "usuario": {
            "nombre": "Robb Stark",
            "correo": "richard_madden@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dcd"),
        "fecha": new Date(2022, 6, 1, 18, 34, 54),
        "comentario": "Esta película me parece sobrevalorada y prescindible; si no la ves no pasa nada, y si te sientas a verla, pues algunos ratos entretiene un poco, pero otros se hace lenta y repetitiva.\nNo sé si es porque una vez que has visto el padrino, las demás películas sobre la mafia parecen mediocres.",
        "modificaciones": {
            "veces_modificado": 1,
            "comentarios_anteriores": ["...Por darle una enésima oportunidad a Martin Scorsese, posiblemente el peor director de la historia del cine, al menos en proporción con su reconocimiento. Salvo \"El color del dinero\" todas las demás películas que he visto son realmente malas pero esta, creo, es la peor de todas."]
        }
    },
    {
        "usuario": {
            "nombre": "Khal Drogo",
            "correo": "jason_momoa@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dd5"),
        "fecha": new Date(2022, 3, 12, 10, 15, 23),
        "comentario": "ESTADO DE GRACIA, no hay mejor definición, y es que, en este trabajo todo funciona, brillante guión adaptado, asombrosa y hermosa fotografía, actores inspirados y sobre todo la elegante y magnífica dirección de Frank Darabont, que ya demostro con CADENA PERPETUA, que la perfección se podía trasladar al cine (e incluso repetirse).",
        "modificaciones": {
            "veces_modificado": 0,
            "comentarios_anteriores": []
        }
    },
    {
        "usuario": {
            "nombre": "Cersei Lannister",
            "correo": "lena_headey@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dbe"),
        "fecha": new Date(2022, 2, 14, 12, 53, 42),
        "comentario": "Cuando mis padres enfermaron inesperadamente y sin remedio, les llevaba películas con que atenuar la angustiosa inminencia del fin.\nAmbos eran cinéfilos. De jóvenes iban a cineclubs, leían revistas extranjeras, tenían libros en francés (la lengua intelectual entonces) sobre el cine de vanguardia. De modo habitual, veían películas y las comentaban entre sí, una y otra vez.",
        "modificaciones": {
            "veces_modificado": 0,
            "comentarios_anteriores": []
        }
    },
    {
        "usuario": {
            "nombre": "Joffrey Baratheon",
            "correo": "jack_gleeson@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dcf"),
        "fecha": new Date(2021, 11, 21, 14, 45, 10),
        "comentario": "Es un clímax casi continuo: cuando no te estremece, te inquieta, o te hace reflexionar, o, incluso, reír. A excepción del final, que es lo mejor, no podría decir en qué punto del metraje se alcanza un nivel de carga emocional claramente superior al resto.",
        "modificaciones": {
            "veces_modificado": 0,
            "comentarios_anteriores": []
        }
    },
    {
        "usuario": {
            "nombre": "Jeor Mormont",
            "correo": "james_cosmo@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dd8"),
        "fecha": new Date(2022, 4, 2, 15, 34, 45),
        "comentario": "No hay nadie como el señor Cameron para esto del cine de acción. Nadie mejor que él sabe entender lo que el público pide en este tipo de películas y no se aleja jamás del más puro y basto entretenimiento mezclando de forma magistral ingredientes básicos de una película de acción como el humor, las escenas espectaculares o los diálogos cargados de sarcasmo. Y para ello da igual que el argumento sea inverosímil, como el ejemplo que hoy nos ocupa. Al salir del cine no recordarás la mayor parte de la trama, ni falta que hace.",
        "modificaciones": {
            "veces_modificado": 0,
            "comentarios_anteriores": []
        }
    },
    {
        "usuario": {
            "nombre": "Sansa Stark",
            "correo": "sophie_turner@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dc9"),
        "fecha": new Date(2021, 10, 23, 12, 45, 52),
        "comentario": "Mucho se ha dicho ya de esta película y no quiero ser repetitivo. A mí me ha gustado mucho y me quedé con la sensación de que ese día me había salido barato el cine y hasta el menú Big King posterior. Entiendo que haya gente que no comparta mi opinión pero leyendo las críticas negativas de esta cinta me he decidido hacer la mía, pero no para ensalzar la película, sino para defenderla de críticas poco sostenibles a mi parecer.",
        "modificaciones": {
            "veces_modificado": 1,
            "comentarios_anteriores": ["Una de las grandezas de Nolan y su modo de hacer cine, es su habilidad para unir contenido y entretenimiento de primer nivel. Uno tiene un público más reducido, y el otro a menudo nos pide que dejemos el cerebro a la entrada. Es verdad que a veces nos lo pide el cuerpo, pero en temporadas como la de verano esto toma visos de condena."]
        }
    },
    {
        "usuario": {
            "nombre": "Varys",
            "correo": "conleth_hill@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dda"),
        "fecha": new Date(2021, 12, 30, 23, 43, 54),
        "comentario": "Para los que les gusta el anime, para los que no, para los que sólo quieren ver una película buena, para los que quieren sacar miles de reflexiones, para los que quieren emocionarse, para los que les quieren quedarse con pequeños momentos, para los que quieren quedarse con momentazos. Para todos.",
        "modificaciones": {
            "veces_modificado": 0,
            "comentarios_anteriores": []
        }
    },
    {
        "usuario": {
            "nombre": "Viserys Targaryen",
            "correo": "harry_lloyd@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dc0"),
        "fecha": new Date(2022, 1, 18, 13, 43, 8),
        "comentario": "No se trata ya de un simple retrato de los quehaceres de una familia mafiosa y su lucha por el poder, ahora las interrelaciones se han complicado y existe un verdadero entorno vivo fuera de ellos, desde políticos a empresarios, todos ellos forman parte de la historia en igualdad de condiciones. Es decir, lo que es la Historia, con mayúsculas, ya no es de género, es un relato sociológico, histórico, político y económico de un momento clave para los Estados Unidos. Y esto lo hace en el río de Pacino como en el de Robert De Niro. La llegada de los inmigrantes, su asentamiento en Little Italy, las relaciones con Cuba, las comisiones de investigación sobre la Mafia... estamos hablando ya de otra cosa, estamos hablando de Cine, no como un mero instrumento de sensaciones placenteras o impactantes, sino como un medio cultural de aprendizaje.",
        "modificaciones": {
            "veces_modificado": 0,
            "comentarios_anteriores": []
        }
    },
    {
        "usuario": {
            "nombre": "Bronn",
            "correo": "jerome_flynn@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dc2"),
        "fecha": new Date(2021, 11, 12, 18, 12, 34),
        "comentario": "¿ Cómo puede una niña pequeña perdida entre la multitud ejemplificar de una manera tan perfecta el puro horror ante la masacre ? Spielberg logró que el espectador se sintiera, al igual que Oskar Schindler en su caballo, abrumado al ver cómo una pequeña niña caminaba sola por el guetto en medio de la masacre, y con el paso del tiempo, dicha secuencia ha permanecido grabada a fuego en el subconsciente colectivo como una de esas imágenes de un poder visual único. Spielberg calló las bocas de aquellos que le tachaban de mero director de productos ultracomerciales con esta película necesaria, soberbia, hermosa, y demostrando a todo el mundo que si se pone serio, no pierde ni un ápice de calidad.",
        "modificaciones": {
            "veces_modificado": 0,
            "comentarios_anteriores": []
        }
    },
    {
        "usuario": {
            "nombre": "Arya Stark",
            "correo": "maisie_williams@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dd8"),
        "fecha": new Date(2021, 2, 15, 14, 45, 3),
        "comentario": "Mi valoración de esta película es muy similar a la de la primera, para la que ya escribí una crítica, así que no me voy a explayar. Que sí, que vale, que es una peli de mucha acción, con unos efectos especiales alucinantes, sobre todo lo del tío de cristal líquido que se funde como si fuera agua y se vuelve a reconstruir. Y realmente el Schwarzenegger parece una mezcla entre hombre y robot.\nEn esta ocasión le han añadido un toque de humor y cierta ternura (como para decir: oye, que los robots también podemos tener sentimientos y ser simpáticos, ¿eh?) al poner al Schwarzenegger en esta ocasión en el bando de los buenos. Lo único entretenido que le veo a la peli es la relación entre el robot y el niño, con el niño enseñando al robot a comportarse como un humano.\nEn general, parece más descafeinada que la primera y le han metido el toque tierno con el niño, pero para mí igualmente vacía y poco memorable.\nLo que más me llamó la atención fue la banda sonora, que se puso muy de moda incluso en versiones discotequeras.",
        "modificaciones": {
            "veces_modificado": 0,
            "comentarios_anteriores": []
        }
    },
    {
        "usuario": {
            "nombre": "Tywin Lannister",
            "correo": "charles_dance@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dce"),
        "fecha": new Date(2022, 4, 25, 14, 43, 54),
        "comentario": "Oda a la libertad de Forman.\nA pesar de que la película transcurre en un manicomio, las referencias a la vida cotidiana son constantes, todos somos los que gastamos el tiempo jugando a la cartas o en la cola para los medicamentos, para cumplir las normas y llegar a ser uno más, la mayor aspiración que tenemos en la vida (eso, y 22 días de vacaciones anuales, claro). Y lo hacen, para evitar que los \"eliminen\" dejando atrás la añoranza de desarrollar la libre personalidad.",
        "modificaciones": {
            "veces_modificado": 0,
            "comentarios_anteriores": []
        }
    },
    {
        "usuario": {
            "nombre": "Stannis Baratheon",
            "correo": "stephen_dillane@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dc3"),
        "fecha": new Date(2021, 11, 23, 14, 53, 34),
        "comentario": "Magistral, deslumbrante, fascinante...no se, diría que es perfecta. A mi modo de ver esta entre las 5 mejores películas de todos los tiempos. Brillante banda sonora, paisajes, fotografia, historia... la verdad que mires por donde la mires, no encuentras nada que se pueda mejorar. El retorno del Rey pone punto final a la mejor trilogia (con permiso del Padrino ) de la historia del cine.",
        "modificaciones": {
            "veces_modificado": 0,
            "comentarios_anteriores": []
        }
    },
    {
        "usuario": {
            "nombre": "Arya Stark",
            "correo": "maisie_williams@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dd0"),
        "fecha": new Date(2022, 1, 14, 9, 54, 23),
        "comentario": "Esta película de culto ha sido plagiada y adaptada a otros géneros como el Western (Los Siete Magníficos), la Ciencia Ficción (Los Siete Magníficos del Espacio) o incluso la animación (Bichos), con mayor o menor fortuna según el caso.\nPero en todos ellos se cuenta la misma \"moraleja\" en la mitad de tiempo y con mucha más fluidez y entretenimiento para el espectador.\nEn todo caso, al ser el creador de la historia hay que concederle cierto reconocimiento.",
        "modificaciones": {
            "veces_modificado": 0,
            "comentarios_anteriores": []
        }
    },
    {
        "usuario": {
            "nombre": "Viserys Targaryen",
            "correo": "harry_lloyd@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dd2"),
        "fecha": new Date(2021, 10, 17, 20, 34, 45),
        "comentario": "Cuando pienso en el \"Silencio de los corderos\", aparte de que es un film de culto y posiblemente el thriller más relevante y popular de los noventa que triunfo por sorpresa contra todo pronóstico, lo primero que me viene a la cabeza es la escena del manicomio en que Miggs, el vecino chalado de Lecter, riega a la agente Starling con cierta substancia de elaboración propia.",
        "modificaciones": {
            "veces_modificado": 0,
            "comentarios_anteriores": []
        }
    },
    {
        "usuario": {
            "nombre": "Melisandre",
            "correo": "carice_van_houten@gameofthron.es"
        },
        "id_pelicula": ObjectId("62bb73f2a13ba394ce9b3dc3"),
        "fecha": new Date(2021, 12, 29, 21, 19, 23),
        "comentario": "Esta es la última parte de la trilogía de El Señor de los Anillos. El principal problema que le veo, a parte de su ideología medievalista basada en el honor, el sacrificio y el éxito, es que cuenta las cosas de forma muy rápida. Narra episodios muy rimbombantes y espectaculares de una manera tan próxima en el tiempo que a uno no le da tiempo a acostumbrarse de nuevo a la normalidad (es decir, a la calma y a que se desarrolle el deseo y las expectativas) y, por lo tanto, las grandes hazañas aquí contadas tienen menos impacto emocional del que podrían tener si se espaciaran.",
        "modificaciones": {
            "veces_modificado": 0,
            "comentarios_anteriores": []
        }
    },
])

db.peliculas.updateOne({_id: ObjectId("62bb73f2a13ba394ce9b3dc0")}, {$set: {comentarios: 2}})
db.peliculas.updateOne({_id: ObjectId("62bb73f2a13ba394ce9b3dc7")}, {$set: {comentarios: 2}})
db.peliculas.updateOne({_id: ObjectId("62bb73f2a13ba394ce9b3dcd")}, {$set: {comentarios: 2}})
db.peliculas.updateOne({_id: ObjectId("62bb73f2a13ba394ce9b3dc3")}, {$set: {comentarios: 3}})
db.peliculas.updateOne({_id: ObjectId("62bb73f2a13ba394ce9b3dc5")}, {$set: {comentarios: 1}})
db.peliculas.updateOne({_id: ObjectId("62bb73f2a13ba394ce9b3dc6")}, {$set: {comentarios: 1}})
db.peliculas.updateOne({_id: ObjectId("62bb73f2a13ba394ce9b3dc8")}, {$set: {comentarios: 3}})
db.peliculas.updateOne({_id: ObjectId("62bb73f2a13ba394ce9b3dd0")}, {$set: {comentarios: 2}})
db.peliculas.updateOne({_id: ObjectId("62bb73f2a13ba394ce9b3dda")}, {$set: {comentarios: 2}})
db.peliculas.updateOne({_id: ObjectId("62bb73f2a13ba394ce9b3dcc")}, {$set: {comentarios: 1}})
db.peliculas.updateOne({_id: ObjectId("62bb73f2a13ba394ce9b3dd3")}, {$set: {comentarios: 2}})
db.peliculas.updateOne({_id: ObjectId("62bb73f2a13ba394ce9b3dd5")}, {$set: {comentarios: 1}})
db.peliculas.updateOne({_id: ObjectId("62bb73f2a13ba394ce9b3dbe")}, {$set: {comentarios: 1}})
db.peliculas.updateOne({_id: ObjectId("62bb73f2a13ba394ce9b3dcf")}, {$set: {comentarios: 1}})
db.peliculas.updateOne({_id: ObjectId("62bb73f2a13ba394ce9b3dd8")}, {$set: {comentarios: 2}})
db.peliculas.updateOne({_id: ObjectId("62bb73f2a13ba394ce9b3dc9")}, {$set: {comentarios: 1}})
db.peliculas.updateOne({_id: ObjectId("62bb73f2a13ba394ce9b3dc2")}, {$set: {comentarios: 1}})
db.peliculas.updateOne({_id: ObjectId("62bb73f2a13ba394ce9b3dce")}, {$set: {comentarios: 1}})
db.peliculas.updateOne({_id: ObjectId("62bb73f2a13ba394ce9b3dd2")}, {$set: {comentarios: 1}})

