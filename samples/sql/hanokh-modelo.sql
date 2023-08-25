-- CREATE DATABASE hanokh-auth01;

-- USE hap;

CREATE TABLE country (
  id_country SERIAL PRIMARY KEY,
  country_name VARCHAR(50),
  initials_country TEXT
);

CREATE TABLE state (
  id_state SERIAL PRIMARY KEY,
  state_name VARCHAR(50),
  initials_state VARCHAR(5),
  id_country INT REFERENCES country(id_country)
);

CREATE TABLE city (
  id_city SERIAL PRIMARY KEY,
  city_name VARCHAR(50),
  id_state INT REFERENCES state(id_state)
);

CREATE TABLE neighborhood (
  id_neighborhood SERIAL PRIMARY KEY,
  neighborhood_name VARCHAR(50),
  id_city INT REFERENCES city(id_city)
);

CREATE TABLE street (
  id_street SERIAL PRIMARY KEY,
  cep VARCHAR(50),
  street_name VARCHAR(50),
  id_neighborhood INT REFERENCES neighborhood(id_neighborhood)
);

CREATE TABLE address (
  id_address SERIAL PRIMARY KEY,
  home_number INT,
  additional_information VARCHAR(500),
  id_street INT REFERENCES street(id_street)
);

CREATE TABLE person (
  id_person SERIAL PRIMARY KEY,
  name VARCHAR(50),
  surname VARCHAR(50),
  email VARCHAR(50),
  username VARCHAR(50),
  password VARCHAR(500),
  id_address INT REFERENCES address(id_address)
);

CREATE TABLE team (
  id_team SERIAL PRIMARY KEY,
  team_name VARCHAR(200)
);

CREATE TABLE team_person (
  id_team_person SERIAL PRIMARY KEY,
  id_person INT REFERENCES person(id_person),
  id_team INT REFERENCES team(id_team)
);
