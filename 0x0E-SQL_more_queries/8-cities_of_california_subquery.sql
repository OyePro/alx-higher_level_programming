-- cities of California in `hbtn_0d_usa` database

  SELECT id, name
    FROM cities
   WHERE state_id = 1
ORDER BY id;
