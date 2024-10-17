-- Creates the stored procedure AddBonus
-- DELIMITER $$
-- CREATE PROCEDURE AddBonus(
--   IN user_id INT,
--   IN project_name VARCHAR(255),
--   IN score INT
-- )
-- BEGIN
--   DECLARE project_id INT;
--   SELECT id INTO project_id FROM projects WHERE name = project_name LIMIT 1;
--   IF project_id IS NULL THEN
--     INSERT INTO projects (name) VALUES (project_name);
--     SET project_id = LAST_INSERT_ID();
--   END IF;
--   INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score)
-- END $$
-- DELIMITER ;
-- Create the stored procedure AddBonus
DELIMITER //

CREATE PROCEDURE AddBonus(
  IN user_id INT,
  IN project_name VARCHAR(255),
  IN score INT
)
BEGIN
  DECLARE project_id INT;

  -- Try to find the project_id based on the project_name
  SELECT id INTO project_id FROM projects WHERE name = project_name LIMIT 1;

  -- If project_id is NULL, the project doesn't exist; create it
  IF project_id IS NULL THEN
    INSERT INTO projects (name) VALUES (project_name);
    SET project_id = LAST_INSERT_ID();
  END IF;

  -- Insert the new correction into the corrections table
  INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END;
//

DELIMITER ;
