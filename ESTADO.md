# Estado atual do projeto (atualizado em 18/11/2026 ~17:30)

Leia este arquivo + `CLAUDE.md`, `PERFIL.md`, `TESTES.md` e `ANALISES.md` para retomar o trabalho.

## Sensor
- Accu-Chek SmartGuide no **braço direito**, aplicado em 13/11 ~14:55. **Troca prevista em 27/11** (próximo no braço esquerdo, ter glicosímetro em casa).
- Calibrado em 14/11: 16:08 (dedo 99 × sensor 80) e 16:43 (dedo 92 × sensor 75,5). Leituras antes das 16:43 de 14/11 marcam ~15–20 abaixo do real.
- Adesivo soltando na borda desde 16/11: orientado a usar esparadrapo ou filme (Tegaderm), **nunca cola**.
- Alerta de baixa no app: 60. Alerta de alta: 180.

## Como processar uma exportação (Exportar.zip)
1. Descompactar numa pasta nova no scratchpad.
2. `python3 -I scripts/processar_export.py <pasta>/dataPoints.jsonl relatorios/originais/AAAA-MM-DD_export_cgm.csv "inicio" "fim"`
3. Escrever o resumo em `relatorios/resumos/`, atualizar `ANALISES.md`, a tabela de resultados de `TESTES.md` e o diário. Fazer commit e push.
- Última exportação processada: **18/11 17:19** (`relatorios/originais/2026-11-18_export_cgm.csv`).

## Plano
- **Fase 1 (até 21/11): testes com carboidrato.** Ainda faltam: A1 arroz, A2 arroz + feijão, A3 banana, A4 pão francês, A5 pão + ovos, A6 ordem dos alimentos, C1 caminhada após comer, C3 academia após o pão, T3 pastelão sozinho, A7 Coca sozinha (com quantidade), repetir a tapioca (T1).
- **Fase 2 (22–26/11): low-carb sem interrupção, sem jantar.** Linha de base: verificar se as madrugadas voltam a ~70–85, se o jejum fica abaixo de 100 e se a fome e a vontade de doce somem.

## Pendências e perguntas abertas
- Quantidade do panetone (18/11 12:11) e da Coca-Cola (18/11 15:49): não informadas.
- Curva do KitKat de 18/11 16:58: aparece na próxima exportação. Comparar com o KitKat de 17/11 (95 → 138).
- Teoria do Rodrigo (saída da cetose): madrugadas 75 → 92 → 113 → **90** (previsão 1 confirmada). Faltam as previsões 2 (picos menores com os dias) e 3 (madrugada mais baixa na fase low-carb).
- Ponto de atenção médico: jejum acima de 100 em dias de rotina low-carb, picos acima de 180 com refeições pequenas ou volta à base acima de 3 h.

## Principais conclusões até agora
- Glicose bem regulada: base ~90–97, nenhum valor abaixo de 54 depois da calibração, só 1 pico acima de 180 (pastelão + Coca, 194,5).
- Proteína/gordura quase não mexem. Feijão sobe pouco. Amido refinado/açúcar sobem rápido; com gordura junto, a curva fica longa e em ondas (pizza, chocotone).
- Treino de pernas baixa a glicose (−30); treino de braços sobe um pouco (+17).
