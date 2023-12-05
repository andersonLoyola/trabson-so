--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3 (Debian 15.3-0+deb12u1)
-- Dumped by pg_dump version 15.3 (Debian 15.3-0+deb12u1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: tb_domicilio; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tb_domicilio (
    id_familia text,
    cod_local_domic_fam integer,
    cod_especie_domic_fam integer,
    qtd_comodos_domic_fam integer,
    qtd_comodos_dormitorio_fam integer,
    cod_material_piso_fam integer,
    cod_material_domic_fam integer,
    cod_agua_canalizada_fam integer,
    cod_abaste_agua_domic_fam integer,
    cod_banheiro_domic_fam integer,
    cod_escoa_sanitario_domic_fam integer,
    cod_destino_lixo_domic_fam integer,
    cod_iluminacao_domic_fam integer,
    cod_calcamento_domic_fam integer
);


ALTER TABLE public.tb_domicilio OWNER TO lucy;

--
-- PostgreSQL database dump complete
--
