-- Calculate the lifespan of bands with the main style "Glam rock" until 2022
-- Lists all bands with Glam rock as their main style - ranked by their longevity

SELECT band_name,
        (IFNULL(split, 2022) - formed)
AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
