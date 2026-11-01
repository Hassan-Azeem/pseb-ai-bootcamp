CREATE DATABASE IF NOT EXISTS library;
USE library;

CREATE TABLE IF NOT EXISTS books (
    id INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

INSERT INTO books (id, title, author, year, price) VALUES
    (1, 'The Hobbit', 'J. R. R. Tolkien', 1937, 450.00),
    (2, '1984', 'George Orwell', 1949, 520.00),
    (3, 'Pride and Prejudice', 'Jane Austen', 1813, 380.00),
    (4, 'To Kill a Mockingbird', 'Harper Lee', 1960, 610.00),
    (5, 'The Great Gatsby', 'F. Scott Fitzgerald', 1925, 490.00),
    (6, 'The Catcher in the Rye', 'J. D. Salinger', 1951, 550.00),
    (7, 'Brave New World', 'Aldous Huxley', 1932, 575.00),
    (8, 'Fahrenheit 451', 'Ray Bradbury', 1953, 430.00);

-- Books priced above 500.
SELECT id, title, author, year, price
FROM books
WHERE price > 500;

-- All books, from highest to lowest price.
SELECT id, title, author, year, price
FROM books
ORDER BY price DESC;

-- Number of books in the table.
SELECT COUNT(*) AS book_count
FROM books;

-- Update the price of one book by its unique id.
UPDATE books
SET price = 475.00
WHERE id = 1;
