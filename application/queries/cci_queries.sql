--Quantos idosos existem em cada família no estado da Bahia?
SELECT tf.id_familia, COUNT(tp.id_pessoa) AS idosos FROM tb_familia tf INNER JOIN tb_pessoa tp ON tp.id_familia = tf.id_familia INNER JOIN tb_mun tm ON tf.cd_ibge = tm.cd_ibge WHERE tp.idade >= 60 AND tm.uf = 'BA' GROUP BY tf.id_familia ORDER BY idosos DESC;
--Qtd de pessoas por Município e cor/raça
SELECT f.cd_ibge, m.nome_municipio, p.cod_raca_cor_pessoa, count(*) qtd 	FROM "public"."tb_pessoa" p inner join tb_familia f on f.id_familia = p.id_familia 	inner join tb_mun m on m.cd_ibge = f.cd_ibge 	group by f.cd_ibge, m.nome_municipio, p.cod_raca_cor_pessoa 	order by cd_ibge, cod_raca_cor_pessoa ;
--Qual é a média de pessoas por família em cada município?
SELECT m.nome_municipio, AVG(f.qtde_pessoas) AS media_pessoas_familia 	FROM tb_mun m 	JOIN tb_familia f ON m.cd_ibge = f.cd_ibge 	GROUP BY m.nome_municipio;
--Quantidade de famílias com casas com menos de 3 cômodos agrupados por estado, regiao e municipio:
SELECT SUM( CASE WHEN trab.cod_trabalho_12_meses_memb = 2 THEN 1 ELSE 0 END ) AS pessoas_desempregadas_12_meses, mun.nome_municipio FROM tb_trab trab INNER JOIN tb_pessoa pessoa ON trab.id_pessoa = pessoa.id_pessoa INNER JOIN tb_familia fam ON fam.id_familia = pessoa.id_familia INNER JOIN tb_mun mun ON mun.cd_ibge = fam.cd_ibge GROUP BY mun.nome_municipio ORDER BY pessoas_desempregadas_12_meses DESC LIMIT 5;
--Quantidade de pessoas por idade, sexo e função que recebem remunerção equivalente a salário mínimo ou inferior
select tp.idade, tp.cod_sexo_pessoa, tb.cod_principal_trab_memb, count(tp.id_pessoa) from tb_pessoa as tp left join tb_trab as tb on tb.id_pessoa = tp.id_pessoa where tb.val_remuner_emprego_memb <= 1320 group by tp.idade, tp.cod_sexo_pessoa, tb.cod_principal_trab_memb order by idade, tp.cod_sexo_pessoa, tb.cod_principal_trab_memb asc;
--Em que municípios moram as 5 pessoas mais velhas entrevistadas?
SELECT m.nome_municipio, max(idade) as idade_maxima from tb_pessoa p inner join tb_familia d on p.id_familia=d.id_familia inner join tb_mun m on d.cd_ibge=m.cd_ibge where p.idade is not null group by m.nome_municipio order by idade_maxima desc limit 5;
--Quantidade de famílias com casas com menos de 3 cômodos agrupados por estado, regiao e municipio:
SELECT 	mun.nome_municipio, mun.regiao, mun.uf, 	COUNT(DISTINCT(f.id_familia)) as qtd_familias FROM tb_familia f INNER JOIN tb_domicilio dom ON f.id_familia = dom.id_familia INNER JOIN tb_mun mun ON f.cd_ibge = mun.cd_ibge WHERE dom.qtd_comodos_domic_fam < 3 GROUP BY mun.uf, mun.regiao, mun.nome_municipio ORDER BY qtd_familias DESC;
--Quantas mulheres concluíram o ensino fundamental?
SELECT COUNT(DISTINCT(tb_pessoa.id_pessoa)) AS "Quantidade de Mulheres" FROM tb_pessoa INNER JOIN tb_esc ON tb_pessoa.id_pessoa = tb_esc.id_pessoa WHERE cod_curso_frequentou_pessoa_memb = 6 AND cod_concluiu_frequentou_memb = 1 AND cod_sexo_pessoa = 2;
--Quantas famílias existem em cada município, agrupadas por água canalizada ?
SELECT m.nome_municipio, CASE WHEN d.COD_AGUA_CANALIZADA_FAM = 1 THEN 'Sim' WHEN d.COD_AGUA_CANALIZADA_FAM = 2 THEN 'Não' ELSE '' END AS agua_canalizada, COUNT(DISTINCT f.id_familia) AS quantidade_de_familias FROM tb_familia f INNER JOIN tb_domicilio d ON f.id_familia = d.id_familia INNER JOIN tb_mun m ON f.cd_ibge = m.cd_ibge GROUP BY m.nome_municipio, agua_canalizada;
--Qual a media de pessoas por familia por municipio?
SELECT m.nome_municipio, AVG(f.qtde_pessoas) FROM tb_familia f LEFT JOIN tb_mun m ON m.cd_ibge = f.cd_ibge WHERE f.qtde_pessoas > 0 GROUP BY m.nome_municipio;
--Qual o curso mais elevado que as pessoas que não tiveram trabalho remunerado nos últimos 12 meses frequentaram?
SELECT tb_esc.cod_curso_frequentou_pessoa_memb AS curso_mais_elevado_pessoa_frequentou, COUNT(*) AS qtd_pessoas_sem_trabalho_remunerado_ultimos_12meses FROM tb_trab INNER JOIN tb_esc ON tb_trab.id_pessoa = tb_esc.id_pessoa WHERE tb_trab.cod_trabalho_12_meses_memb = 2 GROUP BY tb_esc.cod_curso_frequentou_pessoa_memb;
--Quais são os cinco municípios com a maior população e quantas famílias vivem em cada um?
SELECT m.nome_municipio, m.pop, COUNT(f.id_familia) as num_familias FROM tb_mun m JOIN tb_familia f ON m.cd_ibge = f.cd_ibge GROUP BY m.nome_municipio, m.pop ORDER BY m.pop DESC LIMIT 5;
--Quantas famílias com mais de 3 pessoas têm acesso a água canalizada em seus domicílios?
SELECT COUNT(*) FROM tb_familia AS f JOIN tb_domicilio AS d ON f.id_familia = d.id_familia WHERE f.qtde_pessoas > 3 AND d.cod_agua_canalizada_fam = 1;
--Quantas pessoas do sexo feminino moram em casas com água canalizada?
SELECT COUNT(*) AS qtdd_pessoas FROM tb_pessoa JOIN tb_domicilio ON tb_pessoa.id_familia = tb_domicilio.id_familia WHERE tb_pessoa.cod_sexo_pessoa = 2 AND tb_domicilio.cod_agua_canalizada_fam = 1;
--Qual a quantidade de pessoas do sexo masculino e feminino, respectivamente, em Salvador?
SELECT     cod_sexo_pessoa,     COUNT(*) FROM tb_pessoa JOIN tb_familia ON tb_pessoa.id_familia = tb_familia.id_familia WHERE tb_familia.cd_ibge = '2927408' GROUP BY cod_sexo_pessoa;