#!/usr/bin/node
const request = require('request');
const api_url = 'https://swapi-api.alx-tools.com/api';


if (process.argv.length > 2) {
  const urlMovie = `${api_url}/films/${process.argv[2]}/`;

  request(urlMovie, function (err, _, body) {
    if (err == null) {
    const fbody = JSON.parse(body).characters;

    const characters = fbody.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseErr, _, charactersReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
          }
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));

    Promise.all(characters)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
    } else {
      console.log(err);
    }
  });
}
