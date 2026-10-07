import streamlit as st
import random

# 1. Configuración de la página web
st.set_page_config(page_title="Juego Previa", page_icon="🍻", layout="centered")

st.title("🍻 Juego de Previa")
st.markdown("### Elige tu castigo")

# --- 2. LISTAS DE PREGUNTAS (Originales + Nuevas) ---

hot_seat = [
    # Originales
    "¿Cuándo fue la última vez que mentiste y por qué?",
    "¿Qué es aquello que si te hacen/dicen y te vuelves más fácil que la tabla del 1?",
    "¿Tienes algún fetiche? ¿Cuál",
    "Situación más vergonzosa que viviste",
    "¿Cuál sería el lugar más extraño donde querrías tener relaciones?",
    "¿Has usado ropa interior sexy? ¿cómo era?",
    "Algo raro qué te atraiga de una persona",
    "Si tuvieras que besar a alguien que te cae mal, ¿cuál sería la razón más probable?",
    "¿Eres sumis@ o dominante?",
    "Experiencia más desastrosa en el amor",
    "¿Harías un trío?",
    "¿Eres de lanzarte tú o de que se lancen?",
    "¿Te arrepientes de estar/besar... con alguien?",
    "¿Fumar o beber?",
    "Edad más alta y más baja con quien te hayas besado",
    "¿Alguna vez has hecho llorar a alguien?",
    "¿Prefieres una relación o una aventura?",
    "¿Te gustan los motes cursis?",
    "¿Han roto contigo alguna vez?",
    "¿Te replanteaste tu orientación sexual alguna vez?",
    "¿Qué es lo más loco que has hecho por amor?",
    "¿Peor beso?",
    "Búsqueda más rara en internet",
    "¿Alguna vez has llorado por amor? ¿Por quién?",
    "¿Te consideras sentimental o frí@?",
    "¿Tu peor borrachera?",
    "¿Cosa que no volverías a hacer nunca?",
    "¿Soñaste con alguien de aquí?, si es sí, cuenta el último sueño",
    "¿Qué virtud crees que es la más importante en una pareja?",
    "¿Con cuánta gente te has liado?",
    "¿A quién de esta mesa le darías un beso ahora mismo si no hubiera consecuencias?",
    "¿Alguna vez has sido infiel (física o emocionalmente)?",
    "¿Cuál es tu mayor fantasía no cumplida?",
    "¿Alguna vez te has liado con el ex de un amigo/a?",
    "¿Qué es lo más ilegal que has hecho en tu vida?",
    # Nuevas
    "¿A qué edad tuviste tu primera experiencia sexual?",
    "¿Cuál es la parte de tu cuerpo que más te gusta? ¿Y la que menos?",
    "¿Has tenido alguna vez un 'amigo con derechos'?",
    "¿Alguna vez te has enamorado a primera vista de un desconocido?",
    "¿Qué es lo primero en lo que te fijas de una persona físicamente?",
    "¿Te han pillado alguna vez en un momento íntimo contigo mismo/a?",
    "¿Qué es lo más caro que has roto o perdido estando de fiesta?",
    "¿Alguna vez te has arrepentido de un beso justo en el momento de darlo?",
    "¿Crees en las segundas oportunidades después de unos cuernos?",
    "¿Cuál es tu red flag (bandera roja) más tóxica al empezar a conocer a alguien?",
    "¿A qué famoso o famosa revivirías solo para intentar tener una cita?",
    "¿Cuál es el mensaje de WhatsApp más humillante que has enviado y no pudiste borrar a tiempo?"
]

