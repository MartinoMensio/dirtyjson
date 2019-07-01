const express = require('express');
const dJSON = require('dirty-json');
const bodyParser = require('body-parser');


const app = express();
app.use(bodyParser.text());
PORT = 12345

function fix_json(input_string){
    const r = dJSON.parse(input_string)
    //return JSON.stringify(r);
    return r
}

app.post('/', (req, res) => {
  return res.send(fix_json(req.body));
});

app.listen(PORT, () =>
  console.log(`Example app listening on port ${PORT}!`),
);
