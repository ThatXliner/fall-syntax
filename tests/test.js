/* It sure is a sunny day! */

function hello_word(name) {
  console.log(`Hello ${name}`);
}

var SOME_RE = new RegExp("T[hat]{3}Xliner");

var argv = process.argv.slice(2);

if (require.main === module) {
  if !( argv[1].match(SOME_RE) ) {
    hello_world(argv[1]);
  } else {
    console.log("You are cool!"); // haha, vanity
    // NOTE: Reduce the vanity
  };
};
