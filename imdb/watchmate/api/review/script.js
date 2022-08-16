const allowedToSeeMovie = (age, accompanied = true) =>
  age > 13 || accompanied
    ? console.log("You're aloowed to see the movie")
    : console.log("Sorry you can see the movie");

allowedToSeeMovie(13);
