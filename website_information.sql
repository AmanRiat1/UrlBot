-- Adminer 4.7.3 PostgreSQL dump

DROP TABLE IF EXISTS "website_information";
DROP SEQUENCE IF EXISTS website_information_id_seq;
CREATE SEQUENCE website_information_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1;

CREATE TABLE "public"."website_information" (
    "id" integer DEFAULT nextval('website_information_id_seq') NOT NULL,
    "name" text NOT NULL,
    "url" text NOT NULL
) WITH (oids = false);


-- 2019-09-10 02:18:52.991019+00
