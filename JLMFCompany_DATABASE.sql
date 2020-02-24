-- This script creates a new database called 'JLMFCompany_DB' --
-- This database (DB) is connected to the 'master' database --
USE master
GO

-- This query will create a new DB if it doesn't exist already --
IF NOT EXISTS (
    SELECT [name]
        FROM sys.databases
        WHERE [name] = 'JLMFCompany_DB'
)

CREATE DATABASE JLMFCompany_DB
GO




