DROP TABLE IF EXISTS product_score,
"user",
affinity,
region,
comuna,
user_score,
historical,
"match",
provincia,
admin,
product,
indictment,
category,
address,
product_category;

CREATE TABLE
    "product_score" (
        "score_id" INTEGER NOT NULL,
        "user_reviewer" VARCHAR(255) NOT NULL,
        "product_reviewed" VARCHAR(255) NOT NULL,
        "score_date" DATE NOT NULL,
        "score_value" INTEGER NOT NULL
    );

ALTER TABLE "product_score" ADD PRIMARY KEY ("score_id");

CREATE TABLE
    "user" (
        "user_id" VARCHAR(255) NOT NULL,
        "user_name1" VARCHAR(255) NOT NULL,
        "user_name2" VARCHAR(255) NULL,
        "user_surname1" VARCHAR(255) NOT NULL,
        "user_surname2" VARCHAR(255) NULL,
        "user_email" VARCHAR(255) NOT NULL,
        "user_password" VARCHAR(255) NOT NULL,
        "user_last_loc_lat" DOUBLE PRECISION NULL,
        "user_last_loc_long" DOUBLE PRECISION NULL,
        "user_date_lastloc" DATE NULL,
        "date_registred" DATE NOT NULL,
        "date_last_login" DATE NOT NULL,
        "user_score" INTEGER NOT NULL,
        "user_phone" INTEGER NOT NULL,
        "user_active" BOOLEAN NOT NULL,
        "user_inetrest1" INTEGER NOT NULL,
        "user_interest2" INTEGER NOT NULL,
        "user_photo" VARCHAR(255) NOT NULL,
        "user_sells" INTEGER NOT NULL,
        "user_is_premium" BOOLEAN NOT NULL,
        "user_premium_start" DATE NULL,
        "user_premium_ends" DATE NULL
    );

ALTER TABLE "user" ADD PRIMARY KEY ("user_id");

CREATE TABLE
    "affinity" (
        "af_id" INTEGER NOT NULL,
        "af_name" VARCHAR(255) NOT NULL
    );

ALTER TABLE "affinity" ADD PRIMARY KEY ("af_id");

CREATE TABLE
    "region" (
        "region_id" INTEGER NOT NULL,
        "region_name" VARCHAR(255) NOT NULL
    );

ALTER TABLE "region" ADD PRIMARY KEY ("region_id");

CREATE TABLE
    "comuna" (
        "comuna_id" INTEGER NOT NULL,
        "provincia_id" INTEGER NOT NULL,
        "comuna_name" VARCHAR(255) NOT NULL
    );

ALTER TABLE "comuna" ADD PRIMARY KEY ("comuna_id");

CREATE TABLE
    "user_score" (
        "score_id" INTEGER NOT NULL,
        "user_reviwer" VARCHAR(255) NULL,
        "user_reviwed" VARCHAR(255) NOT NULL,
        "score_date" DATE NOT NULL,
        "score_value" INTEGER NOT NULL
    );

ALTER TABLE "user_score" ADD PRIMARY KEY ("score_id");

CREATE TABLE
    "historical" (
        "hist_id" INTEGER NOT NULL,
        "date" DATE NOT NULL,
        "buyer_id" VARCHAR(255) NOT NULL,
        "prod_id" VARCHAR(255) NOT NULL
    );

ALTER TABLE "historical" ADD PRIMARY KEY ("hist_id");

CREATE TABLE
    "match" (
        "user_id" VARCHAR(255) NOT NULL,
        "match_date" DATE NOT NULL,
        "user_liked" VARCHAR(255) NOT NULL
    );

ALTER TABLE "match" ADD PRIMARY KEY ("user_id");

CREATE TABLE
    "provincia" (
        "provincia_id" INTEGER NOT NULL,
        "region_id" INTEGER NOT NULL,
        "provincia_name" VARCHAR(255) NOT NULL
    );

ALTER TABLE "provincia" ADD PRIMARY KEY ("provincia_id");

CREATE TABLE
    "admin" (
        "admin_id" VARCHAR(255) NOT NULL,
        "admin_name1" VARCHAR(255) NOT NULL,
        "admin_name2" VARCHAR(255) NULL,
        "admin_surname1" VARCHAR(255) NOT NULL,
        "admin_surname2" VARCHAR(255) NULL,
        "admin_email" VARCHAR(255) NOT NULL,
        "admin_date_hire" DATE NOT NULL,
        "admin_status" BOOLEAN NOT NULL,
        "is_super_admin" BOOLEAN NOT NULL
    );

ALTER TABLE "admin" ADD PRIMARY KEY ("admin_id");

