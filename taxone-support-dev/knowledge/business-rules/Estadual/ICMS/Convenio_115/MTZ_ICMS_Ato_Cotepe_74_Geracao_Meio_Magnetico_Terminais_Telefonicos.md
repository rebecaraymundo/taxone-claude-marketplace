# MTZ_ICMS_Ato_Cotepe_74_Geracao_Meio_Magnetico_Terminais_Telefonicos

- **Fonte:** MTZ_ICMS_Ato_Cotepe_74_Geracao_Meio_Magnetico_Terminais_Telefonicos.docx
- **Modificado:** 2024-09-02
- **Tamanho:** 70 KB

---

THOMSON REUTERS

Geração Arquivo Magnético  
Ato COTEPE/ICMS 74/2017 – Terminais Telefônicos

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-15387

Julyana Perrucini

Este documento tem como objetivo incluir a geração do arquivo magnético auxiliar em atendimento ao Ato COTEPE/ICMS 74/2017 referentes aos terminais telefônicos dos planos de prestações de serviços telefônicos corporativos, familiares ou similares, em substituição à sistemática estabelecida no subitem 5\.2\.5\.2\. do Anexo Único do Convênio ICMS 115/03, de 12 de dezembro de 2003\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN00

__Regras Gerais__

A geração de o arquivo magnético auxiliar referentes aos terminais telefônicos dos planos de prestações de serviços telefônicos corporativos, familiares ou similares foi criada pela MFS\-15387 em substituição à sistemática estabelecida no subitem 5\.2\.5\.2\. do Anexo Único do Convênio ICMS 115/03, de 12 de dezembro de 2003\.

Esse arquivo somente será gerado quando o campo Ato COTEPE/ICMS 74 no item “Gerar Arquivo Auxiliar” estiver marcado na tela de Geração dos Arquivos Magnéticos para o Convênio 115, do módulo ICMS\.

MFS\-15387

RN01

__Dados Técnicos da Geração dos Arquivos__

__*Formato do Arquivo:*__

- Formatação: compatível com MS\-DOS;
- Tamanho do arquivo: 189 bytes, acrescidos de CR/LF \(Carriage Return/Line Feed\) ao final de cada registro;
- Organização: sequencial;
- Codificação: ASCII\.

MFS\-15387

RN02

__Regra para Identificação do Arquivo__

Se o__ __item “Gerar Arquivo Auxiliar” da tela de Geração dos Arquivos Magnéticos para o Convênio 115 do módulo ICMS estiver marcado com a opção igual a Ato COTEPE/ICMS 74, os arquivos serão identificados no formato:

__UUCCCCCCCCCCCCCCMMSSSANOMMSnnT__

- __UU:__ UF – preencher com sigla da unidade federada do emitente dos documentos fiscais;
- __CCCCCCCCCCCCCC: __CNPJ – preencher com o CNPJ do contribuinte emitente dos documentos fiscais;
- __MM: __Modelo – preencher com o modelo dos documentos fiscais;
- __SSS: __Série – preencher com a série dos documentos fiscais;
- __ANO: __Ano – preencher com o ano de emissão dos documentos fiscais;
- __MM: __Mês – preencher com o mês do período de apuração dos documentos fiscais;
- __Snn: __Status – indica se o arquivo é normal \(N\) ou substituto \(S\)\. Preencher com “01” quando o campo Status estiver com a opção Normal marcada na tela de geração do arquivo magnético ou preencher com o conteúdo informado no campo Sequencial quando for arquivo substituto, campo Status com a opção Substituta marcada na tela de                                      geração do arquivo magnético;
- __T: __Tipo – deverá ser preenchido com a letra “T” de terminal\.

A quebra do arquivo magnético seguirá com a mesma regra aplicada para o Convênio 60, em que é demonstrada por estabelecimento e Modelo do Documento\. Neste contexto, não se aplica a “Geração para Empresas c/ Inscrição Estadual Única”, uma vez que será gerado um arquivo para cada estabelecimento\. Podemos ter o cenário de seleção do campo “Modelo de Documento para geração” a opção “Todos”\. Se isso ocorrer, deverá ser gerado um arquivo para cada estabelecimento e modelo\. Sempre ocorrerá a quebra do arquivo considerando os campos que compõe a nomenclatura do mesmo\.

MFS\-15387

RN03

__Regra p/ Recuperação dos Dados__

__*Origem das Informações para geração:*__

- Tela de Empresa/Estabelecimento do módulo Básicos – Parâmetros \(tabela estabelecimento\), localizado no item de menu: Preliminares >> Empresa/Estabelecimento;
- Tela de Inscrições Estaduais do módulo Básicos – Parâmetros \(tabela registro\_estadual\), localizado no item de menu: Preliminares >> Inscrições Estaduais;
- SAFX42 – Tela de Documento Fiscal Utilities do módulo Básicos – MasterSAF DW, localizado no item de menu: Manutenção >> Documento Fiscal >> Novo Documento Fiscal >> Documento Fiscal Utilities;
- SAFX253 – Botão Terminais Telefônicos da tela de Documento Fiscal Utilities do módulo Básicos – MasterSAF DW, localizado no item de menu: Manutenção >> Documento Fiscal >> Novo Documento Fiscal >> Documento Fiscal Utilities;

__*Regra de seleção geral: *__

