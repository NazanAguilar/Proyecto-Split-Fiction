
-- =========================
-- NOUS USUARIS
-- =========================
INSERT INTO users (username, password, data_alta, usuari_alta)
SELECT 'Marc', '1234', NOW(), (SELECT COUNT(*) + 1 FROM users) UNION ALL
SELECT 'Styven', '1234', NOW(), (SELECT COUNT(*) + 1 FROM users) UNION ALL
SELECT 'Nazan', '1234', NOW(), (SELECT COUNT(*) + 1 FROM users);

-- =========================
-- NOUS PERSONATJES
-- =========================
INSERT INTO characters (name, description, data_alta, usuari_alta)
VALUES
('Pepe', 'Guerrer llegendari de la mitologia nòrdica', NOW(), 1),
('Pato Lucas', 'Un ànec sarcàstic i valent', NOW(), 1);

-- =========================
-- NOVES AVENTURES
-- =========================
INSERT INTO adventures (name, description, data_alta, usuari_alta)
VALUES
('El Laberint de les Ombres', 'Un laberint viu que canvia de forma i manipula la ment.', NOW(), 1);

-- =========================
-- NOUS PERSONATJES D'AVENTURES
-- =========================
INSERT INTO adventure_characters 
(fk_adventure_characters_adventures, fk_adventure_characters_characters, data_alta, usuari_alta)
VALUES
(1, 1, NOW(), 1),
(1, 2, NOW(), 1);

-- =========================
-- NOUS PASSOS
-- =========================
INSERT INTO steps (fk_steps_adventures, description, is_final, data_alta, usuari_alta)
VALUES
(1, 'Et trobes en un passadís fosc, només il·luminat per una torxa flotant.', FALSE, NOW(), 1), -- ID 1
(1, 'La torxa revela dues portes: una vibra i l’altra xiuxiueja.', FALSE, NOW(), 1),             -- ID 2
(1, 'Una ombra gegant et devora i tot es torna negre.', TRUE, NOW(), 1);                        -- ID 3

-- =========================
-- NOVES DECISIONS
-- =========================
INSERT INTO decisions 
(fk_decisions_steps, fk_decisions_next_step, description, result_text, data_alta, usuari_alta)
VALUES
(1, 2, 'Agafar la torxa flotant', 'La torxa t’eleva i et mostra dues portes inquietants.', NOW(), 1), -- ID 1
(1, 3, 'Correr cap a la foscor', 'L’ombra et captura abans que puguis reaccionar.', NOW(), 1),        -- ID 2
(2, 3, 'Obrir la porta vibrant', 'Una ona de xoc et colpeja i tot s’esvaeix.', NOW(), 1),              -- ID 3
(2, 3, 'Obrir la porta que xiuxiueja', 'Les veus t’engolen dins un buit infinit.', NOW(), 1);          -- ID 4

-- =========================
-- NOU JOC
-- =========================
INSERT INTO game 
(fk_game_users, fk_game_characters, fk_game_adventures, game_date, data_alta, usuari_alta)
VALUES
(1, 2, 1, '2023-10-12 14:23:40', NOW(), 1); -- ID 1

-- =========================
-- NOVES ELECCIONS
-- =========================
INSERT INTO choices 
(fk_choices_game, fk_choices_steps, fk_choices_decisions, data_alta, usuari_alta)
VALUES
(1, 1, 1, NOW(), 1),
(1, 2, 3, NOW(), 1);
