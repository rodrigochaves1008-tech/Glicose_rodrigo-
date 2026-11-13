# Glicose Rodrigo

Leitor: **Accu-Chek SmartGuide** (Roche) — sensor de 14 dias no braço. Guia de aplicação: `guias/aplicacao-sensor.html`.

Projeto pessoal para acompanhar a glicose e o dia a dia (alimentação, exercícios, remédios, sono etc.) e cruzar essas informações com os relatórios do leitor de glicose.

## Estrutura

```
diario/                  Um arquivo por dia (AAAA-MM-DD.md) com o que foi feito
relatorios/originais/    Relatórios do leitor exatamente como enviados (PDF, CSV, imagem)
relatorios/resumos/      Resumo de cada relatório (médias, picos, tempo no alvo)
guias/                   Guias práticos (ex.: aplicação do sensor)
ANALISES.md              Observações e padrões encontrados ao longo do tempo
```

## Como funciona

1. **Diário** – a cada áudio/mensagem ("comi X", "caminhei 30 min", "tomei o remédio"), o registro entra em `diario/AAAA-MM-DD.md` com horário.
2. **Relatórios** – cada relatório do leitor é salvo em `relatorios/originais/` e resumido em `relatorios/resumos/`.
3. **Análises** – os relatórios são cruzados com o diário para encontrar padrões (ex.: o que causa picos, efeito de exercícios).

> ⚠️ Este projeto é apenas para organização pessoal e não substitui orientação médica.
