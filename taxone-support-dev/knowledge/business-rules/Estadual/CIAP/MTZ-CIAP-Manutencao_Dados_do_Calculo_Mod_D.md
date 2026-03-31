# MTZ-CIAP-Manutencao_Dados_do_Calculo_Mod_D

- **Fonte:** MTZ-CIAP-Manutencao_Dados_do_Calculo_Mod_D.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 62 KB

---

THOMSON REUTERS

                                                                        __Módulo Ativo Permanente \(CIAP\)__

__ __

__                                           Manutenção dos Dados do Cálculo – Modelo D__

__Localização__: Menu Estadual, Módulo: CIAP, menu Movimento 🡪 Manutenção Dados de Cálculo 🡪 Modelo D 🡪 Fator de Cálculo

__Localização__: Menu Estadual, Módulo: CIAP, menu Movimento 🡪 Manutenção Dados de Cálculo 🡪 Modelo D / Modelo C \(BA, PR\) 🡪 Crédito

*\(a opção da manutenção “por Inscrição Estadual – PIM” não foi citada acima pois ela só trabalha com o livro do Modelo C, já que o AM usa o Modelo C\)*

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS2713

Criação das Regras Específicas por Estabelecimento\.

Alteração na descrição do campo “Fator Mensal” para “Coeficiente das Saídas”\. Esta alteração, *não* tem nenhuma relação com a questão da nova parametrização das regras específicas por Estabelecimento, apenas foi feita na mesma OS\.

 \(ver __RN01__, campo “Coeficiente das Saídas”\)\.

11/01/2016

\(criação do Doc\)

REGRAS DE NEGÓCIO

__RN00__

__Regras gerais__

Os dados gerados no cálculo do CIAP do Modelo C podem ser consultados da seguinte forma:

__No menu “Fator de Cálculo”:__

Neste menu são exibidos os valores totais calculados para o período\.

Tabelas: APT\_EST\_MENS\_ANO

__No menu “Crédito”:__

Neste menu são exibidos os valores calculados para cada Bem\.

Tabelas: APT\_EST\_SAIDA

__RN01__

__Menu “Fator de Cálculo”__  \(valores do resultado do período\)

Campo “__Coeficiente das Saídas__” 🡪 O valor informado neste campo é o coeficiente das saídas usado no cálculo do livro, que é igual ao total saídas tributadas /  total geral das saídas\.

 

Alteração da __MFS2713__: Originalmente este campo se chamava “*Fator Mensal*”\. Foi renomeado para “*Coeficiente das Saídas*” na MFS2713\. O motivo da alteração é o conteúdo da informação demonstrada, que é exatamente o coeficiente das saídas \(total saídas tributadas /  total geral das saídas\)\.

Campo “__Total do Crédito Mensal \(Modelo D\)__” 🡪 Neste campo é exibido o total geral do CIAP, calculado de acordo com as regras do livro Modelo D\. Este total será sempre igual a totalização das parcelas calculadas para todos os Bens\.

Campo “__Total do Crédito Mensal \(EFD – Bloco G\)__” 🡪 Neste campo é exibido o total geral do CIAP, calculado de acordo com as regras do Bloco G\.

Teoricamente, o valor dos campos “*Total Crédito Mensal \(Modelo D\)” *e “*Total do Crédito Mensal \(EFD – Bloco G\)*” seria sempre o mesmo\. No entanto, como o cálculo é feito de forma diferente \(o segundo campo segue as regras do Bloco G da EDF\), poderão ocorrer diferenças devido a questão de arredondamento, principalmente quando se tratar de uma quantidade grande de Bens envolvidos no cálculo\.

__RN02__

__Menu “Demonstrativo das Bases de Crédito__”  \(valores gerados para cada Bem\)

Campo “__Fator Mensal__”__ __🡪 O valor informado neste campo é o resultado do seguinte cálculo:

                                     \[ coeficiente das saídas  / fração utilizada no cálculo \]

 

*\(\*\) total saídas tributadas /  total geral das saídas*

