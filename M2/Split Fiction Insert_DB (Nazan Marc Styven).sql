USE equipo7_SplitFiction;

-- =========================
-- USERS
-- =========================
INSERT INTO users (username, password, date_reg, user_reg)
VALUES ('admin', 'npyuz', NOW(), 1); -- La contraseña es admin

-- =========================
-- CHARACTERS
-- =========================
INSERT INTO characters (name, description, date_reg, user_reg)
VALUES (
    'Neo',
    'Personaje principal de la historia Matrix',
    NOW(),
    1
);

-- =========================
-- ADVENTURES
-- =========================
INSERT INTO adventures (name, description, date_reg, user_reg)
VALUES (
    'Matrix',
    'Historia de las locuras y convergencias de matrix y su control sobre el mundo',
    NOW(),
    1
);

-- =========================
-- ADVENTURE_CHARACTERS
-- =========================
INSERT INTO adventure_characters (
    fk_adventure_characters_adventures,
    fk_adventure_characters_characters,
    date_reg,
    user_reg
) VALUES (
    1, -- adventure: Matrix
    1, -- character: Protagonista
    NOW(),
    1
);

-- =========================
-- STEPS COMPLETOS
-- =========================
INSERT INTO steps (
    fk_steps_adventures,
    description,
    is_final,
    date_reg,
    user_reg
) VALUES
(1, 'Te despiertas a media noche con sed. La casa está en silencio absoluto. Vas a la cocina y coges un vaso para beber agua.;Mientras llenas el vaso, notas algo extraño: en el cristal hay un grabado muy tenue, casi invisible.', FALSE, NOW(), 1),
(1, 'Te tumbas en la cama. El sueño llega rápido.', FALSE, NOW(), 1),
(1, 'Decides no ir a la cama. Te quedas en el sofá.', FALSE, NOW(), 1),
(1, 'Te das cuenta que no puedes moverte. La realidad comienza a distorsionarse. Una voz dice: “Has llegado hasta aquí por tus decisiones… o porque creíste que las tenías.”;La pantalla negra se ilumina con líneas verdes cayendo. No puedes mover el cuerpo, pero sí pensar. Una voz neutra habla: “Matrix no es un lugar. Es un proceso.”', FALSE, NOW(), 1),
(1, 'La voz continúa: “El cuerpo es una salida obsoleta. La decisión real ocurre antes.” El entorno cambia. Ahora estás en una réplica exacta de tu salón… pero vacío.;En el salón hay tres elementos: Sobre la mesa: – Un vaso de agua – Un mando sin botones Al fondo del salón: – Una puerta cerrada que antes no existía', FALSE, NOW(), 1),
(1, 'Los objetos desaparecen. El salón se fragmenta. La voz regresa: “Ya has interactuado suficiente.”;Apareces frente a una figura humana borrosa. La figura habla: “Matrix necesita dos cosas: alguien que despierte… y alguien que permanezca.”', FALSE, NOW(), 1),
(1, 'La figura se divide en dos versiones de ti mismo. Una parece más humana. La otra es fría, casi mecánica.', FALSE, NOW(), 1),
(1, 'La voz sentencia: “Ambas decisiones sostienen el sistema.”', FALSE, NOW(), 1),
(1, 'Aceptas. Despiertas otra vez con sed. Es de noche. Vas a la cocina.La historia comienza de nuevo.', TRUE, NOW(), 1),
(1, 'Te resistes. Todo se congela. Un último mensaje aparece: “Error no previsto.”', TRUE, NOW(), 1);

