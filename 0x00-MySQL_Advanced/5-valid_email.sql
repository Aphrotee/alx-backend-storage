-- This is  a MySQL script that creates a trigger that resets the
-- attribute valid_email only when the email has been changed

DELIMITER $$
DROP TRIGGER IF EXISTS reset_email_validation$$
CREATE
TRIGGER reset_email_validation
BEFORE UPDATE ON users
FOR EACH ROW
IF NEW.email != OLD.email
THEN SET NEW.valid_email = 0;
END IF;
$$