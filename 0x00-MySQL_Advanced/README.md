# 0x00. MySQL Advanced

In this project, we will work with advanced MySQL tasks involving tables, indexes, triggers, views, and stored procedures.

## Tasks

### Task 0: We are all unique!

- **File:** [0-uniq_users.sql](0x00-MySQL_Advanced/0-uniq_users.sql)
- **Description:** Write a SQL script that creates a table `users` following these requirements:
  - With attributes: `id`, `email`, and `name`
  - If the table already exists, your script should not fail
  - Make the `email` attribute unique directly in the table schema
- Usage Example:
  ```
  $ echo "SELECT * FROM users;" | mysql -uroot -p holberton
  $ cat 0-uniq_users.sql | mysql -uroot -p holberton
  $ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");' | mysql -uroot -p holberton
  $ echo 'INSERT INTO users (email, name) VALUES ("sylvie@dylan.com", "Sylvie");' | mysql -uroot -p holberton
  ```

### Task 1: In and not out

- **File:** [1-country_users.sql](0x00-MySQL_Advanced/1-country_users.sql)
- **Description:** Write a SQL script that creates a table `users` with additional attributes for country enumeration.
  - With attributes: `id`, `email`, `name`, and `country`
  - Set a default country value of `US`
  - If the table already exists, your script should not fail
- Usage Example:
  ```
  $ echo "SELECT * FROM users;" | mysql -uroot -p holberton
  $ cat 1-country_users.sql | mysql -uroot -p holberton
  $ echo 'INSERT INTO users (email, name, country) VALUES ("bob@dylan.com", "Bob", "US");' | mysql -uroot -p holberton
  $ echo 'INSERT INTO users (email, name, country) VALUES ("sylvie@dylan.com", "Sylvie", "CO");' | mysql -uroot -p holberton
  ```

### Task 2: Best band ever!

- **File:** [2-fans.sql](0x00-MySQL_Advanced/2-fans.sql)
- **Description:** Write a SQL script that ranks the country origins of bands based on the number of non-unique fans.
- Import the provided `metal_bands.sql.zip` file to use as a data source.
- Resulting table columns: `origin` and `nb_fans`

### Task 3: Old school band

- **File:** [3-glam_rock.sql](0x00-MySQL_Advanced/3-glam_rock.sql)
- **Description:** Write a SQL script that lists all bands with `Glam rock` as their main style, ranked by their longevity.
- Import the provided `metal_bands.sql.zip` file to use as a data source.
- Resulting table columns: `band_name` and `lifespan`

### Task 4: Buy buy buy

- **File:** [4-store.sql](0x00-MySQL_Advanced/4-store.sql)
- **Description:** Write a SQL script that creates a trigger to decrease the quantity of an item after adding a new order.
- The trigger should be created in the provided schema, and a sample database initialization script is provided.

### Task 5: Email validation to sent

- **File:** [5-valid_email.sql](0x00-MySQL_Advanced/5-valid_email.sql)
- **Description:** Write a SQL script that creates a trigger to reset the attribute `valid_email` only when the `email` has been changed.
- A sample database initialization script is provided.

### Task 6: Add bonus

- **File:** [6-bonus.sql](0x00-MySQL_Advanced/6-bonus.sql)
- **Description:** Write a SQL script that creates a stored procedure `AddBonus` to add a new correction for a student.
- A sample database initialization script is provided.

### Task 7: Average score

- **File:** [7-average_score.sql](0x00-MySQL_Advanced/7-average_score.sql)
- **Description:** Write a SQL script that creates a stored procedure `ComputeAverageScoreForUser` to compute and store the average score for a student.
- A sample database initialization script is provided.

### Task 8: Optimize simple search

- **File:** [8-index_my_names.sql](0x00-MySQL_Advanced/8-index_my_names.sql)
- **Description:** Write a SQL script that creates an index `idx_name_first` on the table `names` to optimize simple searches.
- Import the provided `names.sql.zip` file to use as

 a data source.

### Task 9: Optimize search and score

- **File:** [9-index_name_score.sql](0x00-MySQL_Advanced/9-index_name_score.sql)
- **Description:** Write a SQL script that creates an index `idx_name_score` on the table `names` to optimize complex search and scoring.
- Import the provided `names.sql.zip` file to use as a data source.

### Task 10: Safe divide

- **File:** [10-div.sql](0x00-MySQL_Advanced/10-div.sql)
- **Description:** Write a SQL script that creates a function `SafeDiv` to perform division and avoid division by zero.

### Task 11: No table for a meeting

- **File:** [11-students_count.sql](0x00-MySQL_Advanced/11-students_count.sql)
- **Description:** Write a SQL script that creates a stored procedure `HowManyStudents` to return the number of students with a specific meeting date.

## Author

* [Tonny Kirwa](https://github.com/tkirwa)

This project is part of the Holberton School curriculum.