tribunal = [
    # Originales
    "Si tuvieras que emparejar obligatoriamente a dos personas de esta mesa, ¿quiénes serían y por qué?",
    "¿Quién de la mesa crees que tiene el peor gusto para elegir parejas o líos?",
    "Señala a la persona de la mesa que creas que es más probable que acabe en la cárcel.",
    "¿A quién de la mesa le confiarías tu mayor secreto y a quién NO le contarías nada?",
    "Del 1 al 10, puntúa el atractivo de la persona que está sentada justo a tu derecha.",
    "Si tuvieras que intercambiar tu vida con alguien de esta mesa por un día, ¿quién sería y qué es lo primero que harías?",
    "¿Quién de los presentes crees que miente más a menudo para quedar bien?",
    "¿Qué persona de la mesa crees que es la más 'fácil' de convencer para una locura?",
    "¿Quién de la mesa crees que es peor en la cama y qué te hace pensarlo?",
    "Si hubiera un apocalipsis zombie, ¿a quién de la mesa sacrificarías primero para tener tiempo de huir tú?",
    "¿Qué dos personas de esta mesa (que no sean pareja) crees que tendrían más química sexual?",
    "Señala a la persona de la mesa que crees que tiene los fetiches más raros u oscuros.",
    "¿A quién de la mesa NO le dejarías tu móvil desbloqueado durante 10 minutos bajo ningún concepto?",
    "¿Quién crees que es el más 'fantasma' (el que más presume o exagera) del grupo?",
    "Si solo pudieras salvar a una persona de esta mesa de un incendio, ¿quién sería? (Mójate y elige solo a uno).",
    "¿Quién de aquí crees que ha sido más infiel en su vida, aunque no nos lo haya contado nunca?",
    "Confiesa: ¿cuál es la peor primera impresión que tuviste de la persona que tienes ahora mismo a tu izquierda?",
    "¿Quién de la mesa crees que es más superficial a la hora de elegir a alguien para liarse?",
    "Si tuvieras que apostar dinero, ¿quién de nosotros crees que será el primero en divorciarse en el futuro?",
    "¿Quién crees que es el más rencoroso de la mesa, ese que nunca olvida una mala jugada?",
    # Nuevas
    "¿Quién de la mesa tiene más probabilidades de acabar metido en una secta o estafa piramidal?",
    "¿Quién crees que liga menos en una noche de fiesta normal y por qué?",
    "Si tuvieras que prestarle 1.000€ a alguien de aquí y estar seguro de que te los devuelva, ¿a quién elegirías y a quién descartarías al instante?",
    "¿Quién de la mesa tiene más pinta de cotillear las redes sociales de sus ex desde una cuenta secundaria?",
    "¿A quién de los presentes te imaginas teniendo una doble vida secreta?",
    "¿Quién crees que tiene el historial de búsquedas de internet más turbio del grupo?",
    "¿A quién de la mesa le confiarías la organización de tu despedida de soltero/a y a quién se lo prohibirías rotundamente?",
    "¿Quién de la mesa crees que tiene el gusto musical más vergonzoso en la intimidad?",
    "Si tuvieras que convivir un año entero en una casa enana con alguien de la mesa, ¿quién sería tu última opción?",
    "¿Quién crees que es la persona más 'drama queen' o exagerada del grupo cuando bebe de más?",
    "¿A quién de aquí ves capaz de liarse con alguien solo por interés (conseguir un favor, dinero, subir nota, etc.)?",
    "Señala a la persona que crees que tarda más en superar una ruptura amorosa."
]

yo_nunca = [
    # Originales
    "Yo nunca he mandado un mensaje a mi ex estando borracho/a.",
    "Yo nunca he fingido que me llamaban por teléfono para escapar de una cita.",
    "Yo nunca me he liado con más de una persona en la misma noche.",
    "Yo nunca me he sentido atraído/a por un profesor/a o jefe/a.",
    "Yo nunca he ghosteado a alguien que me gustaba.",
    "Yo nunca he dicho 'te quiero' sin sentirlo realmente.",
    "Yo nunca me he colado en una fiesta a la que no estaba invitado/a.",
    "Yo nunca he borrado mensajes de mi móvil para que nadie los viera.",
    "Yo nunca me he despertado sin recordar cómo llegué a mi cama.",
    "Yo nunca he fingido un orgasmo.",
    "Yo nunca he dicho el nombre de otra persona por error mientras me estaba liando (o más) con alguien.",
    "Yo nunca he cotilleado el móvil de mi pareja a escondidas.",
    "Yo nunca me he liado con el hermano o la hermana de un amigo/a.",
    "Yo nunca he enviado un vídeo o foto subida de tono (nude) a la persona equivocada.",
    "Yo nunca he estado con alguien solo para darle celos a otra persona.",
    "Yo nunca me he acostado con un compañero de trabajo o de clase.",
    "Yo nunca me he sentido atraído/a por la pareja de alguien de esta mesa.",
    "Yo nunca he llorado borracho/a en un baño público de una discoteca o bar.",
    "Yo nunca he vomitado de fiesta y, justo después, he seguido bebiendo como si nada.",
    "Yo nunca he mentido sobre mi 'número' (la cantidad de personas con las que me he acostado).",
    "Yo nunca me he escapado de una cita desastrosa poniendo una excusa falsa (como que mi amiga estaba enferma).",
    "Yo nunca me he liado con alguien mucho mayor que yo (más de 10 años de diferencia).",
    "Yo nunca he buscado el Instagram del ex de mi actual rollo/pareja para compararme.",
    # Nuevas
    "Yo nunca he bloqueado a alguien y luego lo he desbloqueado solo para ver si había cambiado su foto de perfil.",
    "Yo nunca me he inventado que tenía pareja para que me dejaran en paz en una discoteca.",
    "Yo nunca he dicho 'estoy llegando' cuando ni siquiera había salido de la ducha.",
    "Yo nunca me he reído a carcajadas en un momento totalmente inapropiado o serio.",
    "Yo nunca he creado una cuenta falsa en redes sociales para espiar a alguien.",
    "Yo nunca he hecho un 'simpa' (irse sin pagar) en un bar, restaurante o taxi.",
    "Yo nunca me he hecho el dormido (o la dormida) para evitar hablar con alguien en persona.",
    "Yo nunca he criticado a un amigo a sus espaldas por algo que yo también hago en secreto.",
    "Yo nunca he intentado ligar con el camarero o camarera para conseguir chupitos gratis.",
    "Yo nunca me he arrepentido de un corte de pelo, piercing o tatuaje al día siguiente de hacérmelo.",
    "Yo nunca he usado la ropa sucia del cesto (o le he dado la vuelta a la ropa interior) porque me daba pereza lavar.",
    "Yo nunca he fingido saber sobre un tema (cine, música, política) solo para impresionar a la persona que me gustaba.",
    "Yo nunca he borrado a alguien de una foto de grupo antes de subirla a mis redes sociales."
]

