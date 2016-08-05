--preset DB create statement
--primary design for future expand is dynamic script slots
CREATE TABLE leaks
(
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    leakname TEXT NOT NULL,
    cvename TEXT,
    leakdesc TEXT,
    dbtypes INTEGER NOT NULL,
    dbtype TEXT,
    dbversion TEXT,
    ostypeCnt INTEGER NOT NULL,
    ostype TEXT,
    osversion TEXT,
    reqpwd INTEGER NOT NULL,
    username TEXT,
    usepwd TEXT,
    scriptname TEXT
);

CREATE TABLE dbs
(
  id        INTEGER PRIMARY KEY,
  dbname    TEXT    NOT NULL,
  dbip      TEXT    NOT NULL,
  dbtype    INTEGER NOT NULL,
  dbversion TEXT,
  ostype    INTEGER,
  osversion TEXT,
  dbport    INTEGER NOT NULL,
  orasid    TEXT,
  username  TEXT,
  userpwd   TEXT
);
CREATE TABLE sqlite_sequence
(
  name TEXT,
  seq  TEXT
);


INSERT INTO dbs (dbname, dbip, dbtype, dbversion, ostype, osversion, dbport, orasid, username, userpwd)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
UPDATE dbs
SET dbname = ?, dbip = ?, dbtype = ?, dbversion = ?, ostype = ?, osversion = ?, dbport = ?, orasid = ?, username = ?,
  userpwd  = ?
WHERE id = ?;