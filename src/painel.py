from sensores import Sensor

def linha_painel(sensor: Sensor) -> str:
    estado = "ALERTA" if sensor.em_alerta() else "OK"
    return f"{sensor.tag()}: {sensor.valor():.1f} {sensor.unidade()} | {estado}"
