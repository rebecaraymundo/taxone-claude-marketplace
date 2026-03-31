# SPED Fiscal - Documentação Visual (TAX ONE)

## 1. Visão Geral - Submódulos do SPED

```mermaid
graph TB
    SPED["<b>SPED - Sistema Público de Escrituração Digital</b>"]

    SPED --> ECD["<b>ECD</b><br>Escrituração Contábil Digital<br><i>SPED Contábil</i><br>37 tabelas (SPED_*)"]
    SPED --> EFD["<b>EFD ICMS/IPI</b><br>Escrituração Fiscal Digital<br><i>SPED Fiscal</i><br>73 tabelas (EFD_*)"]
    SPED --> EPC["<b>EFD Contribuições</b><br>PIS/COFINS/INSS<br><i>SPED PIS/COFINS</i><br>88 tabelas (EPC_*)"]
    SPED --> ECF["<b>ECF</b><br>Escrituração Contábil Fiscal<br>7 tabelas (ECF_*)"]
    SPED --> REINF["<b>EFD-Reinf</b><br>Retenções e Informações<br><i>Contribuições Previdenciárias</i>"]

    EFD --> CIAP["<b>CIAP</b><br>Controle de Crédito<br>do Ativo Permanente<br>35 tabelas (APT_*)"]
    EFD --> COTEPE["<b>COTEPE</b><br>Administração Tributária<br>Estadual<br>20 tabelas"]

    style SPED fill:#1a5276,color:#fff,stroke:#fff
    style ECD fill:#2e86c1,color:#fff
    style EFD fill:#2e86c1,color:#fff
    style EPC fill:#2e86c1,color:#fff
    style ECF fill:#2e86c1,color:#fff
    style REINF fill:#2e86c1,color:#fff
    style CIAP fill:#5dade2,color:#fff
    style COTEPE fill:#5dade2,color:#fff
```

---

## 2. Fluxo Principal - EFD ICMS/IPI (SPED Fiscal)

```mermaid
flowchart LR
    subgraph ENTRADA ["1. ENTRADA DE DADOS"]
        direction TB
        NF["Notas Fiscais<br>(X07/SAFX07)"]
        CF["Cupons Fiscais<br>(ECF)"]
        CT["Conhecimentos<br>Transporte (X46)"]
        ENERGY["Energia/Telecom<br>(X08)"]
    end

    subgraph DWT ["2. DATA WAREHOUSE FISCAL"]
        direction TB
        DWT_DOC["DWT_DOCTO_FISCAL<br>(355 colunas)"]
        DWT_ITEM["DWT_ITEM_DOCTO_FISCAL"]
        DWT_IMP["DWT_IMPOSTO_DOCTO_FISCAL"]
    end

    subgraph CONFIG ["3. CONFIGURAÇÃO"]
        direction TB
        EFD_INI["EFD_DADOS_INICIAIS_ESTAB<br>Dados do Estabelecimento"]
        EFD_CAD["EFD_CAD_*<br>Cadastros (Produtos,<br>Participantes, Contas)"]
        EFD_AJUST["EFD_AJUSTES_AUTO_REGRAS<br>Regras de Ajuste<br>Automático"]
    end

    subgraph PROCESSAMENTO ["4. PROCESSAMENTO (PL/SQL)"]
        direction TB
        FPROC["EFD_SPED_FPROC<br><i>Orquestrador Principal</i>"]
        EFD71["EFD71_GERA<br>Bloco E/G Init"]
        EFD72["EFD72_GERA<br>Ajustes Bloco E"]
        EFD73["EFD73_GERA<br>Bloco E Detalhes"]
        EFD79["EFD79_GERA<br>Bloco H Inventário"]
        EFD82["EFD82_GERA<br>Bloco K Produção"]
        EFD88["EFD88_GERA<br>Bloco 1 Complementar"]
        FPROC --> EFD71 --> EFD72 --> EFD73
        FPROC --> EFD79
        FPROC --> EFD82
        FPROC --> EFD88
    end

    subgraph SAIDA ["5. SAÍDA - BLOCOS DO ARQUIVO"]
        direction TB
        B0["<b>Bloco 0</b><br>Abertura e<br>Cadastros"]
        BC["<b>Bloco C</b><br>Documentos Fiscais<br>Mercadorias"]
        BD["<b>Bloco D</b><br>Documentos Fiscais<br>Serviços"]
        BE["<b>Bloco E</b><br>Apuração ICMS/IPI"]
        BG["<b>Bloco G</b><br>CIAP"]
        BH["<b>Bloco H</b><br>Inventário Físico"]
        BK["<b>Bloco K</b><br>Controle Produção"]
        B1["<b>Bloco 1</b><br>Informações<br>Complementares"]
        B9["<b>Bloco 9</b><br>Encerramento"]
    end

    ENTRADA --> DWT
    DWT --> PROCESSAMENTO
    CONFIG --> PROCESSAMENTO
    PROCESSAMENTO --> SAIDA

    style ENTRADA fill:#f9e79f,stroke:#f1c40f
    style DWT fill:#fadbd8,stroke:#e74c3c
    style CONFIG fill:#d5f5e3,stroke:#27ae60
    style PROCESSAMENTO fill:#d6eaf8,stroke:#2e86c1
    style SAIDA fill:#e8daef,stroke:#8e44ad
```

