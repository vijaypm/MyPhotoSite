BEGIN;
CREATE TABLE "MyPhotos_user" (
    "id" integer NOT NULL PRIMARY KEY,
    "username" varchar(80) NOT NULL,
    "hash_pwd" varchar(64) NOT NULL,
    "email" varchar(80) NOT NULL,
    "createdt" datetime NOT NULL,
    "moddt" datetime NOT NULL,
    "verified" bool NOT NULL,
    "verify_code" varchar(255) NOT NULL,
    "verifydt" datetime NOT NULL
)
;
CREATE TABLE "MyPhotos_useralbum" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL REFERENCES "MyPhotos_user" ("id"),
    "name" varchar(80) NOT NULL,
    "createdt" datetime NOT NULL,
    "moddt" datetime NOT NULL
)
;
CREATE TABLE "MyPhotos_albumphoto" (
    "id" integer NOT NULL PRIMARY KEY,
    "album_id" integer NOT NULL REFERENCES "MyPhotos_useralbum" ("id"),
    "filename" varchar(80) NOT NULL,
    "createdt" datetime NOT NULL,
    "moddt" datetime NOT NULL
)
;

COMMIT;
