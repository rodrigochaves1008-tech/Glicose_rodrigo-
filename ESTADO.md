# Estado atual do projeto

> **23/11: o Rodrigo decidiu NÃO usar outro sensor.** A fase de coleta acabou. Entregue o guia final `guias/guia_alimentar_rodrigo.pdf` (gerado por `scripts/graficos_guia.py` + `scripts/gerar_guia_pdf.py`). Daqui em diante: dúvidas sobre alimentação/hábitos usando os dados já coletados. (atualizado em 23/11/2026)

Ao retomar, leia este arquivo e depois `CLAUDE.md`, `PERFIL.md`, `TESTES.md` e `ANALISES.md`, se precisar de detalhes.

## Rodrigo (resumo do perfil)
- Sem diabetes, sem remédios. Rotina: low-carb/cetogênica, refeições cedo, **sem jantar**. Acorda ~04h e treina cedo.
- **Os horários que ele informa são exatos.** Ele registra refeições, bebidas, treinos (superiores × inferiores) e sintomas na hora.

## Sensor
- **Sensor 1 (braço direito, aplicado em 13/11 ~14:55) ENCERRADO COM FALHA em 23/11 04:11** ("SessionEndedFault"). Instável desde 22/11 ~18:35; leituras provavelmente baixas desde a tarde de 21/11. **Bateria OK até o fim.** ~20 alarmes falsos de hipo urgente na noite de 22/11.
- Alertas no app: baixa 60, alta 180.

## Como processar uma exportação (Exportar.zip)
1. Descompactar numa pasta nova no scratchpad.
2. `python3 -I scripts/processar_export.py <pasta>/dataPoints.jsonl relatorios/originais/AAAA-MM-DD_export_cgm.csv "AAAA-MM-DD HH:MM" "AAAA-MM-DD HH:MM"`
3. Escrever o resumo em `relatorios/resumos/`, atualizar `ANALISES.md`, `TESTES.md` (resultados), o diário e este arquivo. Fazer commit e push.
- **Última exportação processada: final do sensor 1 (23/11 04:08)** (`relatorios/originais/2026-11-23_export_cgm.csv`, resumo `relatorios/resumos/2026-11-21_almoco_a_2026-11-23_fim_do_sensor.md`).
- O script ignora leituras NaN/±Infinity (sem valor ou fora da escala).

## Plano
- **Fase 1 (13–18/11), testes com carboidrato: ENCERRADA.** Ficaram para o próximo sensor: A1 arroz, A2 arroz + feijão, A3 banana, A4 pão francês, A5 pão + ovos, A6 ordem dos alimentos, C1 caminhada após comer, C3 academia após o pão, T3 pastelão sozinho, A7 Coca sozinha (com quantidade), repetir a tapioca.
- **Fase 2 (19–22/11), low-carb: interrompida** (carboidrato em 20, 21 e 22/11) e **encerrada pela falha do sensor em 23/11**. 19/11 = dia 1.
  - 20/11: fava com toucinho em **porção grande** no almoço (~40–60 g de carboidrato).
  - 20/11 ~20:15: **jantar com carboidrato** (frango, batata frita, baião), fora do plano → pico 184,5. Madrugada de 21/11 não conta como low-carb; cetose provavelmente ~25–26/11.
  - 21/11: mungunzá com queijo e nata. 22/11: café com açúcar + bolo, bolo/cuscuz várias vezes, baião com carne.

## Testes que ficaram sem fazer (não haverá novo sensor)
- Testes que faltaram: A1 arroz, A2 arroz + feijão, A3 banana, A4 pão francês, A5 pão + ovos, A6 ordem dos alimentos, C1 caminhada após comer, C3 academia após o pão, T3 pastelão sozinho, A7 Coca sozinha (com quantidade), repetir a tapioca, **repetir o mungunzá com e sem queijo/nata**, **baião com e sem batata frita no mesmo horário**.
- Fase low-carb sem interrupção (madrugadas e volta à cetose): ainda não medida até o fim.
- Sem internet: anotar os horários no celular e mandar depois.

## Resultados (exportações de 20, 21 e 23/11)
- Fase 2 sem os jantares: 100% em 70–140. Madrugadas 96 → 86 (19–20/11) → 102 depois do jantar com batata frita.
- Fava porção grande 128,5; jantar frango + batata frita + baião **184,5**; baião sem batata frita (almoço) +59; bolo + café com açúcar +54; café com pouco açúcar +4; mungunzá com queijo/nata +16 (pouco confiável).
- Balanço do sensor 1 em `ANALISES.md`.

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
