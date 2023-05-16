const express = require('express');
const os = require('os');

const app = express();

const Pool = require('pg').Pool;
const pool = new Pool({
  user: 'citus',
  host: 'c.jonnys-prediction-data-store.postgres.database.azure.com',
  database: 'citus',
  password: 'get_your_own_password',
  port: 5432,
  ssl: true,
});

app.use(express.static('dist'));
app.get('/api/getUsername', (req, res) => res.send({ username: os.userInfo().username }));

app.get('/api/getData', (req, res) => {
    pool.query(`
    SELECT 
    t0.market_name,
    t0.name,
    t0.price, 
    t0.timestamp,
    t0.market_image,
    t0.image
    FROM market_data t0
    JOIN (
        SELECT data_id, MAX(timestamp) as max_ts
        FROM market_data
        GROUP BY 1
    ) as t1 on t1.data_id = t0.data_id and t1.max_ts = t0.timestamp
    `, (error, results) => {
    if (error) {
      throw error
    }
    res.send(results.rows)
  })
});



app.listen(process.env.PORT || 8080, () => console.log(`Listening on port ${process.env.PORT || 8080}!`));