Selecionar os registros processados das tabelas dadas como origem, com os seguintes filtros:

- Código da Empresa = Código da Empresa \(relacionado ao Estabelecimento selecionado na tela de geração\);
- Código do Estabelecimento = Código do Estabelecimento selecionado na tela de geração;
- Data fiscal enquadrada no mês e ano da apuração informada na tela de geração \(campo 03\-DAT\_FISCAL da SAFX42\);
- Modelo do documento fiscal igual a “06”, “21” ou “22” \(campo 13\-COD\_MODELO da SAFX42\);
- Indicador de atendimento ao Convênio 115 do documento fiscal igual a “S” \(campo 61\-IND\_CONVENIO\_115 da SAFX42\);
- Nº do terminal Principal diferente de nulo/branco \(campo 115\-NUM\_TERMINAL\_TEL\)\.

__*Regra de gravação geral:* __Verificar documento de DExPARA DEPARA\_Ato\_Cotepe\_74\_Terminais\_Telefonicos\.xls para obtenção dos resultados, as regras contidas a seguir são campos que necessitam de tratamento e mensagem de log\.

__*Regra de agrupamento:* __Não se aplica\.

__*Ordenação:* __Não se aplica\.

__*Considerações:*__ A ideia desse arquivo auxiliar é demonstrar cada terminal telefônico vinculado a um terminal telefônico principal, então deve ser considerado que a mesma NF irá se repetir no arquivo quando existir “N” terminais vinculados \(SAFX253\)\. Com essa alteração a apresentação do campo “26\-Número do terminal telefônico principal” do arquivo tipo Mestre do Documento Fiscal do Convênio 115 passa a ser gerado com brancos\.

MFS\-15387

RNTT\-03

__Campo 03\-IE__

__Tratamento:__

- Se o campo 08\-INSC\_ESTADUAL da SAFX04 não estiver preenchido, emitir a seguinte mensagem de log: “O campo de IE não foi preenchido, favor verificar\! <<NF>>, <<Série>>, <<Data de Emissão>>, <<Modelo>>, <<PFJ>>\.”\.

MFS\-15387

RNTT\-05

__Campo 05\-UF__

__Tratamento:__

- Se o campo 19\-UF da SAFX04 não estiver preenchido, emitir a seguinte mensagem de log: “O campo da UF não foi preenchido, favor verificar\! <<NF>>, <<Série>>, <<Data de Emissão>>, <<Modelo>>, <<PFJ>>\.”\.

MFS\-15387

RNTT\-07

__Campo 07\-MODELO NF__

__Tratamento:__

- Se o campo 13\-COD\_MODELO da SAFX42 não estiver preenchido, emitir a seguinte mensagem de log: “O campo do Modelo da nota fiscal não foi preenchido, favor verificar\! <<NF>>, <<Série>>, <<Data de Emissão>>, <<Modelo>>, <<PFJ>>\.”\.

MFS\-15387

RNTT\-08

__Campo 08\-SÉRIE__

__Tratamento:__

- Esse campo deve ser preenchido a partir da esquerda\. *Exemplo:* “A  “;
- Se o campo 07\-SERIE\_DOCFIS da SAFX42 não estiver preenchido, emitir a seguinte mensagem de log: “O campo da Série da nota fiscal não foi preenchido, favor verificar\! <<NF>>, <<Série>>, <<Data de Emissão>>, <<Modelo>>, <<PFJ>>\.”\.

MFS\-15387

RNTT\-09

__Campo 09\-NÚMERO NF__

__Tratamento:__

- Esse campo deverá ser alinhado à direita com as posições não significativas preenchidas com zeros\.

MFS\-15387

RNTT\-10

__Campo 10\-CODIGO DE AUTENTICAÇÃO DIGITAL DOCUMENTO FISCAL__

__Tratamento:__

- Se o campo 48\-COD\_AUTENTIC da SAFX42 não estiver preenchido, emitir a seguinte mensagem de log: “O campo do Código de Autenticação da nota fiscal não foi preenchido, favor verificar\! <<NF>>, <<Série>>, <<Data de Emissão>>, <<Modelo>>, <<PFJ>>\.”\.

MFS\-15387

RNTT\-11

__Campo 11\-NÚMERO OU CÓDIGO DA FATURA COMERCIAL__

__Tratamento:__

- Se o campo 116\-NUM\_FAT\_COM da SAFX42 não estiver preenchido, emitir a seguinte mensagem de log: “O campo do Número da Fatura Comercial da nota fiscal não foi preenchido, favor verificar\! <<NF>>, <<Série>>, <<Data de Emissão>>, <<Modelo>>, <<PFJ>>\.”\.

MFS\-15387

RNTT\-13

__Campo 13\-NÚMERO DO TERMINAL TELEFÔNICO__

__Tratamento:__

- Se houver ausência da SAFX253 para notas fiscais \(com terminal telefônico principal\) recuperadas, desconsiderar o registro na geração do arquivo magnético e emitir a seguinte mensagem de log: “Não existem terminais telefônicos para alguns documentos fiscais e os mesmos serão desconsiderados da geração do arquivo, favor verificar\! <<NF>>, <<Série>>, <<Data de Emissão>>, <<Modelo>>, <<PFJ>>\.”\.

MFS\-15387

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN

