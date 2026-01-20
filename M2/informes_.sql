use split_fiction;

-- Informe 1: Resposta més usada

SELECT 
    a.name AS Aventura,
    s.id_steps AS ID_Paso,
    LEFT(s.description, 50) AS Resumen_Paso,
    d.description AS Accion_Para_Escoger,
    COUNT(c.id_choices) AS Veces_Seleccionada
FROM choices c
JOIN decisions d ON c.fk_choices_decisions = d.id_decisions
JOIN steps s ON c.fk_choices_steps = s.id_steps
JOIN adventures a ON s.fk_steps_adventures = a.id_adventures
GROUP BY a.name, s.id_steps, d.description
ORDER BY a.name ASC, Veces_Seleccionada DESC;

-- Informe 2: Jugador que més vegades ha jugat

SELECT 
    u.username AS Jugador,
    COUNT(g.id_game) AS Numero_de_Partidas,
    u.date_reg AS Fecha_Registro
FROM users u
JOIN game g ON u.id_users = g.fk_game_users
GROUP BY u.id_users
ORDER BY 
    Numero_de_Partidas DESC, -- Primero el que más ha jugado
    u.date_reg ASC           -- Si hay empate, el que se registró antes (más antiguo)
LIMIT 1;

-- Informe 3: Quantes aventures ha jugat l'usuari X

SELECT 
    a.id_adventures AS ID_Aventura,
    a.name AS Aventura,
    MAX(g.game_date) AS Ultima_Vez_Jugada
FROM game g
JOIN users u ON g.fk_game_users = u.id_users
JOIN adventures a ON g.fk_game_adventures = a.id_adventures
WHERE u.username = "admin"
GROUP BY a.id_adventures, a.name
ORDER BY Ultima_Vez_Jugada DESC;