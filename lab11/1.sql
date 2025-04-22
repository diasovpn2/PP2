CREATE TABLE phonebook (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    number BIGINT
);
CREATE OR REPLACE FUNCTION insert_or_update_user(new_name TEXT, new_number BIGINT)
RETURNS VOID AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = new_name) THEN
        UPDATE phonebook SET number = new_number WHERE name = new_name;
    ELSE
        INSERT INTO phonebook (name, number) VALUES (new_name, new_number);
    END IF;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION search_by_pattern(pattern TEXT)
RETURNS SETOF phonebook AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook
    WHERE name ILIKE '%' || pattern || '%'
    OR number::TEXT LIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE delete_user(p_name TEXT DEFAULT NULL, p_number BIGINT DEFAULT NULL)
LANGUAGE plpgsql AS $$
BEGIN
    IF p_name IS NOT NULL AND p_number IS NOT NULL THEN
        DELETE FROM phonebook WHERE name = p_name OR number = p_number;
    ELSIF p_name IS NOT NULL THEN
        DELETE FROM phonebook WHERE name = p_name;
    ELSIF p_number IS NOT NULL THEN
        DELETE FROM phonebook WHERE number = p_number;
    END IF;
END;
$$;