---

## 3. Fluxo Principal - EFD Contribuições (PIS/COFINS)

```mermaid
flowchart LR
    subgraph ENTRADA ["1. ENTRADA"]
        direction TB
        NF2["Notas Fiscais<br>(DWT_DOCTO_FISCAL)"]
        SERV["Serviços Prestados<br>/Tomados"]
        REC["Receitas Financeiras<br>e Outras"]
    end

    subgraph CONFIG2 ["2. CONFIGURAÇÃO"]
        direction TB
        EPC_INI["EPC_DADOS_INICIAIS_*<br>Estab/Financ/PisCof"]
        EPC_CAD["EPC_CAD_*<br>Cadastros"]
        EPC_DIC["EPC_DICIONARIO<br>(53 refs)<br>Mapeamento de Dados"]
    end

    subgraph PROC2 ["3. PROCESSAMENTO"]
        direction TB
        EPC_FPROC["EPC_SPED_FPROC<br><i>Geração Principal</i>"]
        EPC_SCP["EPC_SPED_SCP_FPROC<br><i>Sociedade em Conta<br>de Participação</i>"]
    end

    subgraph APURACAO ["4. APURAÇÃO"]
        direction TB
        EPC_APUR["EPC_APURACAO<br>Apuração PIS/COFINS"]
        EPC_CRED["EPC_APUR_CRED_DISP<br>Créditos Disponíveis"]
        EPC_RET["EPC_APUR_RET_DISP<br>Retenções"]
        EPC_AJUST["EPC_AJUSTE_APUR<br>Ajustes"]
    end

    subgraph SAIDA2 ["5. BLOCOS DO ARQUIVO"]
        direction TB
        S0["<b>Bloco 0</b> Abertura"]
        SA["<b>Bloco A</b> Serviços"]
        SC2["<b>Bloco C</b> Mercadorias"]
        SD["<b>Bloco D</b> Serviço Transp."]
        SF["<b>Bloco F</b> Outras Receitas"]
        SM["<b>Bloco M</b> Apuração<br>PIS/COFINS"]
        S1["<b>Bloco 1</b> Complementar"]
        S9["<b>Bloco 9</b> Encerramento"]
    end

    ENTRADA --> PROC2
    CONFIG2 --> PROC2
    PROC2 --> APURACAO
    APURACAO --> SAIDA2

    style ENTRADA fill:#f9e79f,stroke:#f1c40f
    style CONFIG2 fill:#d5f5e3,stroke:#27ae60
    style PROC2 fill:#d6eaf8,stroke:#2e86c1
    style APURACAO fill:#fadbd8,stroke:#e74c3c
    style SAIDA2 fill:#e8daef,stroke:#8e44ad
```