verdad = [
    # Originales
    "¿Qué es lo más ridículo o humillante que has hecho para llamar la atención de alguien que te gustaba?",
    "¿Alguna vez te has sentido atraído/a por algún amigo/a de tu pareja actual o pasada?",
    "Si pudieras borrar mágicamente de tu memoria a una persona con la que te has liado o acostado, ¿quién sería y por qué?",
    "¿Cuál es la mentira más grande que has contado para librarte de una cita o de tener relaciones con alguien?",
    "¿Tienes alguna foto en tu galería del móvil que te arruinaría la reputación si se hiciera pública? (Sin enseñarla, solo explica de qué trata).",
    "¿Alguna vez has pillado a alguien de tu familia o a un amigo en un momento íntimo?",
    "¿Cuál es el sitio web o la búsqueda de internet más vergonzosa que tienes en tu historial reciente?",
    "Del 1 al 10, ¿qué nota le pondrías a tu última experiencia sexual y por qué bajaste (o subiste) puntos?",
    "¿Alguna vez has dudado de tu relación actual (o de tu última relación seria) estando de fiesta?",
    "Si tuvieras luz verde para revisar el móvil de cualquier persona de esta mesa durante 2 minutos, ¿de quién sería y qué buscarías primero?",
    "¿Alguna vez has ensayado un beso en el espejo o con tu propia mano?",
    "¿Cuál es el rumor más fuerte o falso que has escuchado sobre ti mismo/a?",
    "¿Alguna vez te han pillado teniendo relaciones en un lugar público? ¿Dónde fue?",
    "Si tuvieras que pasar 24 horas encerrado/a en una habitación con alguien de esta mesa, ¿a quién elegirías y qué haríais?",
    "¿Cuál es la peor excusa que has puesto en el último momento para cancelar una cita?",
    "¿Alguna vez has robado algo en una tienda, por muy pequeño que fuera?",
    "¿Qué es lo más ridículo o humillante que has hecho estando borracho/a frente a alguien que te gustaba?",
    "¿Has tenido alguna vez un 'sueño húmedo' o fantasía con la pareja de un amigo/a?",
    "¿Cuál es el secreto que te llevarías a la tumba y que hoy vas a confesar a medias?",
    "¿A qué persona de este grupo le darías un 'pase libre' de una noche sin hacer preguntas?",
    # Nuevas
    "¿Cuál es la peor mentira que le has dicho a tus padres y que a día de hoy aún se creen?",
    "Si pudieras leer la mente de una persona de esta mesa durante un minuto, ¿de quién sería?",
    "¿Qué es lo más vergonzoso que tienes escondido en tu habitación ahora mismo?",
    "¿Has sentido envidia o celos alguna vez de la relación sentimental de algún amigo/a tuyo?",
    "¿Cuál es la 'cobra' o rechazo amoroso que más te ha humillado en la vida?",
    "¿Has stalkeado (espiado a fondo) alguna vez el perfil de la nueva pareja o rollo de tu ex?",
    "¿Qué es lo más infantil o ridículo que sigues haciendo a tu edad y que casi nadie sabe?",
    "¿Cuál es la pelea más absurda por la que dejaste de hablarle a alguien durante un tiempo?",
    "¿Alguna vez has vendido, tirado o regalado algo que te dio alguien de esta mesa?",
    "Confiesa un prejuicio muy feo que tenías sobre alguien de este grupo antes de conocerlo bien."
]

