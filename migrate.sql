CREATE TABLE "appfd_place" (
"id" serial NOT NULL PRIMARY KEY,
"created" timestamp with time zone NULL,
"modified" timestamp with time zone NULL,
"attribution" text NULL,
"enwiki_title" text NULL,
"geonames_id" integer NULL,
"osm_id" text NULL,
"pcode" text NULL,
"fips" integer NULL,
"admin1_code" text NULL,
"admin2_code" text NULL,
"admin3_code" text NULL,
"admin4_code" text NULL,
"admin_level" integer NULL,
"east" double precision NULL,
"north" double precision NULL,
"south" double precision NULL,
"west" double precision NULL,
"name" text NULL,
"name_ascii" text NULL,
"name_display" text NULL,
"name_en" text NULL,
"name_normalized" text NULL,
"other_names" text NULL,
"geonames_feature_class" text NULL,
"geonames_feature_code" text NULL,
"place_type" text NULL,
"latitude" double precision NULL,
"longitude" double precision NULL,
"mls" geometry(MULTILINESTRING,4326) NULL,
"mpoly" geometry(MULTIPOLYGON,4326) NULL,
"point" geometry(POINT,4326) NULL,
"area_sqkm" integer NULL,
"importance" double precision NULL,
"osmname_class" text NULL,
"osmname_type" text NULL,
"osm_type" text NULL,
"place_rank" integer NULL,
"dem" double precision NULL,
"elevation" double precision NULL,
"city" text NULL,
"county" text NULL,
"country" text NULL,
"country_code" text NULL,
"state" text NULL,
"street" text NULL,
"note" text NULL,
"population" bigint NULL,
"popularity" bigint NULL,
"timezone" text NULL,
"wikidata_id" text NULL,  
"topic_id" integer NULL
);
