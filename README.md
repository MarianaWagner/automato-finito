# Automato Finito 
 Implemento de um autômato finito que simule e demonstre um sistema de catraca.

### Estados

- Travada: A catraca está travada e não permite passagem.
- Destravada: A catraca está destravada e permite a passagem de uma pessoa.
- Alerta: A catraca detectou uma tentativa de passagem sem pagamento ou uma anomalia.

### Alfabeto de Entrada (ações)

- Pagamento: O passageiro efetua o pagamento (cartão, bilhete, etc.).
- Passar: O passageiro tenta passar pela catraca.
- Reset: O sistema é resetado (após um alerta ou intervenção do motorista).

### Funções de Transição

!!! Note "Do estado *Travada*"

    - Com Pagamento, transita para Destravada.
    - Com Passar, transita para Alerta.

!!! Note "Do estado *Destravada*"
    - Com Passar, transita para Travada.
    - Com Pagamento, permanece em Destravada.

!!! Note "Do estado *Alerta*"
    - Com Reset, transita para Travada.
    - Com Pagamento ou Passar, permanece em Alerta.