reto = [
    # Originales
    "Deja que la persona a tu derecha envíe un mensaje de texto o WhatsApp desde tu móvil a la persona que tú elijas.",
    "Llama a tu ex (o a tu último rollo) y dile que te has acordado de él/ella. Si no contesta, deja un mensaje de voz.",
    "Ponte la ropa interior por encima de los pantalones durante los próximos 3 turnos.",
    "Enseña al grupo las últimas 3 fotos ocultas o eliminadas de tu móvil.",
    "Hazle un baile sensual (twerking, perreo, striptease cómico) a la persona de la mesa que elija el grupo durante 30 segundos.",
    "Deja que alguien del grupo te haga un 'tatuaje' en la cara o en el brazo con un bolígrafo.",
    "Habla con un acento extranjero exagerado (francés, argentino, italiano...) hasta que vuelva a ser tu turno. Si se te olvida y hablas normal, bebes.",
    "Dale un masaje en los hombros y el cuello de 1 minuto a la persona que esté a tu izquierda.",
    "Publica la foto más fea que tengas tuya ahora mismo en tus historias de Instagram o estado de WhatsApp y déjala al menos 1 hora.",
    "Imita el orgasmo o la cara de placer de la persona que tienes enfrente.",
    "Bébete tu próximo trago o chupito sin usar las manos (como en la casilla 39 del tablero).",
    "Intercambia una prenda de ropa con la persona que tienes a tu derecha y llévala puesta durante 3 turnos (inspirado en la casilla 20).",
    "Deja que el grupo te prepare un 'brebaje' mezclando un poco de todo lo que hay en la mesa y dale un trago.",
    "Hazle un 'chupetón' falso en el cuello (o dale un beso sonoro) a la persona que tienes a tu izquierda.",
    "Dale tu móvil desbloqueado a la persona de enfrente para que envíe un mensaje de voz de 10 segundos a uno de tus padres.",
    "Intenta ligar con un objeto inanimado de la sala (una silla, un vaso, la puerta) durante 1 minuto sin reírte.",
    "Cómete un snack o bebe un trago directamente de las manos de otro jugador, sin usar las tuyas.",
    "Haz 10 flexiones o sentadillas mientras recitas los nombres de los ex que recuerdes de la persona a tu derecha.",
    "Déjate vendar los ojos y adivina quién de la mesa te está tocando la cara. Si fallas, bebes.",
    "Siéntate en el regazo de la persona que elija el grupo hasta que vuelva a ser tu turno.",
    # Nuevos
    "Habla susurrando de manera muy cerca en la oreja de la persona a tu derecha cada vez que te toque hablar durante los próximos 2 turnos.",
    "Manda un audio cantando a pleno pulmón el estribillo de tu canción favorita al último grupo de WhatsApp en el que hablaste.",
    "Déjate hacer un peinado ridículo por la persona que tienes a tu izquierda usando agua, servilletas o lo que haya en la mesa.",
    "Imita a un animal (el grupo elige cuál) durante 30 segundos de la forma más dramática y realista posible.",
    "Intercambia tu bebida con la persona que tienes enfrente y da un trago grande a lo que sea que esté bebiendo.",
    "Deja que la persona a tu derecha te haga una foto vergonzosa (papada, haciendo el tonto, etc.) y ponla de fondo de pantalla hasta que acabe la partida.",
    "Intenta lamerte el codo. Si no llegas, bebes tú; si lo logras, mandas beber a dos personas de la mesa.",
    "Habla sin mover los labios (como un ventrílocuo) hasta que vuelva a ser tu turno. Si abres la boca para hablar, bebes.",
    "Mete un cubito de hielo en tu boca e intenta pasarlo a la boca de otro jugador que acepte. Si nadie acepta el reto contigo, bébete tu vaso de un trago.",
    "Escribe 'Estoy embarazada' o 'Voy a ser papá' en tu estado de WhatsApp durante los próximos 15 minutos."
]

# --- 3. DISEÑO DE BOTONES Y LÓGICA ---
st.markdown("---")

# Fila 1: Dos botones
col1, col2 = st.columns(2)
with col1:
    if st.button("🔥 Hot Seat", use_container_width=True):
        st.success(f"**¡Hot Seat!**\n\n{random.choice(hot_seat)}")
with col2:
    if st.button("⚖️ Tribunal", use_container_width=True):
        st.warning(f"**¡Tribunal!**\n\n{random.choice(tribunal)}")

# Fila 2: Dos botones
col3, col4 = st.columns(2)
with col3:
    if st.button("🙈 Yo Nunca", use_container_width=True):
        st.info(f"**¡Yo Nunca!**\n\n{random.choice(yo_nunca)}")
with col4:
    if st.button("🎭 Verdad", use_container_width=True):
        st.error(f"**¡Verdad!**\n\n{random.choice(verdad)}")

# Fila 3: Reto (Ocupa todo el ancho abajo para destacar)
if st.button("🎯 Reto", use_container_width=True):
    st.error(f"**¡Reto!**\n\n{random.choice(reto)}")
