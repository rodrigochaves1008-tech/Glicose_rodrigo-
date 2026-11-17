# Plano de testes: sensor de 13/11 a ~27/11

Objetivo: aproveitar o sensor para entender como cada fator mexe na glicose, **mudando uma coisa por vez**.

## Regras de cada teste
1. **Comece com a glicose estável**: pelo menos 3 h sem comer e seta reta (→) no app.
2. **Coma só o alimento do teste**, sem outra comida nem bebida com caloria até 3 h depois. Água, café puro e chá sem açúcar estão liberados.
3. **Não faça exercício** nas 3 h seguintes, a não ser que o exercício seja o teste.
4. **Anote o horário de início** e mande para o Claude. O resto sai da exportação.
5. Para comparar dois testes, use **a mesma quantidade e o mesmo horário do dia**.
6. Se sentir mal-estar, tontura ou suor frio, interrompa e coma normalmente.

## Dias de rotina (linha de base)
| # | Teste | Como fazer | O que responde |
|---|-------|------------|----------------|
| B1 | Dia normal 1 | Rotina habitual (low-carb, sem jantar), sem testes | Como é a glicose no dia a dia, principalmente tarde e noite sem jantar |
| B2 | Dia normal 2 | Igual, em outro dia | Confirma se o B1 se repete |
| B3 | Noite sem jantar | Dormir depois de um dia de rotina, sem jantar (ele já dorme sem apoiar o braço do sensor) | As baixas de madrugada (60–70) vêm do rebote do jantar de teste ou acontecem também na rotina? |

## Testes de alimentos (de manhã, em jejum)
| # | Teste | Porção sugerida | O que responde |
|---|-------|-----------------|----------------|
| A1 | Arroz branco sozinho | 1 xícara cozida (~150 g) | Amido "puro" do dia a dia |
| A2 | Arroz + feijão | ½ xícara de arroz + ½ de feijão | O feijão segura o arroz? |
| A3 | Fruta sozinha (banana) | 1 banana média | Açúcar natural com fibra |
| A4 | Pão francês sozinho | 1 pão (50 g) | Farinha refinada (base para pizza e massas) |
| A5 | Pão com manteiga e ovos | 1 pão + manteiga + 2 ovos | A gordura e a proteína baixam o pico do pão (comparar com A4)? |
| A6 | Ordem dos alimentos | Mesma refeição do A5, mas comer **ovos primeiro e pão por último**, com 10 min de intervalo | Comer a proteína antes reduz o pico? |
| A7 | Refrigerante comum | 1 lata (350 ml) | Açúcar líquido (o pior caso). **Opcional** |

## Testes de comportamento
| # | Teste | Como fazer | O que responde |
|---|-------|------------|----------------|
| C1 | Caminhada depois de comer | Repetir o A1 ou o A4 e caminhar 15 min logo depois | Quanto uma caminhada curta reduz o pico |
| C2 | Academia em jejum | Treino normal de manhã, antes do café | Como o treino de força mexe na glicose (subida? queda depois?) |
| C3 | Academia depois de comer carboidrato | Treinar ~1 h depois do A4 (pão) | O treino "gasta" o pico? |
| C4 | Repetir o teste com o pior pico | Repetir o teste com o maior pico (provavelmente A1 ou A7) | O resultado se repete? (confiabilidade) |

## Testes extras (fora do plano)
| # | Teste | Porção | O que responde |
|---|-------|--------|----------------|
| T1 | Tapioca com queijo (16/11 07:26) | 2 tapiocas | Amido de mandioca sem fibra. Comparar com a maizena (pico 168 + rebote) |
| T2 | Pastelão com recheio misto + um pouco de Coca-Cola (16/11 20:32) | não medida | Massa de farinha refinada + gordura + açúcar líquido, à noite. Comparar com pizza + sorvete |

## Calendário (revisado em 16/11)
Decisão do Rodrigo: **primeiro os testes com carboidrato, depois low-carb sem interrupção até o fim do sensor.**
Para caber tudo, até **2 testes por dia**: um de manhã e outro à tarde, com **pelo menos 4 h de intervalo** e a glicose estável antes do segundo.

### Fase 1: testes com carboidrato (17 a 21/11)
| Data | Manhã | Tarde |
|------|-------|-------|
| 16/11 | T1 tapioca (feito) | T2 pastelão à noite (20:32, extra) |
| 17/11 | A1 arroz sozinho | A3 banana |
| 18/11 | A2 arroz + feijão | A4 pão sozinho |
| 19/11 | A5 pão com manteiga e ovos | C1 pão sozinho + caminhada de 15 min |
| 20/11 | A6 ordem (ovos antes, pão depois) | C3 academia ~1 h depois do pão |
| 21/11 | C4 repetir o teste com o pior pico | A7 refrigerante (opcional) |

### Fase 2: low-carb sem interrupção (22 a 26/11)
| Data | O que observar |
|------|----------------|
| 22–23/11 | Readaptação: fome, energia e glicose voltando ao padrão low-carb (as cetonas levam ~2–4 dias para voltar) |
| 24/11 | C2 academia em jejum (compatível com low-carb) |
| 22–26/11 | B1/B2/B3: dias e **noites sem jantar** de rotina. É a linha de base "limpa" |
| 27/11 | Troca do sensor (braço esquerdo, com glicosímetro em casa para calibrar) |

A ordem dentro de cada fase pode mudar. Anote sempre o horário de início.

## Resultados
| # | Data | Antes | Pico | Tempo até o pico | Volta à base | Rebote | Observação |
|---|------|-------|------|------------------|--------------|--------|------------|
| T1 tapioca c/ queijo | 16/11 07:26 | 92 | **144** | ~1h | não voltou a 90 em 3h (platô 104–121) | não | Abaixo da maizena (168). Queijo prolonga o platô |
| (pré-plano) maizena c/ queijo/manteiga | 14/11 17:38 | 82 | 168 | 40 min | ~2h35 | **sim, 68** | jantar |
| (pré-plano) sopa de feijão | 15/11 11:25 | 88 | 127 | 1h30 | ~2h | não | |
| (pré-plano) sorvete grande + pizza | 15/11 17:47 / 18:52 | 87 | 172 | 1h | ~6h oscilando (3 ondas) | sim, 70 | |
