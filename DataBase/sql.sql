create table samplers(
    `client_id` text not null,
    `lng` double not null,
    `lat` double not null
);

CREATE TABLE climate_data(
	`data_id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `client_id` text NOT NULL,
    `date` date NOT NULL,
    `time` time NOT NULL,
    `data` text NOT NULL
);

