-- Calculate the lifespan of bands with the main style "Glam rock" until 2022
-- Lists all bands with Glam rock as their main style - ranked by their longevity

SELECT band_name, 
       IFNULL(NULLIF(IF(split = 0, 2022 - formed, split - formed), -formed), 0) as lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
