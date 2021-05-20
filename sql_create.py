import pandas as pd

df = pd.read_csv("./IMD.tsv", header=None,sep='\t')

text = """
DROP SCHEMA IF EXISTS IMD_db;
CREATE SCHEMA IMD_db;
USE IMD_db;
SET AUTOCOMMIT=0;
SET global max_allowed_packet=123456780;

DROP TABLE IF EXISTS `IMD_table`;
CREATE TABLE `IMD_table` (
    `ID` INT(11) NOT NULL PRIMARY KEY,
    `content` TEXT(2000) NOT NULL
);
BEGIN;
"""

count = 1
for i in df.values:
    text += "INSERT INTO `IMD_table` VALUES (" + str(count) + ", N'" + i[0].replace("'", " ") + "');\n"
    count += 1

text += "COMMIT;"

f = open('IMD.sql', 'w', encoding="utf8")

f.write(text)

f.close()