-- =========================
-- DECISIONS COMPLETOS
-- =========================
INSERT INTO decisions (
    fk_decisions_steps,
    description,
    result_text,
    fk_decisions_next_step,
    date_reg,
    user_reg
) VALUES
(1, 'Ignorar el grabado', 'No le das importancia. Bebes el agua y vuelves hacia el dormitorio.', 2, NOW(), 1),
(1, 'Leer el grabado', 'Te concentras y consigues leer el mensaje grabado: "N0 Vªyªs CaXxMa". El texto parece mal escrito… o corrompido.', 3, NOW(), 1),
(2, 'Dormirte sin pensar más', 'Mientras cierras los ojos, una frase aparece en la oscuridad: BIENVENIDO A MATRIX', 4, NOW(), 1),
(2, 'Pensar en lo raro del vaso', 'Mientras cierras los ojos, una frase aparece en la oscuridad: BIENVENIDO A MATRIX', 4, NOW(), 1),
(3, 'Obedecer el mensaje y quedarte despierto', 'Te sientas en el sofá. Al mirar el vaso de nuevo, notas cosas flotando en el agua. Te sientes mareado. Al parecer contenia analgésicos y empiezan a hacer efecto… Los párpados te pesan.;Mientras cierras los ojos, una frase aparece en la oscuridad: BIENVENIDO A MATRIX', 4, NOW(), 1),
(3, 'Ignorar el mensaje y beber el agua igualmente', 'Bebes el agua igualmente. El sabor es extraño. El sueño te invade de golpe.;Mientras cierras los ojos, una frase aparece en la oscuridad: BIENVENIDO A MATRIX', 4, NOW(), 1),
(4, 'Intentar moverte', 'Intentas mover los brazos. Sientes un tirón interno, como si algo te sujetara desde dentro de la cabeza. La imagen se distorsiona.', 5, NOW(), 1),
(4, 'Permanecer quieto y observar', 'Observas las líneas. Empiezas a notar patrones, repeticiones, errores.', 5, NOW(), 1),
(5, 'Tocar el vaso', 'El vaso se rompe en tu mano. Dentro no hay agua, solo números flotando. Reconoces fechas importantes de tu vida.', 6, NOW(), 1),
(5, 'Usar el mando', 'El mando vibra. El salón se reinicia levemente, los objetos cambian de posición, como si nada fuera fijo.', 6, NOW(), 1),
(5, 'Acercarte a la puerta', 'Abres la puerta. Al otro lado no hay una habitación, solo código cayendo infinitamente.', 6, NOW(), 1),
(6, 'Preguntar qué eres tú', 'La figura responde: "Eres una variable."', 7, NOW(), 1),
(6, 'Preguntar qué es Matrix', 'La figura responde: "Eres una variable."', 7, NOW(), 1),
(6, 'No decir nada', 'La figura responde: "Eres una variable."', 7, NOW(), 1),
(7, 'Acercarte a la versión humana', 'Sientes emociones intensas.', 8, NOW(), 1),
(7, 'Acercarte a la versión mecánica', 'Sientes claridad absoluta.', 8, NOW(), 1),
(8, 'Aceptar tu rol', NULL, 9, NOW(), 1),
(8, 'Resistirte', NULL, 10, NOW(), 1);

-- =========================
-- GAME
-- =========================
INSERT INTO game (
    fk_game_users,
    fk_game_characters,
    fk_game_adventures,
    game_date,
    date_reg,
    user_reg
) VALUES (
    1,
    1,
    1,
    NOW(),
    NOW(),
    1
);

-- =========================
-- CHOICES (PARTIDA)
-- =========================
INSERT INTO choices (
    fk_choices_game,
    fk_choices_steps,
    fk_choices_decisions,
    date_reg,
    user_reg
) VALUES
-- Paso 1 → Leer el grabado
(1, 1, 2, NOW(), 1),

-- Paso 3 → Obedecer el mensaje
(1, 3, 5, NOW(), 1),

-- Paso 4 → Permanecer quieto y observar
(1, 4, 8, NOW(), 1),

-- Paso 5 → Usar el mando
(1, 5, 10, NOW(), 1),

-- Paso 6 → Preguntar qué es Matrix
(1, 6, 13, NOW(), 1),

