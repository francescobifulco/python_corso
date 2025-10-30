-- SQLite
CREATE TABLE IF NOT EXISTS notes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content text NOT NULL,
    lat real,
    lng real,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);