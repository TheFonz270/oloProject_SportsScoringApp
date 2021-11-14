DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS players;

CREATE TABLE players (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  army VARCHAR(255),
  wins INT,
  losses INT,
  pts_for INT,
  pts_against INT
);

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    player1_id INT REFERENCES players(id),
    player2_id INT REFERENCES players(id),
    score1 INT,
    score2 INT,
    completed BOOLEAN
);