BEGIN;
--
-- Create model Anuncio
--
CREATE TABLE "anuncios_anuncio" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "titulo" varchar(150) NOT NULL, 
    "texto" text NOT NULL, 
    "created" datetime NOT NULL, 
    "estado" varchar(10) NOT NULL
    );
COMMIT;
