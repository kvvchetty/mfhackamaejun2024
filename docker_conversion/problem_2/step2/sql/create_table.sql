
-- Create the Property table
CREATE TABLE Property (
    property_id INT PRIMARY KEY,
    address VARCHAR(255),
    vacancy_rate DECIMAL(5, 2),
    tenant_turnover_rate DECIMAL(5, 2),
    risk_score INT
);

-- Create the Tenant table
CREATE TABLE Tenant (
    tenant_id INT PRIMARY KEY,
    name VARCHAR(100),
    income_level DECIMAL(10, 2),
    voucher_value DECIMAL(10, 2),
    tenancy_history VARCHAR(255),
    risk_rating VARCHAR(20)
);

-- Create the Voucher table
CREATE TABLE Voucher (
    voucher_id INT PRIMARY KEY,
    value DECIMAL(10, 2),
    issuance_date DATE,
    expiration_date DATE,
    payment_status VARCHAR(20)
);

-- Create the Owner/Landlord table
CREATE TABLE OwnerLandlord (
    owner_id INT PRIMARY KEY,
    name VARCHAR(100),
    contact_information VARCHAR(255)
);

-- Create the Region table
CREATE TABLE Region (
    region_id INT PRIMARY KEY,
    region_name VARCHAR(100),
    state VARCHAR(50)
);

-- Create the Alert table
CREATE TABLE Alert (
    alert_id INT PRIMARY KEY,
    alert_type VARCHAR(50),
    description TEXT,
    date_time DATETIME,
    status VARCHAR(20)
);

-- Define relationships (foreign keys)
ALTER TABLE Property ADD COLUMN owner_id INT;
ALTER TABLE Property ADD COLUMN region_id INT;
ALTER TABLE Tenant ADD COLUMN property_id INT;
ALTER TABLE Voucher ADD COLUMN tenant_id INT;
ALTER TABLE Alert ADD COLUMN property_id INT;
ALTER TABLE Alert ADD COLUMN tenant_id INT;
ALTER TABLE Alert ADD COLUMN voucher_id INT;

-- Add foreign key constraints
ALTER TABLE Property ADD CONSTRAINT fk_property_owner FOREIGN KEY (owner_id) REFERENCES OwnerLandlord(owner_id);
ALTER TABLE Property ADD CONSTRAINT fk_property_region FOREIGN KEY (region_id) REFERENCES Region(region_id);
ALTER TABLE Tenant ADD CONSTRAINT fk_tenant_property FOREIGN KEY (property_id) REFERENCES Property(property_id);
ALTER TABLE Voucher ADD CONSTRAINT fk_voucher_tenant FOREIGN KEY (tenant_id) REFERENCES Tenant(tenant_id);
ALTER TABLE Alert ADD CONSTRAINT fk_alert_property FOREIGN KEY (property_id) REFERENCES Property(property_id);
ALTER TABLE Alert ADD CONSTRAINT fk_alert_tenant FOREIGN KEY (tenant_id) REFERENCES Tenant(tenant_id);
ALTER TABLE Alert ADD CONSTRAINT fk_alert_voucher FOREIGN KEY (voucher_id) REFERENCES Voucher(voucher_id);

