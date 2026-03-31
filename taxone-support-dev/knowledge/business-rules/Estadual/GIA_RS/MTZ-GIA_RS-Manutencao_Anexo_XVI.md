# MTZ-GIA_RS-Manutencao_Anexo_XVI

- **Fonte:** MTZ-GIA_RS-Manutencao_Anexo_XVI.docx
- **Modificado:** 2021-09-21
- **Tamanho:** 27 KB

---

GIA – RS – Manutenção Anexo XVI – Operações Intermunicipais

Localização: Estadual → GIA RS

Menu: Obrigações → IN DRP45/98 – GIA → Manutenção→ Anexo XVI – Operações Intermunicipais

DOCUMENTO DE REQUISITO

__DR__

__Nome__

__Descrição__

OS3402

Nova tela de manutenção do Anexo XVI

Nova tela de manutenção do Anexo XVI

REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

__Regras Gerais__

Todos os campos de valores terão tamanho de 17, sendo 15 inteiros e 2 decimais\. Cada linha que é apresentada no relatório é um registro da nova tabela\. 

__OS3402__

__RN01__

__Campo: Estabelecimento__

Utilizar para o critério de busca o estabelecimento que o usuário escolheu\.  Trará o estabelecimento que o usuário está logado\. Se o usuário não estiver logado em nenhum, trará a lista de estabelecimentos do Rio Grande do Sul\.

Campo obrigatório\.

Campo chave\.

Este campo não deverá estar bloqueado\.

__ __

__OS3402__

__RN02__

__Campo: Mês/ Ano Apuração__

Utilizar para o critério de busca o mês que o usuário preencheu\.

Campo obrigatório\.

Campo chave\.

Este campo não deverá estar bloqueado\.

__OS3402__

__RN03__

__Campo: UF__

Recuperar o COD\_ESTADO da tabela ESTADO, porém deverá ser fixo o conteúdo “RS”, referente ao Estado do Rio Grande do Sul\.

Campo obrigatório\.

Campo chave\.

__OS3402__

__RN04__

__Campo: Município__

Deverá listar o conteúdo da TACES06 \(COD\_MUNICIPIO \+ DESCRICAO tabela MUNICIPIO\. Recuperar os municípios cujo IDENT\_ESTADO é relativo ao COD\_ESTADO selecionado na lista de UF’s\.

Campo obrigatório\.

Campo chave\.

Este campo não deverá estar bloqueado\.

__OS3402__

__RN05__

__Campo: Natureza da Operação__

Trazer fixo o valor gerado através da __RNX16\-9__ do documento matriz “Matriz \- Estadual \- GIA\-RS \- Geracao Versao 8\.doc 

Campo obrigatório\.

Campo chave\.

Este campo não deverá estar bloqueado\.

__OS3402__

__RN06__

__Campo: Ato Declaratório__

Este campo deverá estar livre para que o usuário digite o conteúdo\.

Campo não obrigatório\.

Campo chave\.

Este campo não deverá estar bloqueado\.

__OS3402__

__RN07__

__Campo: Valor do Serviço__

Trazer fixo o valor gerado através da __RNX16\-14 __do documento matriz “Matriz \- Estadual \- GIA\-RS \- Geracao Versao 8\.doc”\.

Campo não obrigatório\.

Este campo não deverá estar bloqueado\.

__OS3402__

__RN08__

__Campo: Custos__

Este campo deverá estar livre para que o usuário digite o valor\.

Campo não obrigatório\.

Este campo não deverá estar bloqueado\.

__OS3402__

__RN09__

__Campo: Nº Processo__

Trazer o número do processo que gerado pela rotina na geração do Meio Magnético, quando o usuário optar pela geração automática do registro\.

__OS3402__

