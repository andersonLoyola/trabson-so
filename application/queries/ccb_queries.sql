-- QUERY QUE RETORNE O CÓDIGO IBGE E ID DA FAMILIA APENAS PARA FAMILIAR COM DATA DE ALTERAÇÃO DO ANO DE 2017 DE FORMA ORDENADA.
SELECT 	CD_IBGE, 	ID_FAMILIA, 	DAT_ALTERACAO_FAM 	FROM TB_FAMILIA 	WHERE DAT_ALTERACAO_FAM >= '2017-01-01' AND DAT_ALTERACAO_FAM <= '2017-12-31' ORDER BY DAT_ALTERACAO_FAM;
-- Quantidade de domicilios sem banheiro
SELECT 	COUNT(DISTINCT(dom.id_familia)) FROM tb_domicilio dom WHERE dom.cod_banheiro_domic_fam = 2;
-- Quantidade de familias que nao possuem domicilio particular regular
SELECT 	COUNT(DISTINCT(dom.id_familia)) FROM tb_domicilio dom WHERE dom.cod_local_domic_fam = 1 AND dom.cod_especie_domic_fam IN (2 ,3);
-- Quais dados do domicílio das famílias que possuem apenas um cômodo?
select * from tb_domicilio where qtd_comodos_domic_fam = 1;
-- FAMILIAs QUE TENHA MAIS DE 2 INTEGRANTES
SELECT * FROM TB_FAMILIA WHERE QTDE_PESSOAS > 2;
-- Quais municipios possuem uma população com número inferior à 1000 pessoas?
select * from tb_mun where pop < 1000;
-- Média de Idade das Pessoas nas Famílias da base de dados?
SELECT AVG(idade) AS media_idade FROM tb_pessoa;
-- Qual a Idade média da população entrevistada?
SELECT avg(idade) from tb_pessoa;
-- Qual a Quantidade média de cômodos dos domicílios?
SELECT avg(qtd_comodos_domic_fam) FROM "public"."tb_domicilio";
-- Qual a média de cômodos por domicilio
SELECT AVG(qtd_comodos_domic_fam) FROM tb_domicilio;
--Quantidade de pessoas por sexo na base de dados?
SELECT CASE WHEN cod_sexo_pessoa = 1 THEN 'Masculino' WHEN cod_sexo_pessoa = 2 THEN 'Feminino' ELSE '' END AS sexo, COUNT(DISTINCT id_pessoa) AS quantidade_de_pessoas FROM tb_pessoa GROUP BY cod_sexo_pessoa;
-- Valor total da média familiar e total de pessoas por municipio
SELECT cd_ibge, SUM (to_number(vlr_renda_media_fam, '99999999999')) AS "totalMediaFam", SUM (qtde_pessoas) AS "totalPessoas" FROM tb_familia GROUP BY cd_ibge order by 3 DESC;
-- Quantidade de pessoas agrupadas por nível de escolaridade
select cod_curso_frequentou_pessoa_memb, cod_concluiu_frequentou_memb, count(id_pessoa) as qtde_pessoas from tb_esc group by cod_curso_frequentou_pessoa_memb, cod_concluiu_frequentou_memb order by cod_curso_frequentou_pessoa_memb, cod_concluiu_frequentou_memb asc;
-- Pergunta 5: Quais são os tipos de materiais de piso mais comuns nas famílias?
SELECT cod_material_piso_fam, COUNT(*) FROM tb_domicilio GROUP BY cod_material_piso_fam ORDER BY COUNT(*) DESC LIMIT 1;
-- Agrupe a quantidade de pessoas pelas diferentes cores de pele.
SELECT cod_raca_cor_pessoa , COUNT(*) FROM tb_pessoa GROUP BY cod_raca_cor_pessoa;