# Test Lexicom


## How to Use

## 1. Task

1. Copy .env.example to .env. Then paste your own data into .env:
```shell
cp .env.example .env
```
2. Execute the command to start Docker:
```shell
docker-compose up --build -d
```
3. Open a web browser and navigate to the API documentation page:
- http://localhost:5000/docs

## 2. Task

1. Run an SQL query to create a short_names table and generate data:
```sql
-- Creating the table short_names
CREATE TABLE short_names (
    name VARCHAR(255) PRIMARY KEY,
    status INT
);

-- Generating 700,000 records
DO $$
BEGIN
    FOR i IN 1..700000 LOOP
        INSERT INTO short_names (name, status) VALUES ('nazvanie' || i, (i % 2)::INT);
    END LOOP;
END $$;
```

2. Perform the SQL query to create the table full_names and generate data:
```sql
-- Creating the table full_names
CREATE TABLE full_names (
    name VARCHAR(255) PRIMARY KEY,
    status INT
);

-- Generating 500 000 records with random extensions
DO $$
DECLARE
    extensions VARCHAR[] := ARRAY['mp3', 'wav', 'flac', 'aac', 
                                  'ogg', 'wma', 'mp4', 'avi', 
                                  'mkv', 'mov', 'wmv', 'flv', 
                                  'jpg', 'jpeg', 'png', 'gif', 
                                  'bmp', 'pdf', 'docx', 'xlsx', 
                                  'txt', 'csv', 'zip', 'rar', 
                                  '7z', 'tar', 'gz'];
    random_index INT;
    extension VARCHAR(10);
BEGIN
    FOR i IN 1..500000 LOOP
        -- We select a random extension from an array of popular extensions
        random_index := floor(random() * array_length(extensions, 1)) + 1;
        extension := extensions[random_index];

        INSERT INTO full_names (name, status) VALUES ('nazvanie' || i || '.' || extension, NULL);
    END LOOP;
END $$;
```

3. 
- 1 solution Using a subquery:
```sql
UPDATE full_names
SET status = (
    SELECT status 
    FROM short_names 
    WHERE short_names.name = substring(full_names.name from 1 for position('.' in full_names.name) - 1);
```
Updates the status column in the full_names table. The status values are retrieved from the short_names table based on the corresponding file name without extension.


- 2 solution Using JOIN:
```sql
UPDATE full_names
SET status = short_names.status
FROM short_names
WHERE short_names.name = substring(full_names.name from 1 for position('.' in full_names.name) - 1)
);
```
Updates the status column in the full_names table.
It assigns the status values from the short_names table based on the file names without extensions,
matching them with the names in the full_names table.

- 3 solution Using a temp table:
```sql
CREATE TEMP TABLE temp_names AS
SELECT 
    s.status AS short_status, 
    f.name AS full_name
FROM short_names s
JOIN full_names f ON substring(f.name from 1 for position('.' in f.name) - 1) = s.name;

UPDATE full_names 
SET status = t.short_status
FROM temp_names t
WHERE full_names.name = t.full_name;

DROP TABLE temp_names;
```
This code creates a temporary table temp_names,
combining status values from short_names with file names from full_names, excluding extensions.
It then updates the status column in full_names based on the matched file names from the temporary table.
Finally, it drops the temporary table