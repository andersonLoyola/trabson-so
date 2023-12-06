-- Quais são as três famílias com a maior renda média em cada município?
SELECT cd_ibge, id_familia, vlr_renda_media_fam  FROM (SELECT cd_ibge, id_familia, vlr_renda_media_fam, ROW_NUMBER() OVER (PARTITION BY cd_ibge ORDER BY vlr_renda_media_fam DESC) as rn      FROM tb_familia ) tmp  WHERE rn <= 3;
