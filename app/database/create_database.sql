-- Criando o banco de dados.
CREATE DATABASE RPG
USE RPG

-- Criando a tabela users.
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    character_id INT UNIQUE
);

-- Criando a tabela characters.
CREATE TABLE characters (
    character_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL UNIQUE,
    category VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(10) NOT NULL,
    strength INT NOT NULL,
    agility INT NOT NULL,
    health INT NOT NULL,
    stamina INT NOT NULL,
    intelligence INT NOT NULL,
    height INT NOT NULL, 
    body_shape VARCHAR(20) NOT NULL,
    skin_color VARCHAR(50),
    hair_color VARCHAR(50),
    biography TEXT,
    picture_src varchar(50),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Adicionando conexão entre as duas tabelas com o character_id referenciando o personagem de cada usuário na tabela users.
ALTER TABLE users
ADD CONSTRAINT character_id
FOREIGN KEY (character_id) REFERENCES characters(character_id);