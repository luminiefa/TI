ALTER TABLE <table>
 -ADD(<collones>)
 -ALTER COLUMN
 -DROP
 ou DROP COLUMN

 DROP TABLE <table>
 TRUNCAD


-1.3
    CONSTRAINT PK_PLANNING_TYPE PRIMARY KEY (Collecte,Type_Collecte);
-1.1
    ALTER TABLE Personne
        - DROP COLUMN téléphone
-1.3
    ALTER TABLE Zone
    ADD chef int FOREIGN KEY REFERENCES PERSONNEL(id);
    