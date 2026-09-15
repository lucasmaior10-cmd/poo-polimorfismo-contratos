#ifndef SENSORES_HPP
#define SENSORES_HPP

#include <string>
#include <cmath>
#include "sensor.hpp"

class SensorNivel : public Sensor {
private:
    double valor_ = 50.0;
public:
    SensorNivel(const std::string& tag) : Sensor(tag) {}

    double valor() const override { return valor_; }
    std::string unidade() const override { return "%"; }

    bool atualizar(double leitura) override {
        if (!std::isfinite(leitura) || leitura < 0.0 || leitura > 100.0) {
            return false;
        }
        valor_ = leitura;
        return true;
    }

    bool emAlerta() const override {
        return valor_ < 20.0;
    }
};

class SensorTemperatura : public Sensor {
private:
    double valor_ = 25.0;
public:
    SensorTemperatura(const std::string& tag) : Sensor(tag) {}

    double valor() const override { return valor_; }
    std::string unidade() const override { return "C"; }

    bool atualizar(double leitura) override {
        if (!std::isfinite(leitura) || leitura < -40.0 || leitura > 125.0) {
            return false;
        }
        valor_ = leitura;
        return true;
    }

    bool emAlerta() const override {
        return valor_ > 45.0;
    }
};

class SensorPressao : public Sensor {
private:
    double valor_ = 1.0;
public:
    SensorPressao(const std::string& tag) : Sensor(tag) {}

    double valor() const override { return valor_; }
    std::string unidade() const override { return "bar"; }

    bool atualizar(double leitura) override {
        if (!std::isfinite(leitura) || leitura < 0.0 || leitura > 10.0) {
            return false;
        }
        valor_ = leitura;
        return true;
    }

    bool emAlerta() const override {
        return valor_ > 8.0;
    }
};

#endif