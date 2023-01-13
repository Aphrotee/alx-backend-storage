-- This is a MySQL scripit that  creates a stored procedure
-- AddBonus that adds a new correction for a student
DELIMITER $$
DROP PROCEDURE IF EXISTS AddBonus$$
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
DECLARE project_id INT;
SET project_id = 0;
IF EXISTS(SELECT * FROM projects WHERE name = project_name)
THEN
SELECT id INTO project_id FROM projects WHERE name = project_name;
ELSE
INSERT INTO projects(name) VALUES (project_name);
SET project_id = LAST_INSERT_ID();
END IF;
INSERT INTO corrections(user_id, project_id, score)
VALUES (user_id, project_id, score);
END;$$
DELIMITER ;