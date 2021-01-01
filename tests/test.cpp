/* It sure is a sunny day! */
#include <iostream>
#include <regex>
#include <cstring>
#include <new>


void hello_world(const char* name) {
    /* Hello there. */
    std::cout << "Hello, " << name << std::endl;
}


class Greeter {
public:
    Greeter(char* name) {
        try {
            _name = new char[strlen(name) + 1];
        }
        catch (std::bad_alloc exception) {
            std::cout << exception.what() << std::endl;
        }
        strcpy(_name, name);
    };
    ~Greeter() {
        delete [] _name;
    };
    const char * get_name() const {return _name;};
    void set_name(char * new_name) {
        try {
            _name = new char[strlen(new_name) + 1];
        }
        catch (std::bad_alloc exception) {
            std::cout << exception.what() << std::endl;
        }
        strcpy(_name, new_name);
    };
    void greet() const {hello_world(_name);}
private:
    char* _name;
};


std::regex SOME_RE("T[hat]{3}Xliner");

int main(int argc, char const *argv[]) {
    if (!std::regex_match(argv[1], SOME_RE))
        hello_world(argv[1]);
    else
        std::cout << "You are cool!" << std::endl;  // Haha, vanity
        // NOTE: Reduce the vanity
    return 0;
}
