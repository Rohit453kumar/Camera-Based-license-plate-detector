CREATE DATABASE license;
use license;
create table vehicle_registration(license_plate VARCHAR(20) PRIMARY KEY NOT NULL,
    owner_name VARCHAR(100) NOT NULL,
    reg_date DATE NOT NULL,
    vehicle_type Varchar(100) NOT NULL);
Create table Driver_license(
licenseno VARCHAR(50) PRIMARY KEY NOT NULL,
	dlname VARCHAR(100) NOT NULL,
    address VARCHAR(1000) NOT NULL,
    license_plate VARCHAR(20) NOT NULL,
    FOREIGN KEY(license_plate) REFERENCES vehicle_registration(license_plate));
CREATE TABLE Violations (
    violation_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    license_plate VARCHAR(20) NOT NULL,
    violation_type VARCHAR(100) NOT NULL,
    violation_date DATE NOT NULL,
    fine_amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (license_plate) REFERENCES vehicle_registration(license_plate)
);
CREATE TABLE Emissions (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    license_plate VARCHAR(20) NOT NULL,
    puc_expiry_date DATE NOT NULL,
    FOREIGN KEY (license_plate) REFERENCES vehicle_registration(license_plate)
);

CREATE TABLE Insurance (
    policy_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    license_plate VARCHAR(20) NOT NULL,
    expiry_date DATE NOT NULL,
    company VARCHAR(20) NOT NULL,
    FOREIGN KEY (license_plate) REFERENCES vehicle_registration(license_plate)
    );

select * from vehicle_registration;
select * from driver_license;
select * from violations;
select * from emissions;
select * from insurance;