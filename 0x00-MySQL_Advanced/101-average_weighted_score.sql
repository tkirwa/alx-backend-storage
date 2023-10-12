-- Define a new stored procedure named ComputeAverageWeightedScoreForUsers
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT 0;  -- Variable to check if the cursor is done
    DECLARE user_id INT;         -- Variable to store user_id for iteration
    DECLARE total_score FLOAT;   -- Variable to store total score
    DECLARE total_weight INT;    -- Variable to store total weight

    -- Declare cursor to iterate over users
    DECLARE users_cursor CURSOR FOR
        SELECT id
        FROM users;

    -- Declare continue handler for the cursor
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    -- Open the cursor
    OPEN users_cursor;

    -- Initialize variables
    SET total_score = 0;
    SET total_weight = 0;

    -- Loop through users
    user_loop: LOOP
        -- Fetch user_id from the cursor
        FETCH users_cursor INTO user_id;

        -- If cursor is done, exit the loop
        IF done = 1 THEN
            LEAVE user_loop;
        END IF;

        -- Calculate the total weighted score for the user
        SELECT SUM(corrections.score * projects.weight), SUM(projects.weight)
        INTO total_score, total_weight
        FROM corrections
        JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;

        -- If total_weight is greater than 0, update the average_score
        IF total_weight > 0 THEN
            UPDATE users
            SET average_score = total_score / total_weight
            WHERE id = user_id;
        ELSE
            -- If total_weight is 0, set average_score to 0
            UPDATE users
            SET average_score = 0
            WHERE id = user_id;
        END IF;
    END LOOP;

    -- Close the cursor
    CLOSE users_cursor;
END $$
DELIMITER ;
