-- Crear base de datos
CREATE DATABASE IF NOT EXISTS leads_db;
USE leads_db;

-- Crear tabla de leads
CREATE TABLE IF NOT EXISTS leads (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    interest VARCHAR(50) NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- OPERACIONES CRUD

-- CREATE: Insertar nuevo lead
INSERT INTO leads (name, email, phone, interest) 
VALUES ('Juan Pérez', 'juan@example.com', '+1 (555) 123-4567', 'Consultoría Tecnológica');

-- READ: Seleccionar todos los leads
SELECT * FROM leads;

-- READ: Seleccionar lead por email
SELECT * FROM leads WHERE email = 'juan@example.com';

-- UPDATE: Actualizar información de lead
UPDATE leads 
SET phone = '+1 (555) 987-6543', interest = 'Desarrollo de Software' 
WHERE email = 'juan@example.com';

-- DELETE: Eliminar lead
DELETE FROM leads WHERE email = 'juan@example.com';

-- Consulta para verificar la tabla
DESCRIBE leads;