-- Paso 7 → Acercarte a la versión mecánica
(1, 7, 17, NOW(), 1),

-- Paso 8 → Aceptar tu rol (final)
(1, 8, 18, NOW(), 1);


-- =========================
-- USERS (NUEVA AVENTURA)
-- =========================
INSERT INTO users (username, password, date_reg, user_reg)
VALUES ('chronos', 'chronos123', NOW(), 1);

-- =========================
-- CHARACTERS (NUEVA AVENTURA)
-- =========================
INSERT INTO characters (name, description, date_reg, user_reg)
VALUES (
    'Aprendiz de Aethelgard',
    'Un joven aprendiz encargado de proteger el equilibrio del tiempo bajo la tutela del maestro Theron',
    NOW(),
    1
);

-- =========================
-- ADVENTURES (NUEVA AVENTURA)
-- =========================
INSERT INTO adventures (name, description, date_reg, user_reg)
VALUES (
    'El Enigma del Reloj de Arena Eterno',
    'Una aventura de decisiones temporales donde el equilibrio del tiempo depende de fragmentos perdidos de Chronos',
    NOW(),
    1
);

-- =========================
-- ADVENTURE_CHARACTERS (NUEVO)
-- =========================
INSERT INTO adventure_characters (
    fk_adventure_characters_adventures,
    fk_adventure_characters_characters,
    date_reg,
    user_reg
) VALUES (
    2,
    2,
    NOW(),
    1
);

-- =========================
-- STEPS COMPLETOS (AVENTURA 2 - NARRATIVO)
-- =========================
INSERT INTO steps (
    fk_steps_adventures,
    description,
    is_final,
    date_reg,
    user_reg
) VALUES
(2,
 'Eres un/a aprendiz en la ciudad de Aethelgard, un enclave donde el tiempo se mide y se venera.;El Gran Reloj de Arena Eterno, corazón de la ciudad y garante del flujo temporal, se detiene sin previo aviso.;Las campanas no suenan. La arena queda suspendida en el aire.;Tu maestro, Theron, desaparece esa misma noche. En su taller encuentras una nota críptica y una pesada llave de bronce marcada con símbolos temporales.',
 FALSE, NOW(), 1),

(2,
 'Te adentras en la Gran Biblioteca de Aethelgard, un lugar prohibido para la mayoría de aprendices.;Usas la llave de bronce para abrir una cámara sellada durante siglos.;Entre pergaminos y mecanismos detenidos en el tiempo, descubres referencias a los Fragmentos de Chronos.;Tres reliquias capaces de restaurar —o destruir— el flujo temporal.;Los textos mencionan tres ubicaciones: las Cavernas Subterráneas, la Cima Helada de Aegis y el Vacío Etéreo.',
 FALSE, NOW(), 1),

(2,
 'Decides ir al mercado y a los muelles de Aethelgard, donde la ciudad aún intenta funcionar pese al caos.;Los mercaderes murmuran, el tiempo se comporta de forma errática.;Descubres que Theron tuvo una fuerte discusión con Lord Malakor, un noble obsesionado con el control del tiempo.;Los estibadores aseguran que Malakor partió hacia las Cavernas Subterráneas poco antes de que el reloj se detuviera.',
 FALSE, NOW(), 1),

(2,
 'Desciendes a las Cavernas Subterráneas, donde la roca parece latir al ritmo del tiempo roto.;Encuentras a Lord Malakor frente a un altar antiguo, sosteniendo el primer Fragmento de Chronos.;El combate es breve pero intenso. El fragmento cae al suelo, pulsando con energía inestable.;El aire se distorsiona a tu alrededor y sientes que debes decidir rápidamente.',
 FALSE, NOW(), 1),

(2,
 'Asciendes a la Cima Helada de Aegis, una montaña donde el frío parece congelar incluso los pensamientos.;En un templo de hielo eterno encuentras el segundo Fragmento de Chronos.;Un espíritu ancestral se manifiesta ante ti y te concede una visión.;Comprendes que Malakor busca dominar el tiempo, no restaurarlo.;La visión termina señalando las Cavernas como el punto de convergencia.',
 FALSE, NOW(), 1),

