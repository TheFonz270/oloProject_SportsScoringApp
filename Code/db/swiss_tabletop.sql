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

-- INSERT INTO players (name, army, wins, losses, pts_for, pts_against) VALUES ('Martin', 'Tau', 0, 0, 0, 0);
-- INSERT INTO players (name, army, wins, losses, pts_for, pts_against) VALUES ('Fraz', 'Death Guard', 0, 0, 0, 0);

-- INSERT INTO games (player1_id, player2_id, score1, score2, completed) VALUES (1, 2, 70, 30, True)