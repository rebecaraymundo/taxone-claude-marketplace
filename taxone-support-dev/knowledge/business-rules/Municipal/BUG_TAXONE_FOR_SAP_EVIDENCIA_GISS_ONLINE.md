# BUG_TAXONE_FOR_SAP_EVIDÊNCIA_GISS_ONLINE

> Fonte: BUG_TAXONE_FOR_SAP_EVIDÊNCIA_GISS_ONLINE.docx



Base
https://uaa-server.hanashow.tax4b.int.thomsonreuters.com:30033/uaa-security-oidc/login
Usuário: AFONSECA

Erro ao gerar a GISS ONLINE no T14SAP


Problema encontrado nos municípios de Rio de Janeiro (RJ), Belo Horizonte (MG) e Vitória (ES)

RJ


{'MANDT_220','EMPRESA_T001','FILIAL_0001','MUNICIPIO_3304557','ANO_2021','PERIODO_06'}

"Id do log: fc64eecc-e06c-4232-aeaa-8c89d477a662\r\rMensagem : Erro no sistema\r\rTrace    : {\n\t\"message\": \"Error while SELECT data SQL error: wrong number or types of parameters in call: P_INDICADOR is not bound: line 31 col 19 (at pos 1130)\",\n\t\"hanaMessage\": \"wrong number or types of parameters in call: P_INDICADOR is not bound: line 31 col 19 (at pos 1130)\",\n\t\"hanaCode\": 1281,\n\t\"hanaSqlState\": \"HY000\",\n\t\"originalCommand\": \"SELECT\\n                    \\\"CD_INDICADOR\\\",\\n                    \\\"NR_LAYOUT\\\",\\n                    \\\"DT_EMISSAO_NF\\\",\\n                    \\\"NR_DOC_NF_INICIAL\\\",\\n                    \\\"NR_DOC_NF_SERIE\\\",\\n                    \\\"TP_DOC_NF\\\",\\n                    \\\"VL_DOC_NF\\\",\\n                    \\\"CD_ATIVIDADE\\\",\\n                    \\\"CD_PREST_TOM_ESTABELECIDO\\\",\\n                    \\\"CD_LOCAL_PRESTACAO\\\",\\n                    \\\"NM_RAZAO_SOCIAL\\\",\\n                    \\\"NR_CNPJ_CPF\\\",\\n                    \\\"CD_TIPO_CADASTRO\\\",\\n                    \\\"NR_INSCRICAO_MUNICIPAL\\\",\\n                    \\\"NM_INSCRICAO_MUNICIPAL_DV\\\",\\n                    \\\"NR_INSCRICAO_ESTADUAL\\\",\\n                    \\\"NM_TIPO_LOGRADOURO\\\",\\n                    \\\"NM_TITULO_LOGRADOURO\\\",\\n                    \\\"NM_LOGRADOURO\\\",\\n                    \\\"NM_COMPL_LOGRADOURO\\\",\\n                    \\\"NR_LOGRADOURO\\\",\\n                    \\\"CD_CEP\\\",\\n                    \\\"NM_BAIRRO\\\",\\n                    \\\"CD_ESTADO\\\",\\n                    \\\"NM_CIDADE\\\",\\n                    \\\"IC_ORIGEM_DADOS\\\",\\n                    \\\"VL_ALIQUOTA\\\",\\n                    \\\"FL_ISENTO\\\",\\n                    \\\"FL_SIMPLES\\\"\\n            FROM  \\\"tax4b.giss::TF_ARQUIVO_21EDITION\\\"(\\n                    '220',\\n                    'T001',\\n                    '0003',\\n                    '3304557',\\n                    '20210601',\\n                    '20210630'\\n               )\",\n\t\"progressCount\": 1\n}\r\r{\n\t\"MANDT\": \"220\",\n\t\"EMPRESA\": \"T001\",\n\t\"COD_MUN\": \"3304557\",\n\t\"DT_PER\": \"06\",\n\t\"DT_ANO\": \"2021\",\n\t\"INDICADOR\": {},\n\t\"LAYOUT\": \"\",\n\t\"FILIAIS\": [\n\t\t{\n\t\t\t\"ID\": 1000083,\n\t\t\t\"filial\": \"0003\"\n\t\t}\n\t],\n\t\"USUARIO_GERACAO\": \"AFONSECA\",\n\t\"EDICOES\": [\n\t\t\"21\"\n\t],\n\t\"FILIAL\": \"0003\",\n\t\"ID\": 1000083,\n\t\"layoutEdition\": \"21\"\n}"


