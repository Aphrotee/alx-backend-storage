-- This is a mysql script that ranks country origins of bands,
-- ordered by the number of (non-unique) f
SELECT origin, sum(fans) nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;