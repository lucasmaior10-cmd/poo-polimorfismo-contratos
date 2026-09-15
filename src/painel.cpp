#include "painel.hpp"
#include <sstream>
#include <iomanip>

std::string linhaPainel(const Sensor& sensor) {
    std::ostringstream ss;
    
    ss << sensor.tag() << ": " 
       << std::fixed << std::setprecision(1) << sensor.valor() << " " 
       << sensor.unidade() << " | " 
       << (sensor.emAlerta() ? "ALERTA" : "OK");
       
    return ss.str();
}
