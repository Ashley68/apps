-- Table: phonebook

-- DROP TABLE phonebook;

CREATE TABLE phonebook
(
  id integer NOT NULL,
  last_name character(50),
  first_name character(50),
  home_phone character(25),
  cell_phone character(25),
  office_phone character(25),
  email character(50),
  notes text,
  birth_date date,
  CONSTRAINT phonebook_pkey PRIMARY KEY (id)
)
ALTER TABLE phonebook
  OWNER TO postgres;
  
insert into phonebook values (1, 'Smith', 'John','510-111-2345','408-111-2345','650-111-2345','jsmith@gmail.com','Likes cheese', '12-12-1983')
insert into phonebook values (2, 'Show', 'Rachel','510-146-2945','408-721-2365','650-192-1845','rsho23@gmail.com','Likes roses', '03-19-1976')
insert into phonebook values (3, 'Herbin', 'Charles','510-192-2295','408-231-2125','650-192-1325','cherbin@gmail.com','Likes whiskey', '03-12-1968')