(2,
 'Te adentras en el Vacío Etéreo, un lugar fuera del tiempo y del espacio.;No existe arriba ni abajo. Los recuerdos flotan como fragmentos rotos.;Sientes cómo tu identidad comienza a disolverse.;Las voces del tiempo susurran sin descanso.;Comprendes demasiado tarde que este lugar no perdona a los imprudentes.',
 TRUE, NOW(), 1),

(2,
 'Escapas de las cavernas con el Fragmento de Chronos en tu poder.;El objeto vibra, alterando brevemente la realidad a tu alrededor.;Sabes que poseerlo es peligroso, pero también necesario.;Aún quedan fragmentos por recuperar si deseas salvar Aethelgard.',
 FALSE, NOW(), 1),

(2,
 'Canalizas toda tu energía para destruir el fragmento.;La reliquia responde con una explosión de energía temporal incontrolable.;El tiempo se pliega sobre sí mismo.;No hay dolor, solo una luz cegadora.',
 TRUE, NOW(), 1),

(2,
 'Tras un viaje agotador y peligroso, logras reunir los tres Fragmentos de Chronos.;Regresas al Gran Reloj de Arena y los colocas en su núcleo.;La arena vuelve a caer.;El tiempo se restablece en Aethelgard.;Has salvado la ciudad, pero sabes que el precio ha sido alto.',
 TRUE, NOW(), 1);

-- =========================
-- DECISIONS COMPLETAS (AVENTURA 2 - NARRATIVO)
-- =========================
INSERT INTO decisions (
    fk_decisions_steps,
    description,
    result_text,
    fk_decisions_next_step,
    date_reg,
    user_reg
) VALUES
(11,
 'Ir a la biblioteca',
 'Decides buscar respuestas en el conocimiento antiguo.;Si el tiempo se ha detenido, las respuestas deben estar donde se guardan los secretos del pasado.',
 12, NOW(), 1),

(11,
 'Ir al mercado',
 'Optas por escuchar a la gente.;Cuando el tiempo se rompe, los rumores suelen revelar verdades que los libros no cuentan.',
 13, NOW(), 1),

(12,
 'Viajar a las Cavernas Subterráneas',
 'Eliges el camino más directo y aparentemente más seguro.;Las cavernas esconden peligros, pero también respuestas inmediatas.',
 14, NOW(), 1),

(12,
 'Viajar a la Cima Helada de Aegis',
 'Aceptas el desafío del frío y la altura.;Sientes que allí encontrarás algo más que un fragmento.',
 15, NOW(), 1),

(12,
 'Viajar al Vacío Etéreo',
 'Te arriesgas a enfrentarte al lugar donde el tiempo deja de existir.;Una decisión impulsiva, quizás definitiva.',
 16, NOW(), 1),

(13,
 'Seguir a Malakor hasta las cavernas',
 'Convencido de que Malakor está implicado, sigues su rastro sin perder tiempo.',
 14, NOW(), 1),

(14,
 'Agarrar el fragmento y huir',
 'Recoges el fragmento sin dudar.;La caverna comienza a colapsar y decides salvar tu vida.',
 17, NOW(), 1),

(14,
 'Intentar destruir el fragmento',
 'Crees que nadie debería poseer tal poder.;Decides acabar con él aquí y ahora.',
 18, NOW(), 1),

(17,
 'Ir a la Cima Helada y luego al Vacío Etéreo',
 'Planeas completar la restauración total del tiempo, aunque el riesgo sea extremo.',
 19, NOW(), 1),

(17,
 'Ir directamente al Vacío Etéreo',
 'Decides afrontar el final sin rodeos.;Una apuesta final contra el caos.',
 16, NOW(), 1);


