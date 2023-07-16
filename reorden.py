import random

# Supongamos que este es tu array de listas
mi_array = [['¿Cuál es el valor de "x" si 2x = 8?', '4', '3', '6', '16'], ['¿Cuál es la fórmula química del ácido sulfúrico?', 'H2SO4', 'H2O', 'H2SO3', 'HSO4'], ['¿Cuál es la unidad básica de la vida?', 'Célula', 'Átomo', 'Molécula', 'Organelo'], ['¿Cuál de las siguientes estructuras se encuentra en el núcleo de la célula?', 'ADN', 'Cloroplasto', 'Ribosoma', 'Mitocondria'], ['¿Cuál es el país más grande del mundo?', 'Rusia', 'Canadá', 'China', 'Estados Unidos'], ['¿Cómo se llama el compuesto CH4?', 'Metano', 'Etano', 'Metanol', 'Metileno'], ['¿Quién formuló la ecuación E=mc²?', 'Albert Einstein', 'Max Planck', 'Niels Bohr', 'Richard Feynman'], ['¿Dónde se encuentra la Torre de Pisa?', 'Italia', 'Francia', 'España', 'Portugal'], ['¿Cuál de los siguientes es el órgano encargado de la digestión de los alimentos en el cuerpo humano?', 'Estómago', 'Riñón', 'Pulmón', 'Hígado'], ['Si en una caja caben 25 bombones y tengo 100 bombones, ¿cuántas cajas necesito?', '4', '3', '5', '6'], ['Un ángulo mayor que 90° y menor a que 180° es conocido como:', 'Obtuso', 'Recto', 'Cóncavo', 'Convexo'], ['¿Qué nombre recibe la capa externa de la piel?', 'Epidermis', 'Dermis', 'Hipopodermis', 'Tejido subcutáneo'], ['¿Cuál es la capital de Brasil?', 'Brasilia', 'Río de Janeiro', 'Sao Paulo', 'Salvador'], ['¿Cuál es el resultado de multiplicar (-1)*(-1)?', '+1', '-1', '∓1', '±1'], ['¿Cuál es el principal gas responsable del efecto invernadero?', 'Dióxido de carbono', 'Oxígeno', 'Nitrógeno', 'Metano'], ['¿Cuál es el órgano encargado de la filtración de la sangre en el cuerpo humano?', 'Riñón', 'Hígado', 'Páncreas', 'Estómago'], ['¿Qué gas se libera durante la fotosíntesis?', 'Oxígeno', 'Dióxido de carbono', 'Nitrógeno', 'Hidrógeno'], ['¿En qué país se encuentra el Machu Picchu?', 'Perú', 'Chile', 'Bolivia', 'Argentina'], ['¿Qué representa la molécula de CO2?', 'Dióxido de carbono', 'Monóxido de carbono', 'Cobre', 'Cloro'], ['¿Cuál es el órgano encargado de producir la insulina en el cuerpo humano?', 'Páncreas', 'Hígado', 'Riñón', 'Estómago'], ['¿Cuál es la primera ley de Newton?', 'Ley de Inercia', 'Fuerza', 'Acción y reacción', 'Gravitación'], ['¿Qué mide un termómetro?', 'Temperatura', 'Presión', 'Humedad', 'Velocidad'], ['¿Cuál es la fuerza más débil conocida?', 'Gravitatoria', 'Electromagnética', 'Nuclear fuerte', 'Nuclear débil'], ['¿Cuál de los siguientes no es un tipo de músculo?', 'Nervioso', 'Esquelético', 'Cardíaco', 'Liso'], ['¿Cuál de las siguientes glándulas produce la hormona del crecimiento?', 'Glándula pituitaria', 'Glándula tiroides', 'Glándula suprarrenal', 'Glándula pancreática'], ['¿Qué faraón egipcio es conocido por sus monumentos en Abu Simbel?', 'Ramsés II', 'Tutankamón', 'Cleopatra', 'Nefertiti'], ['¿Quién propuso la televtrodinámica cuántica?', 'Paul Dirac', 'Max Planck', 'Albert Einstein', 'Erwin Schrödinger'], ['¿Quién descubrió la penicilina?', 'Alexander Fleming', 'Marie Curie', 'Louis Pasteur', 'Isaac Newton'], ['¿Cuántos grados hay en un ángulo recto?', '90', '180', '45', '180'], ['¿Cuál es el lago más grande del mundo?', 'Mar Caspio', 'Lago Superior', 'Lago Baikal', 'Lago Victoria'], ['¿Quién descubrió el electrón?', 'J.J. Thomson', 'Albert Einstein', 'Marie Curie', 'Ernest Rutherford'], ['¿Qué pintor holandés es famoso por pintar "La noche estrellada"?', 'Vincent Van Gogh', 'Piet Mondrian', 'Johannes Vermeer', 'Rembrandt'], ['¿Quién formuló la teoría de la relatividad?', 'Albert Einstein', 'Isaac Newton', 'Niels Bohr', 'Richard Feynman'], ['¿Qué es un ácido en términos de pH?', 'Sustancia con pH < 7', 'Sustancia con pH > 7', 'Sustancia con pH = 7', 'Sustancia con pH = 14'], ['¿En qué unidad se mide la resistencia eléctrica?', 'Ohmios', 'Amperios', 'Voltios', 'Wattios'], ['¿Cuál es la fórmula química del amoníaco?', 'NH3', 'NH4', 'NH2', 'N2H4'], ['¿Qué carga tiene un protón?', 'Carga positiva', 'Carga negativa', 'Positiva y negativa', 'Neutra'], ['¿Qué reina de Francia es conocida por decir "Que coman pastel", aunque probablemente nunca lo dijo?', 'María Antonieta', 'Juana de Arco', 'Catalina de Medici', 'María de Médicis'], ['¿Qué es la física de partículas?', 'Estudia partículas subatómicas', 'Estudia la luz', 'Estudia la gravedad', 'Estudia energía a gran escala'], ['¿Cuál es la raíz cuadrada de 49?', '7', '11', '23', '98'], ['¿Cómo se llama a la línea que divide un círculo en dos partes iguales?', 'Diámetro', 'Perímetro', 'Radio', 'Tangente'], ['¿Cuál es el continente más grande del mundo?', 'Asia', 'África', 'América', 'Antártida'], ['¿Cuál es el nombre del proceso mediante el cual las plantas liberan agua en forma de vapor?', 'Transpiración', 'Fotosíntesis', 'Respiración', 'Evaporación'], ['¿Cuál es el símbolo químico del Estaño?', 'Sn', 'Tn', 'St', 'Ts'], ['¿En qué año fue la Declaración de Independencia de los Estados Unidos?', '1776', '1783', '1800', '1750'], ['¿Qué número es "V" en números romanos?', '5', '50', '10', '3'], ['¿Cómo se llama la energía en movimiento?', 'Cinética', 'Potencial', 'Térmica', 'Eléctrica'], ['¿Dónde se encuentra el punto más bajo de la superficie terrestre?', 'Mar Muerto', 'Cuenca del Danakil', 'Lago Assal', 'Fosa de las Marianas'], ['¿Qué tipo de energía produce la respiración celular?', 'Energía química (ATP)', 'Energía solar', 'Energía térmica', 'Energía eléctrica'], ['¿Como se llama la recta que va desde el centro de un circulo a un punto de su perimétro?', 'Radio', 'Diámetro', 'Seno', 'Pi'], ['¿Cuál es la capital de Suecia?', 'Estocolmo', 'Oslo', 'Copenhague', 'Helsinki'], ['Si un coche recorre 60 km en media hora, ¿a qué velocidad va?', '120 km/h', '60 km/h', '30 km/h', '45 km/h'], ['¿Qué famosa batalla tuvo lugar en 1066 que cambió la historia de Inglaterra?', 'Batalla de Hastings', 'Batalla de Bosworth', 'Batalla de Agincourt', 'Batalla de Waterloo'], ['¿Qué es un gluón?', 'Partícula que une quarks', 'Partícula de luz', 'Partícula de calor', 'Partícula de fuerza'], ['¿Cómo se llama la tabla donde se organizan los elementos químicos?', 'Tabla periódica', 'Tabla de elementos', 'Tabla química', 'Tabla de Mendeleev'], ['¿En qué país se encuentra el volcán Krakatoa?', 'Indonesia', 'Japón', 'Italia', 'Filipinas'], ['¿Cuál es el país más grande de África?', 'Argelia', 'Congo', 'Sudán', 'Libia'], ['¿Cuál es la montaña más alta de África?', 'Kilimanjaro', 'Everest', 'Aconcagua', 'Denali'], ['¿Cuál es la montaña más alta de América del Sur?', 'Aconcagua', 'Kilimanjaro', 'Everest', 'Denali'], ['¿Quién fue el primer hombre en realizar vuelos bien planeados, repetidos y exitosos con planeadores?', 'Otto Lilienthal', 'Wilbur Wright', 'Orville Wright', 'Louis Blériot'], ['¿Qué mide el decibelio?', 'La intensidad del sonido', 'La cantidad de luz', 'La cantidad de calor', 'La presión atmosférica'], ['¿Cuál es la capital de Dinamarca?', 'Copenhague', 'Estocolmo', 'Oslo', 'Helsinki'], ['¿Cuál es el elemento más ligero de la tabla periódica?', 'Hidrógeno', 'Helio', 'Litio', 'Carbono'], ['¿En qué país se encuentra el Taj Mahal?', 'India', 'China', 'Tailandia', 'Nepal'], ['¿En qué año se abrió el Canal de Suez?', '1869', '1859', '1879', '1889'], ['¿Cómo se llama el H2O en términos comunes?', 'Agua', 'Aire', 'Acido', 'Oxígeno'], ['¿Cuál es la suma de los 10 primeros números naturales? (sin contar el 0)', '55', '57', '67', '100'], ['¿En qué país se encuentra el río Misisipi?', 'Estados Unidos', 'Canadá', 'México', 'Brasil'], ['¿Qué emperador romano construyó un muro en Gran Bretaña?', 'Adriano', 'Augusto', 'Nerón', 'Julio César'], ['¿Cuál de los siguientes no es un tipo de tejido animal?', 'Clorofílico', 'Epitelial', 'Muscular', 'Nervioso'], ['¿Cuál de los siguientes es un hueso del cráneo humano?', 'Frontal', 'Fémur', 'Costilla', 'Húmero'], ['¿Cuál de los siguientes es el órgano encargado de la producción de la bilis?', 'Hígado', 'Riñón', 'Pulmón', 'Páncreas'], ['¿Qué elemento tiene el símbolo químico Na?', 'Sodio', 'Nitrógeno', 'Neón', 'Níquel'], ['¿Cómo se le llama a los ángulos menores que 45°', 'Agudos', 'Obtusos', 'Graves', 'Cóncavo'], ['¿Cuál es la principal función de las enzimas en los seres vivos?', 'Catalizar reacciones químicas', 'Transportar oxígeno', 'Producir energía', 'Regular la temperatura corporal'], ['¿Qué faraón egipcio es conocido por su máscara funeraria de oro?', 'Tutankamón', 'Ramsés II', 'Cleopatra', 'Nefertiti'], ['En multiplicación de signos - por + es igual a...', '-', '+', '±', '∓'], ['¿Quién fue el último zar de Rusia?', 'Nicolás II', 'Alejandro III', 'Alejandro II', 'Pedro III'], ['¿En qué país se encentra el volcán Popocatépetl?', 'México', 'Perú', 'Honduras', 'Colombia'], ['¿Cuál es el otro nombre común de la vitamina C?', 'Ácido ascórbico', 'Vitamina B12', 'Vitamina D', 'Ácido fólico'], ['¿Qué emperador romano legalizó el cristianismo?', 'Constantino', 'Nerón', 'Augusto', 'Julio César'], ['¿Cuál es el estado de la materia donde las partículas están más juntas?', 'Sólido', 'Líquido', 'Gaseoso', 'Plasma'], ['¿Cuál es la raiz cuadrada de 144?', '12', '24', '44', '10.4'], ['¿Qué famoso físico propuso las tres leyes del movimiento?', 'Isaac Newton', 'Albert Einstein', 'Galileo Galilei', 'Nikola Tesla'], ['¿Cuál de los siguientes no es un tipo de tejido animal?', 'Clorofílico', 'Epitelial', 'Muscular', 'Nervioso'], ['¿Qué elemento es el más abundante en el universo?', 'Hidrógeno', 'Oxígeno', 'Helio', 'Nitrógeno'], ['¿En qué año se celebraron los primeros Juegos Olímpicos modernos?', '1896', '1900', '1912', '1880'], ['¿En qué país se encuentra el río Ganges?', 'India', 'Bangladesh', 'Nepal', 'Bután'], ['¿Cuál es el símbolo químico del hierro?', 'Fe', 'H', 'He', 'I'], ['¿En qué año se formó la Unión Europea?', '1993', '1989', '1995', '2000'], ['¿Cuál es el nombre del pigmento responsable de dar color a la piel?', 'Melanina', 'Clorofila', 'Hemoglobina', 'Bilirrubina'], ['¿Qué arquitecto diseñó la Sagrada Familia en Barcelona?', 'Antoni Gaudí', 'Pablo Picasso', 'Salvador Dalí', 'Joan Miró'], ['¿Cuál de los siguientes es un ejemplo de una proteína?', 'Hemoglobina', 'Glucosa', 'ADN', 'Vitamina C'], ['¿Cuál es el nombre de la molécula responsable del transporte de oxígeno en la sangre?', 'Hemoglobina', 'Insulina', 'Enzima', 'Melanina'], ['¿Cuál es la ley de Ohm?', 'V=IR', 'E=mc^2', 'F=ma', 'a=v/t'], ['¿Qué mide el espectro electromagnético?', 'Longitud de onda', 'Carga eléctrica', 'Corriente', 'Voltaje'], ['¿Cuál es el elemento más electronegativo?', 'Flúor', 'Oxígeno', 'Nitrógeno', 'Cloro'], ['¿En qué ciudad se encuentra la Estatua de la Libertad?', 'Nueva York', 'Washington D.C.', 'Chicago', 'Boston'], ['¿Qué número (apróximado) representa la letra griega π?', '3.1416', '3', '6.1416', '4'], ['¿Qué es la mitosis?', 'El proceso de división celular', 'La producción de gametos', 'La formación de tejidos', 'La absorción de nutrientes'], ['¿En qué país se encuentra el Parque Nacional Kruger?', 'Sudáfrica', 'Kenia', 'Tanzania', 'Botswana'], ['¿Qué descubridor de América murió creyendo que había encontrado una ruta hacia Asia?', 'Cristóbal Colón', 'Amerigo Vespucci', 'Fernando de Magallanes', 'Juan Ponce de León'], ['¿Qué elemento tiene el símbolo químico K?', 'Potasio', 'Kriptón', 'Calcio', 'Potasio'], ['¿Cuál de los siguientes es un ejemplo de una enfermedad transmitida por mosquitos?', 'Dengue', 'Varicela', 'Gripe', 'Tuberculosis'], ['¿En qué continente se encuentra Madagascar?', 'África', 'Asia', 'América', 'Europa'], ['¿Quién fue el autor de "El Príncipe", un tratado de política del siglo XVI?', 'Nicolás Maquiavelo', 'Thomas Hobbes', 'Jean-Jacques Rousseau', 'John Locke'], ['¿Cuál es el símbolo químico del Plata?', 'Ag', 'Au', 'P', 'Pa'], ['¿Cuántos ceros tiene un millón?', '6', '7', '5', '3'], ['¿En qué país se encuentra la pirámide de Giza?', 'Egipto', 'México', 'Perú', 'India'], ['¿En qué país se encuentra el Gran Cañón?', 'Estados Unidos', 'Canadá', 'México', 'Argentina'], ['¿Cuál es el lago más profundo del mundo?', 'Baikal', 'Tanganica', 'Caspian', 'Superior'], ['¿Cuánto es la mitad de 2 + 1', '2', '3', '1.5', '4'], ['¿Qué líder político sudafricano fue liberado de prisión en 1990 después de casi 28 años?', 'Nelson Mandela', 'Thabo Mbeki', 'Desmond Tutu', 'Jacob Zuma'], ['¿Quién descubrió la radioactividad?', 'Marie Curie', 'Albert Einstein', 'Isaac Newton', 'Max Planck'], ['¿Cuál es el proceso por el cual las plantas convierten materia inorgánica en materia orgánica utilizando la luz solar?', 'Fotosíntesis', 'Respiración celular', 'Digestión', 'Excreción'], ['¿Qué es un amperio?', 'Unidad de corriente eléctrica', 'Unidad de tensión', 'Unidad de resistencia', 'Unidad de carga'], ['¿Qué zar ruso es conocido como el "Zar Liberator" por abolir la servidumbre?', 'Alejandro II', 'Nicolás II', 'Alejandro I', 'Pedro el Grande'], ['¿Cuál es la fuerza más fuerte en el universo?', 'La fuerza nuclear fuerte', 'La fuerza gravitatoria', 'La fuerza electromagnética', 'La fuerza nuclear débil'], ['¿Qué figura geométrica tiene 4 lados iguales pero no es un cuadrado?', 'Rombo', 'Pentágono', 'Rectángulo', 'Trapecio'], ['¿Qué es un electrón?', 'Una partícula con carga negativa', 'Una partícula con carga positiva', 'Un tipo de radiación', 'Un tipo de molécula'], ['¿Qué país es conocido como la Tierra del Sol Naciente?', 'Japón', 'China', 'India', 'Corea del Sur'], ['¿Cuál de los siguientes es un ejemplo de un órgano vestigial en los seres humanos?', 'Apéndice', 'Corazón', 'Cerebro', 'Pulmón'], ['¿Cuál es la velocidad de la luz en el vacío?', '299,792 km por segundo', '30,000 km por segundo', '1,000 km por segundo', '500,000 km por segundo'], ['¿Qué país es conocido como la Tierra de los Kiwis?', 'Nueva Zelanda', 'Australia', 'Inglaterra', 'Canadá'], ['¿Cuántos grados suman los ángulos internos de un cuadrado?', '360°', '180°', '270°', '90°'], ['¿Qué es un hadrón?', 'Partícula compuesta de quarks', 'Partícula de luz', 'Partícula de calor', 'Partícula de fuerza'], ['¿Cuál de los siguientes no es un grupo sanguíneo humano?', 'Grupo X', 'Grupo A', 'Grupo B', 'Grupo AB'], ['¿Quién fue conocido como el "León de Judá" en Etiopía?', 'Haile Selassie', 'Menelik II', 'Yohannes IV', 'Tewodros II'], ['¿Cuál es la fórmula química del amoníaco?', 'NH3', 'NH4', 'NH2', 'N2H4'], ['¿Qué es la densidad en términos químicos?', 'Masa por unidad de volumen', 'Volumen por unidad de masa', 'Peso por unidad de volumen', 'Átomos por unidad de volumen'], ['¿Qué trata de explicar la teoría del big bang?', 'Origen del universo', 'Origen de la vida', 'Origen de la Tierra', 'Origen de la energía'], ['¿Cuál es el órgano más grande del cuerpo humano?', 'La piel', 'El hígado', 'El corazón', 'Los pulmones'], ['¿Cómo se llama el estudio del universo a gran escala?', 'Cosmología', 'Astrofísica', 'Quantum física', 'Meteorología'], ['¿Cómo se le llama a los átomos del mismo elemento con diferentes números de neutrones?', 'Isótopos', 'Quimera', 'Isopropílico', 'Intrótopos'], ['¿Cuál es el proceso de formación de nuevas células sexuales en los seres vivos?', 'Meiosis', 'Mitosis', 'Fotosíntesis', 'Axis'], ['¿Cuál es la capital de Canadá?', 'Ottawa', 'Toronto', 'Montreal', 'Vancouver'], ['¿Cuál es el país más pequeño del mundo?', 'Vaticano', 'Mónaco', 'San Marino', 'Liechtenstein'], ['¿Cuánto es 1000-100+10?', '910', '990', '900', '890'], ['¿En qué año se descubrió la tumba de Tutankamón?', '1922', '1911', '1930', '1899'], ['¿Cuántos elementos hay en la tabla periódica?', '118', '100', '120', '112'], ['¿Cuál es el nombre de la hormona responsable de regular el nivel de glucosa en la sangre?', 'Insulina', 'Testosterona', 'Estrógeno', 'Adrenalina'], ['¿Dónde se encuentra la Gran Barrera de Coral?', 'Australia', 'Hawái', 'Fiji', 'Filipinas'], ['¿Qué país tiene la mayor cantidad de islas?', 'Suecia', 'Filipinas', 'Indonesia', 'Canadá'], ['¿Qué son los leptones?', 'Partículas elementales', 'Un tipo de energía', 'Unidades de fuerza', 'Un tipo de luz'], ['¿Qué antigua ciudad fue destruida por la erupción del Vesubio en el 79 d.C.?', 'Pompeya', 'Roma', 'Atenas', 'Esparta'], ['¿Qué fórmula calcula el aŕea de un círculo?', 'πr²', '2πr', 'πr/2', 'π²r'], ['¿Cuántas caras tiene una pirámide de base cuadrada?', '5', '4', '3', '6'], ['¿Qué invento se atribuye a Johannes Gutenberg en el siglo XV?', 'Imprenta', 'Brújula', 'Telescopio', 'Microscopio'], ['¿Qué importante documento fue firmado por el Rey Juan de Inglaterra en 1215?', 'Magna Carta', 'Declaración de Breda', 'Bill of Rights', 'Constitución de Inglaterra'], ['¿En qué año se produjo la masacre de la plaza de Tiananmen en China?', '1989', '1991', '1985', '1987'], ['¿Cuál es la tercera ley de Newton?', 'Acción y reacción', 'F=ma', 'Preservación del estado', 'Conservación de la energía'], ['¿Qué es un neutrón?', 'Partícula sin carga', 'Partícula negativa', 'Partícula positiva', 'Partícula doblemente cargada'], ['¿Qué se deduce de la segunda ley de la termodinámica?', 'Aumento de la entropía', 'Conservación de la energía', 'Inercia', 'Acción y reacción'], ['¿Cuántos lados tiene un dodecágono?', '12', '10', '22', '20'], ['¿Qué letra equivale al 1000 en números romanos', 'M', 'X', 'V', 'Z'], ['¿Cómo se le llama a los ángulos mayores que 180°?', 'Cóncavo', 'Agudos', 'Rectos', 'Obtusos'], ['¿Qué líder chino es conocido por la "Revolución Cultural"?', 'Mao Zedong', 'Deng Xiaoping', 'Xi Jinping', 'Chiang Kai-shek'], ['¿Qué partículas se encuentran en el núcleo de un átomo?', 'Protones y neutrones', 'Protones y electrones', 'Electrones y neutrones', 'Solo protones'], ['¿Cuál es el nombre de la célula reproductora masculina?', 'Espermatozoide', 'Óvulo', 'Eritrocito', 'Leucocito'], ['¿Cuál es el elemento más abundante en la atmósfera terrestre?', 'Nitrógeno', 'Oxígeno', 'Carbono', 'Hidrógeno'], ['¿Cuál es la fórmula química de la sal común?', 'NaCl', 'KCl', 'CaCl2', 'NaOH'], ['¿Cuánto es 3 elevado al cubo (3^3)?', '27', '9', '6', '33'], ['¿En qué país se encuentra la Ciudad Prohibida?', 'China', 'Japón', 'Corea del Sur', 'Vietnam'], ['Un número natural mayor que 1 que tiene únicamente dos divisores positivos distintos: él mismo y el 1 se denomina número...', 'Primo', 'Irracional', 'Imaginario', 'Simple'], ['¿Qué opción representa el teorema de pitágoras?', '\\( c^{2} = a^{2} + b^{2} \\)', 'F=ma', '\\( E = mc^{2} \\)', '\\(F=G({m M}/{d^2})\\)'], ['¿Cuál es la unidad de frecuencia?', 'Hertz', 'Joule', 'Newton', 'Watt'], ['¿Cuál es el pH neutro en la escala de pH?', '7', '0', '14', '5'], ['¿Cuál es el proceso de eliminación de desechos líquidos en los seres humanos?', 'Excreción', 'Digestión', 'Respiración', 'Sudoración'], ['¿Cuál de las siguientes opciones es un órgano del sistema nervioso?', 'Cerebro', 'Páncreas', 'Hígado', 'Pulmón'], ['¿Cómo se llama un polígono de 3 lados?', 'Triángulo', 'Trapecio', 'Cuadrado', 'Isoseles'], ['¿Cuántos aristas tiene un cubo?', '12', '8', '16', '4'], ['¿Qué es un fotón?', 'Una partícula de luz', 'Una partícula de sonido', 'Una partícula de calor', 'Una partícula de materia'], ['¿Cuál es el nombre del O2 en términos comunes?', 'Oxígeno', 'Ozono', 'Monóxido de carbono', 'Dióxido de carbono'], ['¿Cuál es el nombre del HCl en términos comunes?', 'Ácido clorhídrico', 'Ácido sulfúrico', 'Agua', 'Aire'], ['¿Cuál de los siguientes no es un ejemplo de organismo unicelular?', 'Insecto', 'Bacteria', 'Protozoo', 'Alga'], ['¿Qué antiguo general griego es conocido por haber tenido un ojo tuerto?', 'Filipo II de Macedonia', 'Alejandro Magno', 'Leónidas de Esparta', 'Pericles'], ['¿En qué unidad se mide la energía?', 'Joules', 'Amperios', 'Ohmios', 'Wattios'], ['¿Cuál es la capital de España?', 'Madrid', 'Barcelona', 'Valencia', 'Sevilla'], ['¿Cómo se llama un polígono con todos los lados y ángulos iguales?', 'Regular', 'Idéntico', 'Simétrico', 'Irregular'], ['¿En qué país tuvo lugar la Revolución de los Claveles en 1974?', 'Portugal', 'Francia', 'Rusia', 'China'], ['¿En qué año se abolió oficialmente la esclavitud en los Estados Unidos?', '1863', '1866', '1870', '1850'], ['¿Cuál es la función principal del sistema respiratorio en los seres humanos?', 'Obtener oxígeno y eliminar dióxido de carbono', 'Regular la temperatura corporal', 'Transportar nutrientes y desechos', 'Filtrar la sangre y eliminar toxinas'], ['¿Qué elemento químico tiene el símbolo Au, derivado del latín "aurum"?', 'Oro', 'Plata', 'Cobre', 'Hierro'], ['¿A qué grupo pertenecen los metales alcalinos en la tabla periódica?', 'Grupo 1', 'Grupo 2', 'Grupo 3', 'Grupo 4'], ['¿En qué unidad se mide la potencia eléctrica?', 'Wattios', 'Amperios', 'Ohmios', 'Voltios'], ['¿De qué países es frontera el Monte Everest?', 'Nepal y China', 'China e India', 'Nepal e India', 'Butan y China'], ['¿Cuál es la fórmula química del azúcar común?', 'C12H22O11', 'C6H12O6', 'C2H5OH', 'C12H22O12'], ['¿Cuánto es el 15% de 200?', '30', '15', '40', '60'], ['¿Qué ciudad sirvió como la última capital del Imperio Romano de Occidente?', 'Rávena', 'Roma', 'Constantinopla', 'Atenas'], ['¿Qué líder vietnamita lideró a Vietnam en la Guerra de Vietnam?', 'Ho Chi Minh', 'Ngo Dinh Diem', 'Vo Nguyen Giap', 'Le Duan'], ['¿Cuántos grados suman los ángulos internos de un triángulo?', '180°', '360°', '90°', '270°'], ['¿Cómo se llama la reacción química que libera energía en forma de calor?', 'Exotérmica', 'Endotérmica', 'Reacción redox', 'Fotosíntesis'], ['La gravedad es una...', 'Fuerza de atracción', 'Fuerza de repulsión', 'Fuerza de inercia', 'Fuerza de fricción'], ['¿Qué indica el número atómico de un elemento?', 'El número de protones', 'El número de electrones', 'El número de neutrones', 'La masa atómica'], ['¿Dónde se encuentra el Coliseo?', 'Roma', 'Atenas', 'Londres', 'París'], ['¿En qué año comenzó la Revolución Francesa?', '1789', '1776', '1799', '1804'], ['¿Cuál es el elemento más abundante en el cuerpo humano?', 'Oxígeno', 'Carbono', 'Hidrógeno', 'Nitrógeno'], ['¿Cómo se llama el enlace químico formado por la transferencia de electrones?', 'Enlace iónico', 'Enlace covalente', 'Enlace metálico', 'Enlace de hidrógeno']]
# Reordena las sublistas dentro del array principal
#random.shuffle(mi_array)

#print(mi_array)

#flat_array = [item for sublist in mi_array for item in sublist]

# Agrupar en grupos de 33 elementos cada uno
grouped_array = [mi_array[n:n+33] for n in range(0, len(mi_array), 33)]

print(grouped_array)