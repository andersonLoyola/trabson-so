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
-- Name: tb_esc; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tb_esc (
    id_familia text,
    id_pessoa text,
    ind_frequenta_escola_memb integer,
    cod_concluiu_frequentou_memb integer,
    cod_curso_frequentou_pessoa_memb integer,
    cod_ano_serie_frequenta_memb integer,
    cod_ano_serie_frequentou_memb integer
);


ALTER TABLE public.tb_esc OWNER TO lucy;

--
-- PostgreSQL database dump complete
--
