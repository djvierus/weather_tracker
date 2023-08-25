--
-- PostgreSQL database dump
--

-- Dumped from database version 14.9 (Ubuntu 14.9-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 15.3


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

--
-- TOC entry 3317 (class 1262 OID 16441)
-- Name: weather; Type: DATABASE; Schema: -; Owner: -
--

CREATE DATABASE weather WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.UTF-8';


\connect weather

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

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: -
--

-- *not* creating schema, since initdb creates it


--
-- TOC entry 210 (class 1259 OID 16447)
-- Name: weather_hist_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.weather_hist_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


SET default_table_access_method = heap;

--
-- TOC entry 209 (class 1259 OID 16442)
-- Name: weather_history; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.weather_history (
    id bigint NOT NULL,
    "timestamp" timestamp without time zone NOT NULL,
    temperature bigint NOT NULL,
    source character varying(75) NOT NULL,
    city character varying(75),
    state character varying(75)
);


--
-- TOC entry 3172 (class 2606 OID 16446)
-- Name: weather_history weather_history_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.weather_history
    ADD CONSTRAINT weather_history_pkey PRIMARY KEY (id);


