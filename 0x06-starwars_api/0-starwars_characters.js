#!/usr/bin/node
const request = require("request");

const movieID = process.argv[2];

request
  .get(`https://swapi-api.alx-tools.com/api/films/${movieID}`)
  .on("data", (data) => {
    const charactersURL = JSON.parse(data)?.["characters"];
    const characters = charactersURL.map(
      (url) =>
        new Promise((resolve) =>
          request
            .get(url)
            .on("data", (data_2) => resolve(JSON.parse(data_2).name))
        )
    );
    Promise.all(characters)
      .then((names) => console.log(names.join("\n")))
      .catch((allErr) => console.log(allErr));
  });