---

## 4. Fluxo - ECD (SPED Contábil)

```mermaid
flowchart LR
    subgraph ENTRADA3 ["1. ENTRADA"]
        direction TB
        LANC["Lançamentos<br>Contábeis"]
        PLANO["Plano de Contas<br>Referencial"]
        CCUSTO["Centros de Custo"]
    end

    subgraph CONFIG3 ["2. CONFIGURAÇÃO"]
        direction TB
        SPED_INI["SPED_DADOS_INI<br>Dados Iniciais"]
        SPED_SIG["SPED_DADOS_SIGNATARIO<br>Signatários"]
        SPED_AUD["SPED_DADOS_AUDITOR<br>Auditor"]
        SPED_LIVRO["SPED_LIVRO_*<br>Config. de Livros"]
    end

    subgraph PROC3 ["3. PROCESSAMENTO"]
        direction TB
        SAF_CONT["SAF_SPED_CONTABIL_FPROC<br>(120 refs)<br><i>Orquestrador Principal</i>"]
        SAF_BPDRE["SAF_SPED_CONTABIL_BPDRE_FPROC<br>(60 refs)<br><i>Balanço e DRE</i>"]
        SAF_REL["SAF_SPED_CONTABIL_REL_FPROC<br>(26 refs)<br><i>Relatórios</i>"]
        WORK["Tabelas WORK<br>(I050, I075, I100,<br>I310, I355)"]
        SAF_CONT --> WORK
        SAF_CONT --> SAF_BPDRE
    end

    subgraph SAIDA3 ["4. BLOCOS DO ARQUIVO"]
        direction TB
        E0["<b>Bloco 0</b> Abertura"]
        EI["<b>Bloco I</b><br>I050 Plano de Contas<br>I075 Hist. Padronizado<br>I100 Centro Custo<br>I200 Lançamentos<br>I250 Partidas<br>I310/I355 Diário Auxiliar"]
        EJ["<b>Bloco J</b><br>J100 Balanço<br>J150 DRE<br>J800 DRA/DMPL<br>J900 Termos"]
        E9["<b>Bloco 9</b> Encerramento"]
    end

    ENTRADA3 --> PROC3
    CONFIG3 --> PROC3
    PROC3 --> SAIDA3

    style ENTRADA3 fill:#f9e79f,stroke:#f1c40f
    style CONFIG3 fill:#d5f5e3,stroke:#27ae60
    style PROC3 fill:#d6eaf8,stroke:#2e86c1
    style SAIDA3 fill:#e8daef,stroke:#8e44ad
```

---

## 5. Mapa de Tabelas por Bloco (EFD ICMS/IPI)

