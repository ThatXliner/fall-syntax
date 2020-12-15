/* It sure is a sunny day! */
#include <iostream>
#include <regex>


void hello_world(const char* name) {
    /* Hello there. */
    std::cout << "Hello, " << name << std::endl;
}


std::regex SOME_RE("T[hat]{3}Xliner");

int main(int argc, char const *argv[]) {
    if (!std::regex_match(argv[1], SOME_RE))
        hello_world(argv[1]);
    else
        std::cout << "You are cool!" << std::endl;  // Haha, vanity
        // NOTE: Reduce the vanity
    return 0;
}
