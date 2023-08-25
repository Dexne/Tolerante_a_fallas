#include <iostream>
#include <fstream>

std::string readFromFile(const std::string& filename) {
    try {
        std::ifstream file(filename);
        if (!file.is_open()) {
            throw std::runtime_error("Error: No se puede abrir el archivo.");
        }
        
        std::string content((std::istreambuf_iterator<char>(file)),
                             (std::istreambuf_iterator<char>()));
        return content;
    } catch (const std::exception& e) {
        std::cerr << e.what() << std::endl;
        return "";
    }
}

int main() {
    std::string filename = "archivo.txt";
    std::string content = readFromFile(filename);
    if (!content.empty()) {
        std::cout << "Contenido del archivo: " << content << std::endl;
    }

    return 0;
}
