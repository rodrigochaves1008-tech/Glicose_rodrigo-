# Estado atual do projeto (atualizado em 20/11/2026 ~12h)

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
- **Última exportação processada: 18/11 17:19.** Os dias 18 (noite), 19 e 20/11 ainda não foram analisados.

## Plano
- **Fase 1 (13–18/11), testes com carboidrato: ENCERRADA.** Ficaram para o próximo sensor: A1 arroz, A2 arroz + feijão, A3 banana, A4 pão francês, A5 pão + ovos, A6 ordem dos alimentos, C1 caminhada após comer, C3 academia após o pão, T3 pastelão sozinho, A7 Coca sozinha (com quantidade), repetir a tapioca.
- **Fase 2 (19–26/11), low-carb sem interrupção e sem jantar.** 19/11 = dia 1.
  - 20/11: fava com toucinho em **porção grande** no almoço (~40–60 g de carboidrato).
  - Ele estima voltar à cetose em **24–25/11** → só ~2 dias de dados em cetose antes da troca. Fitas de cetona na urina (farmácia) foram sugeridas para confirmar.

## O que analisar na próxima exportação
- Madrugadas de 19 e 20/11 (previsão: cair de ~90 para 70–85) e jejum (< 100).
- KitKat de 18/11 16:58 (comparar com o de 17/11: 95 → 138).
- Treino de braço **depois de comer** (20/11 05:15) × treino de braço em jejum (18/11: 100 → 117 → 98).
- Fava em porção grande (20/11 11:49) × sopa de feijão (15/11: pico 127).
- Iogurte integral (19/11 13:34, tamanho não informado).

## Sintomas e fatores de confusão
- 16/11: garganta inflamada (melhorou em 17/11). 19/11: **corpo pesado + sem voz** (provável virose/laringite leve). Inflamação pode subir a glicose.
- Fome e vontade de doce incomuns desde 16/11 (provável saída da cetose). Devem sumir na fase 2.
- 19/11: Red Bull zero de manhã + cochilo → melhorou um pouco.
- Sono ruim em várias noites.

## Teoria do Rodrigo (saída da cetose)
- Madrugadas: 75 → 92 → 113 → **90** (15–18/11). Previsão 1 (estabilizar) confirmada.
- Faltam: previsão 2 (picos menores com os dias de carboidrato; o chocotone de 400 g deu só 146) e previsão 3 (madrugadas mais baixas na fase low-carb).

## Principais conclusões até agora
- Glicose bem regulada: base ~90–97, nenhum valor abaixo de 54 depois da calibração, só 1 pico acima de 180 (pastelão + Coca, 194,5). Volta à base em 2–3 h na maioria das refeições.
- Proteína/gordura quase não mexem (manhã de 18/11: CV 3%). Feijão sobe pouco. Amido refinado e açúcar sobem rápido; com gordura junto, a curva fica longa e em ondas (pizza, chocotone ~8 h).
- Treino de pernas baixa a glicose (−30); treino de braços sobe um pouco (+17).

## Ponto de atenção médico
- Jejum acima de 100 em dias de rotina low-carb, picos acima de 180 com refeições pequenas, volta à base acima de 3 h, ou rouquidão por mais de 2–3 semanas.

## Perguntas ainda sem resposta
- Quantidade do panetone e da Coca-Cola de 18/11. Tamanho do iogurte integral de 19/11.
