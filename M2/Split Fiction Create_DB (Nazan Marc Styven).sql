CREATE DATABASE IF NOT EXISTS equipo7_SplitFiction;
USE equipo7_SplitFiction;

-- =========================
-- USERS
-- =========================
CREATE TABLE users (
    id_users INT UNSIGNED,
    username VARCHAR(50),
    password VARCHAR(255),
    date_reg DATETIME,
    user_reg INT,
    date_mod DATETIME,
    user_mod INT
);

-- =========================
-- CHARACTERS
-- =========================
CREATE TABLE characters (
    id_characters INT UNSIGNED,
    name VARCHAR(100),
    description TEXT,
    date_reg DATETIME,
    user_reg INT,
    date_mod DATETIME,
    user_mod INT
);

-- =========================
-- ADVENTURES
-- =========================
CREATE TABLE adventures (
    id_adventures INT UNSIGNED,
    name VARCHAR(150),
    description TEXT,
    date_reg DATETIME,
    user_reg INT,
    date_mod DATETIME,
    user_mod INT
);

-- =========================
-- ADVENTURE_CHARACTERS
-- =========================
CREATE TABLE adventure_characters (
    id_adventure_characters INT UNSIGNED,
    fk_adventure_characters_adventures INT,
    fk_adventure_characters_characters INT,
    date_reg DATETIME,
    user_reg INT,
    date_mod DATETIME,
    user_mod INT
);

-- =========================
-- STEPS
-- =========================
CREATE TABLE steps (
    id_steps INT UNSIGNED,
    fk_steps_adventures INT,
    description TEXT,
    is_final BOOLEAN,
    date_reg DATETIME,
    user_reg INT,
    date_mod DATETIME,
    user_mod INT
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
    date_reg DATETIME,
    user_reg INT,
    date_mod DATETIME,
    user_mod INT
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
    date_reg DATETIME,
    user_reg INT,
    date_mod DATETIME,
    user_mod INT
);

-- =========================
-- CHOICES
-- =========================
CREATE TABLE choices (
    id_choices INT UNSIGNED,
    fk_choices_game INT,
    fk_choices_steps INT,
    fk_choices_decisions INT,
    date_reg DATETIME,
    user_reg INT,
    date_mod DATETIME,
    user_mod INT
);
