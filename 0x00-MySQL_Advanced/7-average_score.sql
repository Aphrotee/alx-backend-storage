-- This is a MySQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student

DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser$$
CREATE PROCEDURE ComputeAverageScoreForUser(IN userId INT)
BEGIN
DECLARE average FLOAT;
SELECT avg(score)
into average
FROM corrections
WHERE user_id = userId;
UPDATE users
SET average_score = average
WHERE id = userID;
END;
$$

DELIMITER ;