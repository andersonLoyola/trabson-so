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
-- Name: tb_trab; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tb_trab (
    id_familia text,
    id_pessoa text,
    cod_principal_trab_memb integer,
    val_remuner_emprego_memb integer,
    cod_trabalho_12_meses_memb integer,
    qtd_meses_12_meses_memb integer,
    val_renda_bruta_12_meses_memb integer,
    val_renda_doacao_memb integer,
    val_renda_aposent_memb integer,
    val_renda_seguro_desemp_memb integer,
    val_renda_pensao_alimen_memb integer,
    val_outras_rendas_memb integer
);


ALTER TABLE public.tb_trab OWNER TO lucy;

--
-- PostgreSQL database dump complete
--
