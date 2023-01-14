-- This is a MySQL script that creates a stored procedure
-- ComputeAverageWeightedScoreForUser that computes and
-- store the average weighted score for a student.

DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser$$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN userID INT)
BEGIN
	DECLARE cummulativeWeightedSum INT;
	DECLARE weightedSum INT;
	DECLARE weightedAverage FLOAT;
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
END$$
DELIMITER ;