# Estado atual do projeto (atualizado em 21/11/2026 ~13h)

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
- **Última exportação processada: 21/11 12:53** (`relatorios/originais/2026-11-21_export_cgm.csv`, resumo `relatorios/resumos/2026-11-20_almoco_a_2026-11-21_almoco.md`).

## Plano
- **Fase 1 (13–18/11), testes com carboidrato: ENCERRADA.** Ficaram para o próximo sensor: A1 arroz, A2 arroz + feijão, A3 banana, A4 pão francês, A5 pão + ovos, A6 ordem dos alimentos, C1 caminhada após comer, C3 academia após o pão, T3 pastelão sozinho, A7 Coca sozinha (com quantidade), repetir a tapioca.
- **Fase 2 (19–26/11), low-carb sem interrupção e sem jantar.** 19/11 = dia 1.
  - 20/11: fava com toucinho em **porção grande** no almoço (~40–60 g de carboidrato).
  - 20/11 ~20:15: **jantar com carboidrato** (frango, batata frita, baião), fora do plano → pico 184,5. Madrugada de 21/11 não conta como low-carb; cetose provavelmente ~25–26/11.
  - Ele estima voltar à cetose em **24–25/11** → só ~2 dias de dados em cetose antes da troca. Fitas de cetona na urina (farmácia) foram sugeridas para confirmar.

## O que analisar na próxima exportação
- Madrugadas de 22/11 em diante (low-carb de novo): voltar para ~86 ou menos? Jejum < 100?
- A onda sem comer ~3–4 h depois do almoço continua (18, 19 e 20/11)?
- Refeições de 21/11 depois das 12:53 (ainda não informadas).

## Resultados das exportações de 20 e 21/11 (resumo)
- Fase 2 sem o jantar: 100% em 70–140. Manhãs em jejum com CV 3–7%.
- Madrugadas: 96 (19/11) → **86** (20/11) → 102 (21/11, depois do jantar com batata frita + baião).
- **Fava porção grande: 128,5** (igual à sopa de feijão). **Jantar frango + batata frita + baião: 184,5**, ~5h15 em ondas (2º valor > 180; os dois foram jantares com amido + gordura).
- KitKat 18/11: +45 (igual a 17/11). Café com pouco açúcar: +4. Café + treino de braço: +26.

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
- Glicose bem regulada: base ~90–97, nenhum valor abaixo de 54 depois da calibração, só 2 picos acima de 180, os dois em jantares com amido + gordura (pastelão + Coca, 194,5; frango + batata frita + baião, 184,5), cada um por ~10 min. Volta à base em 2–3 h na maioria das refeições.
- Proteína/gordura quase não mexem (manhã de 18/11: CV 3%). Feijão sobe pouco. Amido refinado e açúcar sobem rápido; com gordura junto, a curva fica longa e em ondas (pizza, chocotone ~8 h).
- Treino de pernas baixa a glicose (−30); treino de braços sobe um pouco (+17).

## Ponto de atenção médico
- Jejum acima de 100 em dias de rotina low-carb, picos acima de 180 com refeições pequenas, volta à base acima de 3 h, ou rouquidão por mais de 2–3 semanas.

## Perguntas ainda sem resposta
- Quantidade do panetone e da Coca-Cola de 18/11. Tamanho do iogurte integral de 19/11.
