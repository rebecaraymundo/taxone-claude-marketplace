# MTZ_REINF_Tela_Informacoes_Contribuinte

> Fonte: MTZ_REINF_Tela_Informacoes_Contribuinte.docx






THOMSON REUTERS

Tela Informações do Contribuinte
SPED - REINF



DOCUMENTO DE REQUISITO


Sumário

1.	Tela	3
2.	Regras dos Campos	3



























## Tela





## Regras dos Campos


Localização da tela: Módulo: SPED >> REINF
Menu: Parâmetros >> Informações do Contribuinte

Título da tela: Informações do Contribuinte








| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-11064 | Tela Dados Iniciais | Inclusão de Tela |
| MFS-12777 | Tela Dados Iniciais | Alteração no nome da tela para “Informações do Contribuinte” |
| MFS20930 | Lara Aline | Ajuste na regra do campo Desoneração da Folha e Classificação Tributária de acordo com o novo Layout 1.4. |
| MFS-81450 | Alessandra Cristina Navatta | Inclusão de campo, para atendimento do evento R-1000, versão 2.1 do REINF |
| MFS-90001 | Alessandra Cristina Navatta | Alteração da versão 2.1 para 2.1.1 |
| MFS-523048 | Alessandra Cristina Navatta | Inclusão do campo Indicativo de Entidade Vinculada a União, para atendimento do evento R-1000, versão 2.1.1 |
| MFS-840399 | Alessandra Cristina Navatta | Inclusão do campo Indicador de Pertencimento do IRRF, para atendimento do evento R-1000 (campo indPertIRRF), versão 2.1.2 (Nota Técnica 02/2025) |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Dropdown | S | S | Default: Não Preenchido | Na lista será demonstrado código e a razão social de cada estabelecimento centralizador*, somente da empresa que acessou o módulo.  Centralizador – XXX-XXXXXXXXXXXXXXXXX (Centralizador + cód. E razão social do estabelecimento)  Caso algum estabelecimento não tenha sido associado a uma centralização, este será demonstrado na listagem de estabelecimentos precedido da palavra “Descentralizado”:  Descentralizado – XXX-XXXXXXXXXXXXXXXXX (Descentralizado + cód. E razão social do estabelecimento)  * Entende-se Estabelecimento Centralizador aquele que foi cadastrado como tal na tela de “Centralização da Escrituração de Obrigações Federais”, no módulo Parâmetro / menu Preliminares. Caso não exista nenhum estabelecimento cadastrado como centralizador nesta tela para a empresa serão demonstrados os estabelecimentos como descentralizados. | MFS-11064 |
| Início Validade | Data | S | S |  | Deverá ser preenchido com a data do primeiro dia do mês, caso preenchido com data diferente ou não preenchido exibir a seguinte mensagem: Campo Início Validade deve ser preenchido com o primeiro dia do mês.  Caso não for uma data válida exibir a seguinte mensagem: O Campo Início Validade com formato inválido. | MFS-11064 |
| Fim Validade | Data | N | S |  | Deverá ser preenchido com a data do último dia do mês, caso preenchido com data diferente exibir a seguinte mensagem: Campo Fim Validade deve ser preenchido com o último dia do mês.  Caso não for uma data válida exibir a seguinte mensagem: O Campo Fim Validade com formato inválido.  Caso data menor que data início de validade exibir a seguinte mensagem: “A Data Final deve ser maior ou igual a Data Inicial” | MFS-11064 |
| Registro de Informações de Cadastro do Contribuinte | Registro de Informações de Cadastro do Contribuinte | Registro de Informações de Cadastro do Contribuinte | Registro de Informações de Cadastro do Contribuinte | Registro de Informações de Cadastro do Contribuinte | Registro de Informações de Cadastro do Contribuinte | Registro de Informações de Cadastro do Contribuinte |
| Classificação Tributária | Dropdown | S | S | Defaulf: Não preenchido | Serão listados os seguintes códigos:  01 – Empresa enquadrada no regime de tributação Simples Nacional com tributação previdenciária substituída  02 – Empresa enquadrada no regime de tributação Simples Nacional com tributação previdenciária não substituída  03 – Empresa enquadrada no regime de tributação Simples Nacional com tributação previdenciária substituída e não substituída  04 – MEI – Micro Empreendedor Individual  06 – Agroindústria  07- Produtor Rural Pessoa Jurídica  08-Consórcio Simplificado de Produtores Rurais  09 – Órgão Gestor de Mão de Obra  10 – Entidade Sindical a que se refere a Lei 12.023/2009 11 – Associação Desportiva que mantém Clube de Futebol Profissional  13 – Banco, caixa econômica, sociedade de crédito, financiamento e investimento e demais empresas relacionadas no parágrafo 1º do art. 22 da Lei 8.212./91  14 – Sindicatos em geral, exceto aquele classificado no código [10]  21 – Pessoa Física, exceto Segurado Especial  22 – Segurado Especial  60 – Missão Diplomática ou Repartição Consular de carreira estrangeira  70 – Empresa de que trata o Decreto 5.436/2005  80 – Entidade Imune ou Isenta Beneficente de Assistência Social isenta de contribuições sociais  85 – Ente Federativo, Órgãos da União, Autarquias e Fundações Públicas  99 – Pessoas Jurídicas em Geral  Caso o usuário selecionar qualquer opção diferente de 02, 03 ou 99, no campo Desoneração da Folha será selecionada a opção ‘Não Aplicável’, sem possibilidade de alteração.  Caso não preenchido exibir a seguinte mensagem: “O campo Classificação Tributária deve ser informado”. | MFS-11064 MFS20930 |
| Escrituração Contábil na ECD | Radio Button | S | S | Default: Empresa Entrega ECD | Indicativo:   - Não Faz - Empresa entrega a ECD | MFS-11064 |
| Desoneração da Folha | Radio Button | S | S | Default: Não Aplicável Empresa enquadrada nos termos da Lei 12.546/2011 | Indicativo:  - Não Aplicável - Empresa enquadrada nos artigos 7° a 9° da Lei 12.546/2011 termos da Lei 12.546/2011  A opção ‘Empresa enquadrada nos artigos 7° a 9° da Lei 12.546/2011’ ficará disponível para seleção APENAS se no campo Classificação Tributária for selecionada as opções 02, 03 ou 99. | MFS-11064 MFS20930 |
| Acordo de Isenção de Multa | Radio Button | S | S | Default: Sem acordo | Indicativo:  - Sem acordo - Com acordo | MFS-11064 |
| Situação Pessoa Jurídica | Radio Button | N | S | Default: 0 – Situação Normal | Serão Listadas as seguintes opções:  0 – Situação Normal 1 – Extinção 2 – Fusão  3 – Cisão 4 – Incorporação | MFS-11064 |
| Indicativo de Entidade Vinculada a União | Dropdown | N | S | Default: Não preenchido | Serão exibidas as opções:  Vazio 0 - Não aplicável 1 - Órgão da Administração Pública Federal Direta, autarquias e fundações da Administração Pública Federal, empresas públicas, sociedades de economia mista, ou demais entidades em que a que União detenha maioria do capital social sujeito a voto, recebe recursos do Tesouro Nacional e está obrigada a registrar a execução orçamentária no Siafi | MFS-523048 |
| Data da Transformação de Entidade Beneficente de Assistência Social Isenta de Contribuições Sociais em Sociedade com Fins Lucrativos – Art. 13 – Lei 11096/2005 | Data | N | S |  | Informar a data da transformação de entidade beneficente de assistência social isenta de contribuições sociais em sociedade com fins lucrativos – Art. 13 – Lei 11096/2005. | MFS-81450 |
| Indicador de Pertencimento do IRRF | Check-box |  |  | Default : Desmarcado | Indicador de pertencimento do IRRF. Preenchimento exclusivo para os contribuintes cuja natureza jurídica seja igual a [126-0, 127-9, 129-5, 130-9]. | MFS-840399 |
| Registro de Informações de Contato do Contribuinte | Registro de Informações de Contato do Contribuinte | Registro de Informações de Contato do Contribuinte | Registro de Informações de Contato do Contribuinte | Registro de Informações de Contato do Contribuinte | Registro de Informações de Contato do Contribuinte | Registro de Informações de Contato do Contribuinte |
| Nome | Textbox | S | S |  | Caso não preenchido exibir a seguinte mensagem: “O campo Nome deve ser informado”. | MFS-11064 |
| CPF | Textbox | S | S |  | Caso não preenchido exibir a seguinte mensagem: “O campo CPF deve ser informado”.  Obs: Deve ser um CPF válido | MFS-11064 |
| Telefone | Textbox | N | S | DDDTelefone | Este campo deve ser preenchido pelo cliente com ddd e telefone | MFS-11064 |
| Celular | Textbox | N | S | DDDTelefone | Este campo deve ser preenchido pelo cliente com ddd e telefone | MFS-11064 |
| E-mail | Textbox | N | S |  |  | MFS-11064 |
| Registro de Informações da Software House  Obs: Permitir a inclusão de várias empresas (Software House) desenvolvedoras de aplicações geradoras de arquivos. Caso houver informação então: | Registro de Informações da Software House  Obs: Permitir a inclusão de várias empresas (Software House) desenvolvedoras de aplicações geradoras de arquivos. Caso houver informação então: | Registro de Informações da Software House  Obs: Permitir a inclusão de várias empresas (Software House) desenvolvedoras de aplicações geradoras de arquivos. Caso houver informação então: | Registro de Informações da Software House  Obs: Permitir a inclusão de várias empresas (Software House) desenvolvedoras de aplicações geradoras de arquivos. Caso houver informação então: | Registro de Informações da Software House  Obs: Permitir a inclusão de várias empresas (Software House) desenvolvedoras de aplicações geradoras de arquivos. Caso houver informação então: | Registro de Informações da Software House  Obs: Permitir a inclusão de várias empresas (Software House) desenvolvedoras de aplicações geradoras de arquivos. Caso houver informação então: | Registro de Informações da Software House  Obs: Permitir a inclusão de várias empresas (Software House) desenvolvedoras de aplicações geradoras de arquivos. Caso houver informação então: |
| CPNJ | Textbox | S | S |  | Caso não preenchido exibir a seguinte mensagem: “O campo CNPJ deve ser informado”.  Obs: Deve ser um CNPJ válido. | MFS-11064 |
| Nome/Razão Social | Textbox | S | S |  | Caso não preenchido exibir a seguinte mensagem: “O campo Nome/Razão Social deve ser informado”. | MFS-11064 |
| Nome do Contato | Textbox | S | S |  | Caso não preenchido exibir a seguinte mensagem: “O campo Nome do Contato deve ser informado”. | MFS-11064 |
| Telefone | Textbox | N | S | DDDTelefone | Este campo deve ser preenchido pelo cliente com ddd e telefone | MFS-11064 |
| E-mail | Textbox | N | S |  |  | MFS-11064 |
