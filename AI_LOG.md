
# Rastreabilidade de IA

| Pedido ao agente | Aceito/rejeitado | Justificativa técnica e verificação |
|---|---|---|
| Implementação do painel polimórfico e sensor de pressão em C++ e Python | Aceito | Códigos desenvolvidos mantendo o contrato estável e validações corretas. Testes locais aprovados com sucesso. |

## Justificativa Funcional (Etapa 01)
O valor de leitura 15 provoca alerta no SensorNivel porque o seu contrato define que qualquer valor estritamente menor que 20% caracteriza uma situação de alerta (leitura < 20). Já para o SensorTemperatura, o alerta só é disparado se a leitura for estritamente maior que 45°C (leitura > 45), fazendo com que o valor 15 seja considerado seguro (OK).
