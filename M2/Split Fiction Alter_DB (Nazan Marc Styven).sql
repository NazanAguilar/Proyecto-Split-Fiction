USE Split_Fiction;

-- =========================
-- USERS
-- =========================
ALTER TABLE users
    MODIFY id_users INT UNSIGNED AUTO_INCREMENT,
    ADD CONSTRAINT pk_users PRIMARY KEY (id_users),
    MODIFY username VARCHAR(50) NOT NULL,
    MODIFY password VARCHAR(255) NOT NULL,
    MODIFY data_alta DATETIME NOT NULL,
    MODIFY usuari_alta INT NOT NULL,
    MODIFY data_mod DATETIME NULL,
    MODIFY usuari_mod INT NULL,
    ADD CONSTRAINT uq_users_username UNIQUE (username);

-- =========================
-- CHARACTERS
-- =========================
ALTER TABLE characters
    MODIFY id_characters INT UNSIGNED AUTO_INCREMENT,
    ADD CONSTRAINT pk_characters PRIMARY KEY (id_characters),
    MODIFY name VARCHAR(100) NOT NULL,
    MODIFY description TEXT NOT NULL,
    MODIFY data_alta DATETIME NOT NULL,
    MODIFY usuari_alta INT NOT NULL,
    MODIFY data_mod DATETIME NULL,
    MODIFY usuari_mod INT NULL,
    ADD CONSTRAINT uq_characters_name UNIQUE (name);

-- =========================
-- ADVENTURES
-- =========================
ALTER TABLE adventures
    MODIFY id_adventures INT UNSIGNED AUTO_INCREMENT,
    ADD CONSTRAINT pk_adventures PRIMARY KEY (id_adventures),
    MODIFY name VARCHAR(150) NOT NULL,
    MODIFY description TEXT NOT NULL,
    MODIFY data_alta DATETIME NOT NULL,
    MODIFY usuari_alta INT NOT NULL,
    MODIFY data_mod DATETIME NULL,
    MODIFY usuari_mod INT NULL,
    ADD CONSTRAINT uq_adventures_name UNIQUE (name);

-- =========================
-- ADVENTURE_CHARACTERS
-- =========================
ALTER TABLE adventure_characters
    MODIFY id_adventure_characters INT UNSIGNED AUTO_INCREMENT,
    ADD CONSTRAINT pk_adventure_characters PRIMARY KEY (id_adventure_characters),
    MODIFY fk_adventure_characters_adventures INT UNSIGNED NOT NULL,
    MODIFY fk_adventure_characters_characters INT UNSIGNED NOT NULL,
    MODIFY data_alta DATETIME NOT NULL,
    MODIFY usuari_alta INT NOT NULL,
    MODIFY data_mod DATETIME NULL,
    MODIFY usuari_mod INT NULL,
    ADD CONSTRAINT fk_ac_adventures
        FOREIGN KEY (fk_adventure_characters_adventures)
        REFERENCES adventures(id_adventures),
    ADD CONSTRAINT fk_ac_characters
        FOREIGN KEY (fk_adventure_characters_characters)
        REFERENCES characters(id_characters);

-- =========================
-- STEPS
-- =========================
ALTER TABLE steps
    MODIFY id_steps INT UNSIGNED AUTO_INCREMENT,
    ADD CONSTRAINT pk_steps PRIMARY KEY (id_steps),
    MODIFY fk_steps_adventures INT UNSIGNED NOT NULL,
    MODIFY description TEXT NOT NULL,
    MODIFY is_final BOOLEAN NOT NULL DEFAULT FALSE,
    MODIFY data_alta DATETIME NOT NULL,
    MODIFY usuari_alta INT NOT NULL,
    MODIFY data_mod DATETIME NULL,
    MODIFY usuari_mod INT NULL,
    ADD CONSTRAINT fk_steps_adventures
        FOREIGN KEY (fk_steps_adventures)
        REFERENCES adventures(id_adventures);

-- =========================
-- DECISIONS
-- =========================
ALTER TABLE decisions
    MODIFY id_decisions INT UNSIGNED AUTO_INCREMENT,
    ADD CONSTRAINT pk_decisions PRIMARY KEY (id_decisions),
    MODIFY fk_decisions_steps INT UNSIGNED NOT NULL,
    MODIFY fk_decisions_next_step INT UNSIGNED NOT NULL,
    MODIFY description TEXT NOT NULL,
    MODIFY result_text TEXT NOT NULL,
    MODIFY data_alta DATETIME NOT NULL,
    MODIFY usuari_alta INT NOT NULL,
    MODIFY data_mod DATETIME NULL,
    MODIFY usuari_mod INT NULL,
    ADD CONSTRAINT fk_decisions_steps
        FOREIGN KEY (fk_decisions_steps)
        REFERENCES steps(id_steps),
    ADD CONSTRAINT fk_decisions_next_step
        FOREIGN KEY (fk_decisions_next_step)
        REFERENCES steps(id_steps);

-- =========================
-- GAME
-- =========================
ALTER TABLE game
    MODIFY id_game INT UNSIGNED AUTO_INCREMENT,
    ADD CONSTRAINT pk_game PRIMARY KEY (id_game),
    MODIFY fk_game_users INT UNSIGNED NOT NULL,
    MODIFY fk_game_characters INT UNSIGNED NOT NULL,
    MODIFY fk_game_adventures INT UNSIGNED NOT NULL,
    MODIFY game_date DATETIME NOT NULL,
    MODIFY data_alta DATETIME NOT NULL,
    MODIFY usuari_alta INT NOT NULL,
    MODIFY data_mod DATETIME NULL,
    MODIFY usuari_mod INT NULL,
    ADD CONSTRAINT fk_game_users
        FOREIGN KEY (fk_game_users)
        REFERENCES users(id_users),
    ADD CONSTRAINT fk_game_characters
        FOREIGN KEY (fk_game_characters)
        REFERENCES characters(id_characters),
    ADD CONSTRAINT fk_game_adventures
        FOREIGN KEY (fk_game_adventures)
        REFERENCES adventures(id_adventures);

-- =========================
-- CHOICES
-- =========================
ALTER TABLE choices
    MODIFY id_choices INT UNSIGNED AUTO_INCREMENT,
    ADD CONSTRAINT pk_choices PRIMARY KEY (id_choices),
    MODIFY fk_choices_game INT UNSIGNED NOT NULL,
    MODIFY fk_choices_steps INT UNSIGNED NOT NULL,
    MODIFY fk_choices_decisions INT UNSIGNED NOT NULL,
    MODIFY data_alta DATETIME NOT NULL,
    MODIFY usuari_alta INT NOT NULL,
    MODIFY data_mod DATETIME NULL,
    MODIFY usuari_mod INT NULL,
    ADD CONSTRAINT fk_choices_game
        FOREIGN KEY (fk_choices_game)
        REFERENCES game(id_game),
    ADD CONSTRAINT fk_choices_steps
        FOREIGN KEY (fk_choices_steps)
        REFERENCES steps(id_steps),
    ADD CONSTRAINT fk_choices_decisions
        FOREIGN KEY (fk_choices_decisions)
        REFERENCES decisions(id_decisions);
