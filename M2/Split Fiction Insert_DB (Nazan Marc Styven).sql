USE Split_Fiction;

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
    'Protagonista',
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
    'Historia interactiva basada en decisiones, convergencias y control',
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
-- CHOICES
-- =========================
INSERT INTO choices (
    fk_choices_game,
    fk_choices_steps,
    fk_choices_decisions,
    date_reg,
    user_reg
) VALUES
(1, 1, 2, NOW(), 1),
(1, 2, 3, NOW(), 1),
(1, 3, 5, NOW(), 1);
