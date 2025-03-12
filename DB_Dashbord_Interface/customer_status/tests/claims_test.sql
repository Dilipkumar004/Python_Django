WITH user_ids AS (
    SELECT id
    FROM claims -- Replace with your actual model
)

SELECT
    id,
    COUNT(*) AS count
FROM user_ids
GROUP BY id
HAVING COUNT(*) > 1