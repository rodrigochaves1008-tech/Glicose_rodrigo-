# Estado atual do projeto (atualizado em 20/11/2026 ~15h40)

Ao retomar, leia este arquivo e depois `CLAUDE.md`, `PERFIL.md`, `TESTES.md` e `ANALISES.md`, se precisar de detalhes.

## Rodrigo (resumo do perfil)
- Sem diabetes, sem remédios. Rotina: low-carb/cetogênica, refeições cedo, **sem jantar**. Acorda ~04h e treina cedo.
- **Os horários que ele informa são exatos.** Ele registra refeições, bebidas, treinos (superiores × inferiores) e sintomas na hora.

## Sensor
- Accu-Chek SmartGuide no **braço direito**, aplicado em 13/11 ~14:55. **Troca em 27/11** (próximo no braço esquerdo; ter glicosímetro em casa e calibrar logo no início).
- Calibrado em 14/11: 16:08 (dedo 99 × sensor 80) e 16:43 (dedo 92 × sensor 75,5). Antes das 16:43 de 14/11, as leituras estão ~15–20 abaixo do real.
- Adesivo soltando na borda desde 16/11: usar esparadrapo ou Tegaderm, **nunca cola**.
- Alertas no app: baixa 60, alta 180.

## Como processar uma exportação (Exportar.zip)
1. Descompactar numa pasta nova no scratchpad.
2. `python3 -I scripts/processar_export.py <pasta>/dataPoints.jsonl relatorios/originais/AAAA-MM-DD_export_cgm.csv "AAAA-MM-DD HH:MM" "AAAA-MM-DD HH:MM"`
3. Escrever o resumo em `relatorios/resumos/`, atualizar `ANALISES.md`, `TESTES.md` (resultados), o diário e este arquivo. Fazer commit e push.
- **Última exportação processada: 20/11 12:33** (`relatorios/originais/2026-11-20_export_cgm.csv`, resumo `relatorios/resumos/2026-11-18_tarde_a_2026-11-20_almoco.md`).

## Plano
- **Fase 1 (13–18/11), testes com carboidrato: ENCERRADA.** Ficaram para o próximo sensor: A1 arroz, A2 arroz + feijão, A3 banana, A4 pão francês, A5 pão + ovos, A6 ordem dos alimentos, C1 caminhada após comer, C3 academia após o pão, T3 pastelão sozinho, A7 Coca sozinha (com quantidade), repetir a tapioca.
- **Fase 2 (19–26/11), low-carb sem interrupção e sem jantar.** 19/11 = dia 1.
  - 20/11: fava com toucinho em **porção grande** no almoço (~40–60 g de carboidrato).
  - 20/11 ~20:15: **jantar com carboidrato** (frango, batata frita, baião), fora do plano. Madrugada de 21/11 não conta como low-carb; cetose provavelmente mais tarde que 24–25/11.
  - Ele estima voltar à cetose em **24–25/11** → só ~2 dias de dados em cetose antes da troca. Fitas de cetona na urina (farmácia) foram sugeridas para confirmar.

## O que analisar na próxima exportação
- **Jantar de 20/11 ~20:15** (frango + batata frita + baião): pico, duração, ondas e efeito na madrugada de 21/11 × pastelão (16/11, noite: 194,5) e pizza (15/11: 172). Se exportar só amanhã, a fava e o jantar saem juntos.
- **Fava em porção grande (20/11 11:49)**: só 44 min de dados (84 → 108, ainda subindo). Ver pico, tempo e volta à base × sopa de feijão (15/11: pico 127).
- Madrugadas de 21/11 em diante: continuar caindo de 86 para 70–85? Jejum < 100?
- Subidas à tarde **sem comer** (18/11 15:28 e 19/11 15:43, confirmado): ver se repetem ~3–4 h depois do almoço (provável onda tardia de proteína/gordura) e cruzar com café puro, cochilo e estresse.

## Resultados da exportação de 20/11 (resumo)
- Fase 2: 100% em 70–140, máximo 120. Manhãs em jejum com CV 3% (18, 19, 20/11).
- Madrugadas: 96 (19/11) → **86** (20/11). Antes do café: 102 → 94.
- KitKat 18/11: +45 (igual a 17/11, +43). Queda a 72 às 18:19 = provável artefato.
- Café + treino de braço (20/11): 94 → 120,5 → base em ~2 h. Os efeitos somam.

## Sintomas e fatores de confusão
- 16/11: garganta inflamada (melhorou em 17/11). 19/11: **corpo pesado + sem voz** (provável virose/laringite leve). Inflamação pode subir a glicose.
- Fome e vontade de doce incomuns desde 16/11 (provável saída da cetose). Devem sumir na fase 2.
- 19/11: Red Bull zero de manhã + cochilo → melhorou um pouco.
- Sono ruim em várias noites.

## Teoria do Rodrigo (saída da cetose)
- Madrugadas: 75 → 92 → 113 → **90** (15–18/11). Previsão 1 (estabilizar) confirmada.
- Previsão 3 (madrugadas mais baixas no low-carb): **começando a se confirmar**: 96 (19/11) → 86 (20/11).
- Falta: previsão 2 (picos menores com os dias de carboidrato; o chocotone de 400 g deu só 146) — fica para o próximo sensor.

## Principais conclusões até agora
- Glicose bem regulada: base ~90–97, nenhum valor abaixo de 54 depois da calibração, só 1 pico acima de 180 (pastelão + Coca, 194,5). Volta à base em 2–3 h na maioria das refeições.
- Proteína/gordura quase não mexem (manhã de 18/11: CV 3%). Feijão sobe pouco. Amido refinado e açúcar sobem rápido; com gordura junto, a curva fica longa e em ondas (pizza, chocotone ~8 h).
- Treino de pernas baixa a glicose (−30); treino de braços sobe um pouco (+17).

## Ponto de atenção médico
- Jejum acima de 100 em dias de rotina low-carb, picos acima de 180 com refeições pequenas, volta à base acima de 3 h, ou rouquidão por mais de 2–3 semanas.

## Perguntas ainda sem resposta
- Quantidade do panetone e da Coca-Cola de 18/11. Tamanho do iogurte integral de 19/11.