```mermaid
graph TB
    subgraph BLOCO_0 ["Bloco 0 - Cadastros"]
        EFD_CAD_PARTIC["EFD_CAD_PARTIC<br>0150 - Participantes"]
        EFD_CAD_PROD["EFD_CAD_PROD_SERV<br>0200 - Produtos"]
        EFD_CAD_BEM["EFD_CAD_BEM<br>0200 - Bens"]
        EFD_CAD_CCUSTO["EFD_CAD_CCUSTO<br>0600 - C.Custo"]
        EFD_CAD_OBS["EFD_CAD_OBS<br>0460 - Observações"]
        EFD_CAD_NAT["EFD_CAD_NAT_OP<br>0400 - Nat. Operação"]
        EFD_CAD_CONTA["EFD_CAD_CONTA<br>0500 - Plano Contas"]
    end

    subgraph BLOCO_C ["Bloco C - Docs Mercadorias"]
        DWT_DOC2["DWT_DOCTO_FISCAL<br>C100 - NF-e"]
        DWT_ITEM2["DWT_ITEM_DOCTO_FISCAL<br>C170 - Itens"]
        C197["EFD_C197_TEMP<br>C197 - Ajustes ICMS"]
    end

    subgraph BLOCO_E ["Bloco E - Apuração"]
        EST_APUR["EST_APUR_ICMS<br>E110 - Apuração ICMS"]
        EFD_AJUST2["EFD_AJUSTES_AUTO_REGRAS<br>E111/E116 - Ajustes"]
        EFD_APUR_A["EFD_APURACAO_ASSISTIDA<br>Apuração Assistida"]
    end

    subgraph BLOCO_G ["Bloco G - CIAP"]
        APT_AQ["APT_AQUISICAO<br>G125 - Bens"]
        EFD_BEM_CIAP2["EFD_BEM_CIAP<br>G126 - Parcelas ICMS"]
    end

    subgraph BLOCO_H ["Bloco H - Inventário"]
        INV["SAFX35<br>H010 - Inventário Físico"]
    end

    subgraph BLOCO_K ["Bloco K - Produção"]
        PROD["Controle Produção<br>K100-K260"]
    end

    style BLOCO_0 fill:#d5f5e3,stroke:#27ae60
    style BLOCO_C fill:#f9e79f,stroke:#f1c40f
    style BLOCO_E fill:#fadbd8,stroke:#e74c3c
    style BLOCO_G fill:#d6eaf8,stroke:#2e86c1
    style BLOCO_H fill:#e8daef,stroke:#8e44ad
    style BLOCO_K fill:#fdebd0,stroke:#e67e22
```

---

## 6. Packages PL/SQL - Dependências

```mermaid
graph TD
    subgraph EFD_FISCAL ["EFD ICMS/IPI"]
        EFD_FPROC["<b>EFD_SPED_FPROC</b><br>Orquestrador<br>(32 tabelas)"]
        EFD71["EFD71_GERA<br>Init E/G (40 refs)"]
        EFD72["EFD72_GERA<br>Ajustes E (47 refs)"]
        EFD73["EFD73_GERA<br>Detalhes E"]
        EFD79["EFD79_GERA<br>Inventário H"]
        EFD82["EFD82_GERA<br>Produção K"]
        EFD88["EFD88_GERA<br>Complementar 1"]
        EFD_ESP["EFD_SPED_ESP_FPROC<br>Estados Especiais (34 refs)"]
        EFD_IES["EFD_SPED_IES_FPROC<br>Instituições (31 refs)"]
        EFD_CONV["EFD_SPED_CONV_FPROC<br>Conversão (23 refs)"]
        EFD_RESSARC["EFD_CALC_RESSARC_MG_FPROC<br>Ressarcimento MG (53 refs)"]

        EFD_FPROC --> EFD71
        EFD_FPROC --> EFD72
        EFD_FPROC --> EFD73
        EFD_FPROC --> EFD79
        EFD_FPROC --> EFD82
        EFD_FPROC --> EFD88
        EFD_FPROC --> EFD_ESP
        EFD_FPROC --> EFD_IES
        EFD_FPROC --> EFD_CONV
    end

    subgraph ECD_CONTABIL ["ECD - SPED Contábil"]
        SAF_CONT2["<b>SAF_SPED_CONTABIL_FPROC</b><br>Orquestrador (120 refs)"]
        SAF_BPDRE2["SAF_SPED_CONTABIL_BPDRE_FPROC<br>Balanço/DRE (60 refs)"]
        SAF_REL2["SAF_SPED_CONTABIL_REL_FPROC<br>Relatórios (26 refs)"]
        SAF_CONT2 --> SAF_BPDRE2
        SAF_CONT2 --> SAF_REL2
    end

    subgraph EPC_CONTRIB ["EFD Contribuições"]
        EPC_FPROC2["<b>EPC_SPED_FPROC</b><br>Orquestrador (39 refs)"]
        EPC_SCP2["EPC_SPED_SCP_FPROC<br>SCP (36 refs)"]
        EPC_DIC2["EPC_DICIONARIO<br>Mapeamento (53 refs)"]
        EPC_FPROC2 --> EPC_SCP2
        EPC_FPROC2 --> EPC_DIC2
    end

    style EFD_FISCAL fill:#d6eaf8,stroke:#2e86c1
    style ECD_CONTABIL fill:#d5f5e3,stroke:#27ae60
    style EPC_CONTRIB fill:#e8daef,stroke:#8e44ad
```

