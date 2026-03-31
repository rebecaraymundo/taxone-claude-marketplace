# MTZ-ICMS-MM_Convenio_115-Parte_2

- **Fonte:** MTZ-ICMS-MM_Convenio_115-Parte_2.docx
- **Modificado:** 2023-02-10
- **Tamanho:** 30 KB

---

__ICMS – Convênio 115__

__Localização: Módulo:__ Estadual >> ICMS 

__              Menu:__ DATA MART >> Convênio ICMS 115 >> Geração do Meio Magnético

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__OS2768/ OS3424\-D__

ICMS – convênio 115

As empresas que fornecem energia elétrica, cujo documento de saída é o modelo 06 devem gerar arquivo magnético conforme previsto pelo convênio 115\. 

Porém, a Portaria CAT 79/03 em seu artigo 4, § 2º, diz, que os arquivos serão gerados com a mesma periodicidade de apuração do ICMS do contribuinte, devendo conter a totalidade dos documentos fiscais do período de apuração\.

Já o RICMS/00, no seu artigo 110, diz o seguinte: Na apuração do imposto, relativamente às operações com energia elétrica, considerar\-se\-ão os documentos fiscais que apresentem o __vencimento__ do prazo de pagamento no período de apuração\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Para que o meio magnético do convênio 115 seja gerado corretamente, e para que as regras abaixo sejam aplicadas com sucesso, as notas de saídas de utilities modelo 06, será necessário que o usuário carregue o campo 32 da safx 42 com a data de vencimento dos documentos aqui mencionados\.

__OS2768__

__RN01__

__\[ALTERADA – OS3424\-D\]__ __Regra para geração do Meio Magnético do Convênio 115:__

No momento da geração do meio magnético do convênio 115, o usuário informa no campo “Mês/Ano da Apuração” a data que determinará a busca das notas fiscais para geração do arquivo magnético\. O sistema busca as notas da safx 42 e 43, quando esse, identificar a existência das notas fiscais de saída, cujo modelo for igual a 06, deverá buscar as notas pela data informada no campo 32 da safx 42 \(data de vencimento\)\.

Ao recuperar as notas da SAFX42, aplicar a regra descrita abaixo:

__Campo 13 \- COD\_MODELO \(SAFX42\) = ‘6’, UF Estabelecimento = SP, UF Destinatário = SP__

__SE__ campo 03 \- DAT\_FISCAL \(SAFX42\) tiver data até 31\.12\.2011, a escrituração deve ser pela data de vencimento, ou seja, pelo campo 32 da SAFX42\.

__SE__ campo 03 \- DAT\_FISCAL \(SAFX42\) tiver data a partir de 01\.01\.2012, a escrituração deve ser pela emissão, ou seja pelo campo 03\(SAFX42\)\.

__Obs\.:__ A UF Destinatário deve ser = SP em virtude de negócios, pois o estabelecimento é situado em SP, porém comercializa energia elétrica para outra UF, como por exemplo, as cidades que se localizam em divisas entre estados\.

__Obs\.:__ A regra acima deve ser válida para reprocessamento\.

__OS2768/ OS3424\-D/__

__RN02__

As notas cujo modelo seja diferente de 06 deverão ser buscadas através da data fiscal como já é feito hoje, essa regra não deve ser alterada\.

__OS2768__

__RN03__

O convênio 115 deverá gerar as notas modelo 06, saídas, com base na data de vencimento, somente quando a UF do estabelecimento a qual esta sendo gerado o meio magnético for “SP”\.

__OS2768__

__RN04__

Na tela de geração, estas regras devem valer tanto para a geração de uma série específica quanto para todas as séries\.

__OS2768__

__RN05__

Estas regras devem valer apenas para a geração do Convênio 115, e não para o Convênio 133\.

__OS2768__

__RN06__

No arquivo magnético, embora o filtro seja pela data de vencimento, deverá ser gravada no arquivo a data de emissão do documento fiscal\.

__OS2768__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

