# MTZ-DW-Manutencao_SAFX15

- **Fonte:** MTZ-DW-Manutencao_SAFX15.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 29 KB

---

    

__Módulo DW – Manutenção – Tabela de Cadastro de Empregados \(SAFX15\)__

Localização: 

Menu Básicos,  Módulo: DW, item de menu  “Manutenção 🡪 Cadastros 🡪 Controle de Funcionário > Funcionário”

* *

*\(Obs: As regras descritas neste documento são numeradas de acordo com os campos  da SAFX15, conforme o Manual de Layout,  o que facilita a consulta\. Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como  RN00\)*

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS4761

 MasterSAF DW > Manutenção > Cadastros > Controle de Funcionário > Tela de Funcionário\.

Alteração no tamanho do campo Carteira Profissional da tela de funcionários \(SAFX15\)\. Deverá aceitar até 11 caracteres\.

17/06/2015

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN00__

__Regras gerais__

__RN18__

__Campo 18 – Carteira Profissional__:

O campo CART\_PROF deve ser atualizado, tendo o seu tamanho alterado para  aceitar até 11 caracteres\.

__Características do campo__

Tamanho: 11

Tipo: N 

Edita: Sim

Obrigatório: Não 

__OS4671__