---

## 7. Menus do TAX ONE (Navegação)

```mermaid
graph LR
    MENU["<b>TAX ONE</b>"]

    MENU --> SPED_MENU["SPED"]

    SPED_MENU --> EFD_FISCAL_M["EFD Fiscal<br>(ICMS/IPI)"]
    SPED_MENU --> EFD_CONTRIB_M["EFD Contribuições<br>(PIS/COFINS)"]
    SPED_MENU --> ECD_M["ECD<br>(Contábil)"]
    SPED_MENU --> ECF_M["ECF"]
    SPED_MENU --> REINF_M["EFD-Reinf"]

    EFD_FISCAL_M --> EFD_PARAM["Parâmetros"]
    EFD_FISCAL_M --> EFD_CAD_M["Cadastros"]
    EFD_FISCAL_M --> EFD_GERA["Geração"]
    EFD_FISCAL_M --> EFD_VALID["Validação"]
    EFD_FISCAL_M --> EFD_TRANSM["Transmissão"]

    EFD_CAD_M --> CAD_PARTIC_M["Participantes"]
    EFD_CAD_M --> CAD_PROD_M["Produtos/Serviços"]
    EFD_CAD_M --> CAD_BEM_M["Bens (CIAP)"]
    EFD_CAD_M --> CAD_AJUST_M["Regras de Ajuste"]

    EFD_GERA --> GERA_ARQ["Gerar Arquivo"]
    EFD_GERA --> GERA_REL["Relatório Analítico"]

    ECD_M --> ECD_DADOS["Dados Iniciais"]
    ECD_M --> ECD_LIVROS["Livros"]
    ECD_M --> ECD_DEM["Demonstrações<br>(Balanço/DRE)"]
    ECD_M --> ECD_GERA2["Geração"]

    EFD_CONTRIB_M --> EPC_PARAM_M["Parâmetros"]
    EFD_CONTRIB_M --> EPC_CAD_M["Cadastros"]
    EFD_CONTRIB_M --> EPC_APUR_M["Apuração"]
    EFD_CONTRIB_M --> EPC_GERA_M["Geração"]

    style MENU fill:#1a5276,color:#fff
    style SPED_MENU fill:#2e86c1,color:#fff
    style EFD_FISCAL_M fill:#5dade2,color:#fff
    style EFD_CONTRIB_M fill:#5dade2,color:#fff
    style ECD_M fill:#5dade2,color:#fff
    style ECF_M fill:#5dade2,color:#fff
    style REINF_M fill:#5dade2,color:#fff
```

---

## 8. Volumetria e Referências

| Submódulo | Tabelas | Packages PL/SQL | Refs PL/SQL | E2E Specs |
|-----------|---------|-----------------|-------------|-----------|
| EFD ICMS/IPI | 73 (EFD_*) | EFD_SPED_FPROC + 9 blocos | ~300 | efdFiscal/ |
| EFD Contribuições | 88 (EPC_*) | EPC_SPED_FPROC + 2 | ~128 | efdContribuicoes/ |
| ECD Contábil | 37 (SPED_*) | SAF_SPED_CONTABIL_* (3) | ~206 | ecdEscrituracaoContabilDigital/ |
| CIAP | 35 (APT_*) | Integrado ao EFD (G) | ~50 | — |
| COTEPE | 20 | SAF_MM_COTEPE_FPROC | ~57 | — |
| ECF | 7 | — | — | — |
| **Total SPED** | **~280** | **~16 packages** | **~741** | **45 specs** |

---

*Gerado automaticamente a partir do knowledge base do taxone-support-dev.*
*Diagramas em Mermaid — renderizar em qualquer viewer Markdown compatível (GitHub, VS Code, etc).*
