-- This is a MySQL script that creates a stored procedure
-- ComputeAverageWeightedScoreForUsers that computes and
-- store the average weighted score for all students.

DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers$$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE cummulativeWeightedSum INT;
	DECLARE weightedSum INT;
	DECLARE weightedAverage FLOAT;
    DECLARE userId INT;
    DECLARE done INT DEFAULT FALSE;
    DECLARE user_cursor CURSOR FOR
    SELECT id
    FROM users;
    DECLARE
		CONTINUE HANDLER FOR NOT FOUND
    SET done = TRUE;
    OPEN user_cursor;
    user_loop:
    LOOP
		FETCH user_cursor INTO userId;
    IF done THEN LEAVE user_loop;
    END IF;
	SELECT sum(score * (SELECT weight FROM projects WHERE id = project_id))
		INTO cummulativeWeightedSum
		FROM corrections
		WHERE user_id = userId;
	SELECT sum((SELECT weight FROM projects WHERE id = project_id))
		INTO weightedSum
		FROM corrections
		WHERE user_id = userId;
	SET weightedAverage = cummulativeWeightedSum / weightedSum;
	UPDATE users 
		SET average_score = weightedAverage
		WHERE id = userId;
	END LOOP;
    CLOSE user_cursor;
END$$
DELIMITER ;