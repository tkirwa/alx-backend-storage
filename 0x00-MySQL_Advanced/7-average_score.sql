-- Create a stored procedure to compute and store the average score for a user
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
    DECLARE total_score INT;
    DECLARE number_of_corrections INT;
    DECLARE average FLOAT;

    -- Calculate the total score and number of corrections for the user
    SELECT SUM(score), COUNT(*) INTO total_score, number_of_corrections
    FROM corrections
    WHERE user_id = user_id;

    -- Calculate the average score (use COALESCE to handle division by zero)
    SET average = COALESCE(total_score / number_of_corrections, 0);

    -- Update the user's average score
    UPDATE users
    SET average_score = average
    WHERE id = user_id;
END;
//
DELIMITER ;
