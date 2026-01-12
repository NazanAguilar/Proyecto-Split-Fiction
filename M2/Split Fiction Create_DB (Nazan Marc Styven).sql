CREATE DATABASE IF NOT EXISTS Split_Fiction;
USE Split_Fiction;

-- =========================
-- USERS
-- =========================
CREATE TABLE users (
    id_users INT UNSIGNED,
    username VARCHAR(50),
    password VARCHAR(255),
    data_alta DATETIME,
    usuari_alta INT,
    data_mod DATETIME,
    usuari_mod INT
);

-- =========================
-- CHARACTERS
-- =========================
CREATE TABLE characters (
    id_characters INT UNSIGNED,
    name VARCHAR(100),
    description TEXT,
    data_alta DATETIME,
    usuari_alta INT,
    data_mod DATETIME,
    usuari_mod INT
);

-- =========================
-- ADVENTURES
-- =========================
CREATE TABLE adventures (
    id_adventures INT UNSIGNED,
    name VARCHAR(150),
    description TEXT,
    data_alta DATETIME,
    usuari_alta INT,
    data_mod DATETIME,
    usuari_mod INT
);

-- =========================
-- ADVENTURE_CHARACTERS
-- =========================
CREATE TABLE adventure_characters (
    id_adventure_characters INT UNSIGNED,
    fk_adventure_characters_adventures INT,
    fk_adventure_characters_characters INT,
    data_alta DATETIME,
    usuari_alta INT,
    data_mod DATETIME,
    usuari_mod INT
);

-- =========================
-- STEPS
-- =========================
CREATE TABLE steps (
    id_steps INT UNSIGNED,
    fk_steps_adventures INT,
    description TEXT,
    is_final BOOLEAN,
    data_alta DATETIME,
    usuari_alta INT,
    data_mod DATETIME,
    usuari_mod INT
);

-- =========================
-- DECISIONS
-- =========================
CREATE TABLE decisions (
    id_decisions INT UNSIGNED,
    fk_decisions_steps INT,
    description TEXT,
    result_text TEXT,
    fk_decisions_next_step INT,
    data_alta DATETIME,
    usuari_alta INT,
    data_mod DATETIME,
    usuari_mod INT
);

-- =========================
-- GAME
-- =========================
CREATE TABLE game (
    id_game INT UNSIGNED,
    fk_game_users INT,
    fk_game_characters INT,
    fk_game_adventures INT,
    game_date DATETIME,
    data_alta DATETIME,
    usuari_alta INT,
    data_mod DATETIME,
    usuari_mod INT
);

-- =========================
-- CHOICES
-- =========================
CREATE TABLE choices (
    id_choices INT UNSIGNED,
    fk_choices_game INT,
    fk_choices_steps INT,
    fk_choices_decisions INT,
    data_alta DATETIME,
    usuari_alta INT,
    data_mod DATETIME,
    usuari_mod INT
);