BH

{'MANDT_220','EMPRESA_T001','FILIAL_0001','MUNICIPIO_3106200','ANO_2021','PERIODO_06'}

"Id do log: f138ca60-4a24-4a54-adef-f5a2c805d5c8\r\rMensagem : Erro no sistema\r\rTrace    : {\n\t\"message\": \"Error while SELECT data SQL error: wrong number or types of parameters in call: P_INDICADOR is not bound: line 31 col 19 (at pos 1130)\",\n\t\"hanaMessage\": \"wrong number or types of parameters in call: P_INDICADOR is not bound: line 31 col 19 (at pos 1130)\",\n\t\"hanaCode\": 1281,\n\t\"hanaSqlState\": \"HY000\",\n\t\"originalCommand\": \"SELECT\\n                    \\\"CD_INDICADOR\\\",\\n                    \\\"NR_LAYOUT\\\",\\n                    \\\"DT_EMISSAO_NF\\\",\\n                    \\\"NR_DOC_NF_INICIAL\\\",\\n                    \\\"NR_DOC_NF_SERIE\\\",\\n                    \\\"TP_DOC_NF\\\",\\n                    \\\"VL_DOC_NF\\\",\\n                    \\\"CD_ATIVIDADE\\\",\\n                    \\\"CD_PREST_TOM_ESTABELECIDO\\\",\\n                    \\\"CD_LOCAL_PRESTACAO\\\",\\n                    \\\"NM_RAZAO_SOCIAL\\\",\\n                    \\\"NR_CNPJ_CPF\\\",\\n                    \\\"CD_TIPO_CADASTRO\\\",\\n                    \\\"NR_INSCRICAO_MUNICIPAL\\\",\\n                    \\\"NM_INSCRICAO_MUNICIPAL_DV\\\",\\n                    \\\"NR_INSCRICAO_ESTADUAL\\\",\\n                    \\\"NM_TIPO_LOGRADOURO\\\",\\n                    \\\"NM_TITULO_LOGRADOURO\\\",\\n                    \\\"NM_LOGRADOURO\\\",\\n                    \\\"NM_COMPL_LOGRADOURO\\\",\\n                    \\\"NR_LOGRADOURO\\\",\\n                    \\\"CD_CEP\\\",\\n                    \\\"NM_BAIRRO\\\",\\n                    \\\"CD_ESTADO\\\",\\n                    \\\"NM_CIDADE\\\",\\n                    \\\"IC_ORIGEM_DADOS\\\",\\n                    \\\"VL_ALIQUOTA\\\",\\n                    \\\"FL_ISENTO\\\",\\n                    \\\"FL_SIMPLES\\\"\\n            FROM  \\\"tax4b.giss::TF_ARQUIVO_21EDITION\\\"(\\n                    '220',\\n                    'T001',\\n                    '0005',\\n                    '3106200',\\n                    '20210601',\\n                    '20210630'\\n               )\",\n\t\"progressCount\": 1\n}\r\r{\n\t\"MANDT\": \"220\",\n\t\"EMPRESA\": \"T001\",\n\t\"COD_MUN\": \"3106200\",\n\t\"DT_PER\": \"06\",\n\t\"DT_ANO\": \"2021\",\n\t\"INDICADOR\": {},\n\t\"LAYOUT\": \"\",\n\t\"FILIAIS\": [\n\t\t{\n\t\t\t\"ID\": 1000081,\n\t\t\t\"filial\": \"0005\"\n\t\t}\n\t],\n\t\"USUARIO_GERACAO\": \"AFONSECA\",\n\t\"EDICOES\": [\n\t\t\"21\"\n\t],\n\t\"FILIAL\": \"0005\",\n\t\"ID\": 1000081,\n\t\"layoutEdition\": \"21\"\n}"

Pelo Treinamento assistido, o campo Indicador (que é de preenchimento obrigatório) não está sendo apresentado na tela.


