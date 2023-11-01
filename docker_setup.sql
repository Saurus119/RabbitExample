-- create login for user
CREATE LOGIN testUser WITH PASSWORD = 'StrongPassword!123';

-- create user
CREATE USER testUser FOR LOGIN testUser;

-- set permissions
ALTER ROLE db_datareader ADD MEMBER testUser;
ALTER ROLE db_datawriter ADD MEMBER testUser;

-- Create table
CREATE TABLE dbo.Cosmonauts (
	Id int IDENTITY(1,1) NOT NULL,
	Name nchar(30) NOT NULL,
	Date date NULL
)
