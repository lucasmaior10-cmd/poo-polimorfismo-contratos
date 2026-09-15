# Modelo a completar
classDiagram
    class Sensor {
        <<abstract>>
        -string tag_
        +tag() string
        +valor()* double
        +unidade()* string
        +atualizar(double)* bool
        +emAlerta()* bool
    }

    class SensorNivel {
        -double valor_
        +valor() double
        +unidade() string
        +atualizar(double) bool
        +emAlerta() bool
    }

    class SensorTemperatura {
        -double valor_
        +valor() double
        +unidade() string
        +atualizar(double) bool
        +emAlerta() bool
    }

    class SensorPressao {
        -double valor_
        +valor() double
        +unidade() string
        +atualizar(double) bool
        +emAlerta() bool
    }

    class Painel {
        +linhaPainel(Sensor) string
    }

    Sensor <|-- SensorNivel
    Sensor <|-- SensorTemperatura
    Sensor <|-- SensorPressao
    Painel ..> Sensor

