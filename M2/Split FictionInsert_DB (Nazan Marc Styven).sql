USE Split_Fiction;

INSERT INTO users (username, password, data_alta, usuari_alta)
VALUES ('rafa', 'hashed_password', NOW(), 1);

INSERT INTO characters (name, description, data_alta, usuari_alta)
VALUES ('Beowulf', 'Heroic warrior', NOW(), 1);

INSERT INTO adventures (name, description, data_alta, usuari_alta)
VALUES ('La matanza de Texas', 'Horror adventure', NOW(), 1);


