-- =========================
-- INFORME 1
-- =========================
SELECT 
    a.name AS aventura,
    s.id_steps AS id_pas,
    s.description AS descripcio_pas,
    d.id_decisions AS id_decisio,
    d.description AS accio,
    COUNT(c.id_choices) AS cops_triada
FROM adventures a
JOIN steps s ON s.fk_steps_adventures = a.id_adventures
JOIN decisions d ON d.fk_decisions_steps = s.id_steps
LEFT JOIN choices c ON c.fk_choices_decisions = d.id_decisions
GROUP BY a.id_adventures, s.id_steps, d.id_decisions
ORDER BY a.name, s.id_steps, cops_triada DESC;

-- =========================
-- INFORME 2
-- =========================
SELECT 
    u.username,
    COUNT(g.id_game) AS partides_jugades,
    MIN(g.game_date) AS primer_cop_jugat
FROM users u
JOIN game g ON g.fk_game_users = u.id_users
GROUP BY u.id_users
ORDER BY partides_jugades DESC, primer_cop_jugat ASC
LIMIT 1;


-- =========================
-- INFORME 3
-- =========================
SELECT
    a.id_adventures AS idadventure,
    a.name AS Name,
    g.game_date AS date
FROM game g
JOIN adventures a ON g.fk_game_adventures = a.id_adventures
JOIN users u ON g.fk_game_users = u.id_users
WHERE u.username = 'rafa'
ORDER BY g.game_date DESC;

