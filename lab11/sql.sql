-- Таблица
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    phone VARCHAR(20) NOT NULL
);

-- Функция поиска по шаблону
CREATE OR REPLACE FUNCTION search_by_pattern(pattern TEXT)
RETURNS TABLE(id INT, first_name VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook
    WHERE first_name ILIKE '%' || pattern || '%'
       OR phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- Процедура вставки/обновления одного пользователя
CREATE OR REPLACE PROCEDURE insert_or_update_user(name TEXT, phone TEXT)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = name) THEN
        UPDATE phonebook SET phone = phone WHERE first_name = name;
    ELSE
        INSERT INTO phonebook (first_name, phone) VALUES (name, phone);
    END IF;
END;
$$ LANGUAGE plpgsql;

-- Процедура массовой вставки с проверкой номера
CREATE OR REPLACE PROCEDURE insert_many_users(
    IN names TEXT[],
    IN phones TEXT[],
    OUT incorrect_data TEXT[]
)
AS $$
DECLARE
    i INT := 1;
    phone_pattern TEXT := '^\d{10,15}$';
BEGIN
    incorrect_data := ARRAY[]::TEXT[];

    WHILE i <= array_length(names, 1) LOOP
        IF phones[i] ~ phone_pattern THEN
            IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = names[i]) THEN
                UPDATE phonebook SET phone = phones[i] WHERE first_name = names[i];
            ELSE
                INSERT INTO phonebook (first_name, phone) VALUES (names[i], phones[i]);
            END IF;
        ELSE
            incorrect_data := array_append(incorrect_data, names[i] || ' - ' || phones[i]);
        END IF;
        i := i + 1;
    END LOOP;
END;
$$ LANGUAGE plpgsql;