CREATE TABLE
    "product" (
        "prod_id" VARCHAR(255) NOT NULL,
        "prod_name" VARCHAR(255) NOT NULL,
        "prod_new" BOOLEAN NOT NULL,
        "permuta" BOOLEAN NOT NULL,
        "prod_price" INTEGER NOT NULL,
        "prod_date" DATE NOT NULL,
        "prod_score" INTEGER NULL,
        "prod_seller" VARCHAR(255) NOT NULL,
        "prod_reported" BOOLEAN NULL,
        "prod_active" BOOLEAN NOT NULL,
        "prod_description" VARCHAR(255) NOT NULL,
        "prod_affinitie1" INTEGER NOT NULL,
        "prod_affinitie2" INTEGER NULL,
        "prod_photo1" VARCHAR(255) NOT NULL,
        "prod_photo2" VARCHAR(255) NOT NULL,
        "prod_photo3" VARCHAR(255) NULL,
        "prod_photo4" VARCHAR(255) NULL,
        "prod_photo5" VARCHAR(255) NULL,
        "id_prod_indct" INTEGER NULL
    );

ALTER TABLE "product" ADD PRIMARY KEY ("prod_id");

CREATE TABLE
    "indictment" (
        "id_prod_indct" INTEGER NOT NULL,
        "report_date" DATE NOT NULL,
        "user_reported" VARCHAR(255) NOT NULL,
        "user_accuser" VARCHAR(255) NOT NULL,
        "report_description" VARCHAR(255) NOT NULL,
        "report_action" VARCHAR(255) NOT NULL
    );

ALTER TABLE "indictment" ADD PRIMARY KEY ("id_prod_indct");

CREATE TABLE
    "category" (
        "cat_id" VARCHAR(255) NOT NULL,
        "cat_name" VARCHAR(255) NOT NULL
    );

ALTER TABLE "category" ADD PRIMARY KEY ("cat_id");

CREATE TABLE
    "address" (
        "comuna_id" INTEGER NOT NULL,
        "cod_postal" VARCHAR(255) NULL,
        "casa_o_dep" INTEGER NOT NULL,
        "calle" VARCHAR(255) NOT NULL,
        "user_id" VARCHAR(255) NOT NULL,
        "numero" VARCHAR(255) NOT NULL,
        "comentario" VARCHAR(255) NULL
    );

ALTER TABLE "address" ADD PRIMARY KEY ("user_id");

CREATE TABLE
    "product_category" (
        "product" VARCHAR(255) NOT NULL,
        "category" VARCHAR(255) NOT NULL
    );

ALTER TABLE "product_score" ADD CONSTRAINT "product_score_product_reviewed_foreign" FOREIGN KEY ("product_reviewed") REFERENCES "product" ("prod_id");

ALTER TABLE "historical" ADD CONSTRAINT "historical_prod_id_foreign" FOREIGN KEY ("prod_id") REFERENCES "product" ("prod_id");

ALTER TABLE "address" ADD CONSTRAINT "address_user_id_foreign" FOREIGN KEY ("user_id") REFERENCES "user" ("user_id");

ALTER TABLE "product" ADD CONSTRAINT "product_prod_id_foreign" FOREIGN KEY ("id_prod_indct") REFERENCES "indictment" ("id_prod_indct");

ALTER TABLE "comuna" ADD CONSTRAINT "comuna_provincia_id_foreign" FOREIGN KEY ("provincia_id") REFERENCES "provincia" ("provincia_id");

ALTER TABLE "provincia" ADD CONSTRAINT "provincia_region_id_foreign" FOREIGN KEY ("region_id") REFERENCES "region" ("region_id");

ALTER TABLE "product_category" ADD CONSTRAINT "product_category_product_foreign" FOREIGN KEY ("product") REFERENCES "product" ("prod_id");

ALTER TABLE "product_category" ADD CONSTRAINT "product_cat_category_foreign" FOREIGN KEY ("category") REFERENCES "category" ("cat_id");

ALTER TABLE "address" ADD CONSTRAINT "address_comuna_id_foreign" FOREIGN KEY ("comuna_id") REFERENCES "comuna" ("comuna_id");

ALTER TABLE "user_score" ADD CONSTRAINT "user_score_user_reviwer_foreign" FOREIGN KEY ("user_reviwer") REFERENCES "user" ("user_id");

ALTER TABLE "match" ADD CONSTRAINT "match_user_id_foreign" FOREIGN KEY ("user_id") REFERENCES "user" ("user_id");

ALTER TABLE "product" ADD CONSTRAINT "product_prod_seller_foreign" FOREIGN KEY ("prod_seller") REFERENCES "user" ("user_id");

-- Eliminamos 
DROP TABLE IF EXISTS django_session;

-- Creamos esta tabla para que deje iniciar a usuarios
CREATE TABLE
    django_session (
        session_key varchar(40) NOT NULL PRIMARY KEY,
        session_data text NOT NULL,
        expire_date timestamp
        with
            time zone NOT NULL
    );