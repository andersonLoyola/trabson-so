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
-- Name: tb_familia; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tb_familia (
    cd_ibge text,
    id_familia text,
    dat_alteracao_fam date,
    vlr_renda_media_fam text,
    qtde_pessoas integer
);


ALTER TABLE public.tb_familia OWNER TO lucy;

--
-- PostgreSQL database dump complete
--
