use split_fiction;

-- Informe 1: Resposta més usada

SELECT 
    a.name AS "ID AVENTURA - NOMBRE",
    s.id_steps AS "ID Paso",
    s.description AS "PASO DESCRIPCION",
    d.description AS "RESPUESTAS",
    COUNT(c.id_choices) AS "NUMERO VECES SELECCIONADA"
FROM choices c
JOIN decisions d ON c.fk_choices_decisions = d.id_decisions
JOIN steps s ON c.fk_choices_steps = s.id_steps
JOIN adventures a ON s.fk_steps_adventures = a.id_adventures
GROUP BY a.name, s.id_steps, d.description
ORDER BY a.name ASC, "NUMERO VECES SELECCIONADA" DESC;

-- Informe 2: Jugador que més vegades ha jugat

SELECT 
    u.username AS "PLAYER NAME",
    COUNT(g.id_game) AS "GAMES PLAYED",
    u.date_reg AS "REGISTRATION DATES"
FROM users u
JOIN game g ON u.id_users = g.fk_game_users
GROUP BY u.id_users
ORDER BY 
    "GAMES PLAYED" DESC, -- Primero el que más ha jugado
    u.date_reg ASC;           -- Si hay empate, el que se registró antes (más antiguo)

-- Informe 3: Quantes aventures ha jugat l'usuari X

SELECT 
    a.id_adventures AS idadventure,
    a.name AS "Name",
    MAX(g.game_date) AS "date"
FROM game g
JOIN users u ON g.fk_game_users = u.id_users
JOIN adventures a ON g.fk_game_adventures = a.id_adventures
WHERE u.username = "admin"
GROUP BY a.id_adventures, a.name
ORDER BY "date" DESC;