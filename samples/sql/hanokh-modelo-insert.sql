-- USE hanokh-auth01;

-- Table Country
INSERT INTO country(country_name, initials_country)
  VALUES ('Brasil', 'BR');

-- Table state
INSERT INTO state(state_name, initials_state, id_country)
  VALUES ('Santa Catarina', 'SC', 1);

-- Table city
INSERT INTO city(city_name, id_state)
  VALUES ('São Francisco do Sull', 1);

-- Table neighborhood
INSERT INTO neighborhood(neighborhood_name, id_city)
  VALUES ('Rocio Pequeno', 1);

--Table Street
INSERT INTO street(cep, street_name, id_neighborhood)
  VALUES ('89240-000', 'Rua Alcides Teixeira', 1);

-- Table address
INSERT INTO address(home_number, additional_information, id_street)
  VALUES (110, 'Rua é proxima a padaria Delícias do Sul', 1);

--Table person
INSERT INTO person(name, surname, email, username, password, id_address)
  VALUES ('Eli', 'Pereira', 'elipe.pereira@gmail.com', 'eli',
    '7523fd6ed3c3da1c0352782ab716b28cd5017c2182fe124dec2989c937387950159a44460fde8405fae90b4bc5d83eb67c508978b45e72471d538d279de98190', 1);

INSERT INTO team(team_name) VALUES('admin');

INSERT INTO team_person(id_person, id_team) VALUES (1, 1);
