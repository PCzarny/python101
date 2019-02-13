DROP TABLE IF EXISTS tasks;
CREATE TABLE tasks (
  id integer primary key autoincrement,
  description text not null,
  done boolean not null,
  added_at datetime not null
);

INSERT INTO tasks (id, description, done, added_at)
VALUES (null, 'Feed cat', 0, datetime(current_timestamp));
INSERT INTO tasks (description, done, added_at)
VALUES ('Wash dishes', 0, datetime(current_timestamp));
