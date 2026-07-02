-- ============================================
-- Dutypar Database Setup for XAMPP MySQL
-- Port: 3306
-- ============================================

-- Drop database if exists (be careful in production!)
DROP DATABASE IF EXISTS dutypar;

-- Create database with UTF-8 support
CREATE DATABASE dutypar 
    CHARACTER SET utf8mb4 
    COLLATE utf8mb4_unicode_ci;

-- Use the database
USE dutypar;

-- Verify database created
SELECT 'Database "dutypar" created successfully!' AS Status;
SHOW DATABASES LIKE 'dutypar';
