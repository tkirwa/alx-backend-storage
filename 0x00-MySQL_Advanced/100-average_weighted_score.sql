-- Define a new stored procedure named ComputeAverageWeightedScoreForUser
DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    -- Update the average_score for a specific user
    UPDATE users
    SET average_score = (
        SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight)
        -- Calculate the weighted average score by joining corrections and projects tables
        FROM corrections
        INNER JOIN projects ON projects.id = corrections.project_id
        WHERE corrections.user_id = user_id
    )
    -- Update the user's average score where the user_id matches
    WHERE users.id = user_id;
END $$
DELIMITER ;
