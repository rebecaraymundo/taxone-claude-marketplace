# MTZ_NFSENACIONAL_Geracao_do_Meio_Magnetico

- **Fonte:** MTZ_NFSENACIONAL_Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2021-05-14
- **Tamanho:** 149 KB

---

                                                                            THOMSON REUTERS

	

Municipal 

 Serviços Tomados 

	Geração do Meio Magnético – NFSE NACIONAL 

##### 	DOCUMENTO DE REQUISITO	

__MFS/CH__

__Nome__

__Descrição__

MFS11924

João Henrique de Araujo

<a id="OLE_LINK14"></a><a id="OLE_LINK15"></a><a id="OLE_LINK16"></a>Este documento tem como objetivo tratar a geração do meio magnético em XML de serviços tomados para atender o novo validador NFSE NACIONAL\.

CH21626\_2017

\(MFS\-14638\)

João Henrique de Araujo

Essa alteração tem como objetivo não considerar NFS\-e de Prestadores de dentro do município de Ipatinga\-MG\.

MFS31709

Andréa Rocha

Este documento tem como objetivo incluir o município de Pirajuí no validador NFSE Nacional\.

MFS31775

Andréa Rocha

Este documento tem como objetivo incluir o município de Água Boa no validador NFSE Nacional\.

MFS31767

Andréa Rocha

Este documento tem como objetivo incluir o município de Ponta Grossa no validador NFSE Nacional\.

MFS29822

Andréa Rocha

Este documento tem como objetivo incluir o município de Andirá no validador NFSE Nacional\.

MFS33775

Aline Melo

Este documento tem como objetivo retornar o município de Ponta Grossa para o validador FINTELISS\.

MFS40578

Andréa Rocha

Este documento tem como objetivo incluir o município de José Bonifácio no validador NFSE Nacional\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MSF/CH__

__RN01__

__Regra para inclusão do novo módulo no Manager:__

O módulo “Ipatinga” deve ficar localizado no grupo “Municipal”\.

Descrição do módulo:__ “Consiste no envio e processamento da declaração mensal das notas fiscais de serviços eletrônica tomados do município de Ipatinga”\.__

__MFS11924__

__RN02__

__Regra para abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “MG” e ao código de município do IBGE igual a “31307” \(Ipatinga\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Ipatinga, Minas Gerais\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS11924__

__RN03__

__Estrutura de menus do módulo:__

- Arquivo
- Obrigações
	- __Geração do Meio Magnético __
	- __Arquivo de Entradas de Serviços \(Const\.Civil/Utilities/Telecom\)__
- Janela
- Ajuda

__MFS11924__

__RN04__

__Regra de nomenclatura do arquivo:__

O arquivo pode ser gerado com qualquer nome, a critério do contribuinte, então colocaremos a nomenclatura padrão\.

__       NFSENACIONAL\_MUNICIPIO\_DDMMAAAA\.XML__, onde:

       __NFSENACIONAL__: representa a obrigação que está sendo gerada\. 

       __MUNICIPIO__: representa o município que está sendo gerado\.

       __DDMMAAAA__: representa a data inicial da geração

       __\.XML__: extensão do arquivo\.

*Exemplo:* NFSENACIONAL\_IPATINGA\_01012010\.XML

Quando o parâmetro “Quebrar Arquivos por Data de Emissão” estiver marcado, deve ser realizada a seguinte verificação: 

- Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. 
- Esse arquivo deve conter __todas__ as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivos de acordo com as competências geradas\. A nomenclatura desses arquivos deverá ser como o exemplo abaixo:

__        NFSENACIONAL\_MUNICIPIO\_DDMMAAAA\_MMAAAA\.XML__, onde:

__        NFSENACIONAL__: representa a obrigação que está sendo gerada\.    

__        MUNICIPIO__: representa o município que está sendo gerado\.   

        __DDMMAAAA__: representa a data inicial da geração\.   

__        MMAAAA:__ mês da competência referente à nota gerada

        __\.XML__: extensão do arquivo\.

Ex: NFSENACIONAL\_IPATINGA\_01012014\_122013\.XML

Neste caso o arquivo normal __também__ deverá ser gerado, além dos arquivos indicando competências distintas\. Estas notas com competência distintas não devem estar no arquivo normal\.

__*Observação:* __Este parâmetro \(Quebrar Arquivo por Data de Emissão\) será válido apenas para Notas de Serviços Tomados\.

__MFS11924__

__RN05__

__Regra dos campos da Tela Obrigações – Geração Meio Magnético:__

__Menu:__  Obrigações >> Geração do Meio Magnético:

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial: __O campo deve ser um text Box com a seguinte __máscara: DD/MM/AAAA__\. Por default esse campo deve ser preenchido com o primeiro dia do mês corrente\. Utilizar SYSDATE \(data mais atual\)\.

__Data Final: __O campo deve ser um text Box com a seguinte __máscara: DD/MM/AAAA__\. Por default esse campo deve ser preenchido com o último dia do mês corrente\. Utilizar SYSDATE \(data mais atual\)\. 

A Data Final não poderá ser __menor__ que a Data Inicial\. Caso o usuário informe, o sistema deverá exibir a mensagem de aviso: “Data Final digitada não pode ser menor que a Data Inicial informada”\.                                  

__Quebrar arquivo por Data de Emissão:__ Deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Estabelecimento:__ O sistema deve exibir os estabelecimentos pertencentes ao município de Gaspar, que estejam licenciados e que o usuário possua acesso no PowerLock\.

__MFS11924__

__RN06__

__Regra para abas existentes na geração do meio magnético:__

Após processar o meio magnético devem ser exibidas as abas “Log”, “Arquivo”, “Processos” e “Relatório”\. 

A aba “Arquivo” deve exibir o arquivo que poderá ser salvo localmente\.

A aba “Log” deve exibir a mensagem “Processo concluído com sucesso” quando o arquivo for gerado corretamente, caso contrário exibir a mensagem “Processo concluído com erros”\.

__MFS11924__

__RN07__

__Regras para geração do Meio Magnético:__

__Regras referentes à formatação dos registros gerados no meio magnético:__

A seguir formatações de dados que devem ser seguidas para geração do meio magnético na estrutura do arquivo:

1. __O arquivo a ser gerado para importação dever ser no formato__ __‘XML’__\.
2. __Não deve ser inserido caractere não significativo para preencher o tamanho completo do campo, ou seja, zeros antes de número ou espaço em branco após a cadeia de caracteres\. A posição do campo é definida na estrutura do documento XML através de tags \(<tag>conteúdo</tag>\)\.__
3. __A regra constante do parágrafo anterior deverá estender\-se aos campos para os quais não há indicação de obrigatoriedade e que, no entanto, seu preenchimento torna\-se obrigatório, seja condicionado à legislação específica ou ao negócio do contribuinte\. Nesse caso, deverá constar a tag com o valor correspondente e, para os demais campos não obrigatórios, deverão ser eliminadas as tags\.__
4. __Para reduzir o tamanho final do arquivo XML do arquivo, alguns cuidados de programação deverão ser assumidos:__

\- Não incluir "zeros não significativos" para campos numéricos;

\- Não incluir "espaços" no início ou no final de campos numéricos e alfanuméricos;

\- Não incluir comentários no arquivo XML;

\- Não incluir anotação e documentação no arquivo XML \(tag annotation e tag documentation\);

\- Não incluir caracteres de formatação no arquivo XML \("line\-feed", "carriage return", "tab", caractere de "espaço" entre as tags\)\.

\- Não incluir caracteres de formatação no arquivo XML \("line\-feed", "carriage return", "tab", caractere de "espaço" entre as tags\)\.

\- Para quebra de linha na exibição para os campos contendo caracteres Discriminacao e Outrasinformacoes, utilizar a sequência “\\s\\n”\.

1. __As tags que permitirem valores nulos devem ser omitidas da estrutura XML a ser enviada quando seus valores forem nulos\.__
2. __A seguir encontra\-se a tabela com a lista dos tipos simples que serão utilizados como tipos de dados\. A tabela consiste das seguintes colunas:__

\- Campo: nome do tipo simples;

\- Tipo: tipo primitivo de dados utilizados pelo campo: __C \- Caractere, N \- Número, D \- Data ou Data/Hora e T \- Token__;

\- Descrição: descreve informações sobre o campo;

\- Tam\.: tamanho do campo;

1.  __Quando forem caracteres, o tamanho define a quantidade máxima de caracteres que o texto poderá ter;__
2.  __Quando for numérico o tamanho pode ser representado das seguintes formas:__

__\- Número__ __inteiro__, que define o total de dígitos existente no número\. Exemplo: “15” significa que o número poderá ter, no máximo, 15 dígitos;

\- __Número fracionário__, que define o total de dígitos e quantos deles serão designados para a parte fracionária\. Exemplo: “15,2” significa que o número poderá ter, no máximo, 15 dígitos sendo 2 deles a da parte fracionária\. A parte fracionária não é obrigatória quando assim definido;

\- __Número decimal__, tem o formato o __0\.00,__ não deve ser utilizado separador de milhar\. O ponto \(\.\) deve ser utilizado para separar a parte inteira da fracionária\. Exemplo: 48\.562,25 = 48562\.25 1,00 = 1\.00 ou 0,50 = 0\.50 ou 0\.5            

\- __Valores Percentuais__, Tem o formato o __00\.00__\. O formato em percentual presume o valor percentual em sua forma fracionária\. O ponto \(\.\) separa a parte inteira da fracionária\. Exemplo: 62% = 62, 15% = 15, 25,32% = 25\.32\.

__MFS11924__

__RN08__

__Regra p/ Recuperação das notas fiscais de Serviços Tomados \(só geraremos serviços tomados no arquivo\)\.__

Contemplar todas as notas fiscais de serviço com as seguintes particularidades:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\);
- Classificação da nota fiscal = 2 ou 3 
- Empresa e estabelecimento escolhidos na tela de geração;
- Data fiscal da nota dentro do período de referência informado na tela de geração;
- Não será considerado documento sem item;
- Não considerar documentos fiscais cancelados;
- O agrupamento das NFS\-e será feito através dos campos: __ALIQ\_TRIBUTO\_ISS, COD\_SERV\_LEI\_116 e IND\_ISS\_RETIDO\.__
- Não considerar NFS\-e de Prestadores de dentro do município da obrigação \(Estabelecimento\), ou seja, quando a Pessoa Fis/Jur cadastrada na NFS\-e estiver com o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR __Igual__ ao do município da obrigação \(Estabelecimento\)\.

__MFS11924__

CH21626\_2017

\(MFS\-14638\)

__RN09__

__Estrutura do Arquivo:__

__Exemplo de XML de Serviços Tomados:__

<?xml version="1\.0" encoding="UTF\-8"?>

[<ConsultarNfseServicoPrestadoResposta>](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)

  [<ListaNfse>](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)

    [<CompNfse>](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)

      [<Nfse versao="__2\.02__">](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)

        [<InfNfse Id="__10066518__">](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)

            <Numero>201600000102860</Numero>

            <CodigoVerificacao>ANMZ\-JMAX</CodigoVerificacao>

            <DataEmissao>2016\-11\-01T17:47:26</DataEmissao>

       [<ValoresNfse>](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)

            <BaseCalculo>100\.00</BaseCalculo>

            <Aliquota>0\.0300</Aliquota>

            <ValorIss>3\.00</ValorIss>

            <ValorLiquidoNfse>97\.00</ValorLiquidoNfse>            

       </ValoresNfse>

       <ValorCredito>0</ValorCredito>

       [<PrestadorServico>](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)

            [<IdentificacaoPrestador>](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)

                [<CpfCnpj>](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)

                      <Cnpj>00000000000000</Cnpj>

                 </CpfCnpj> 

                 <InscricaoMunicipal>30854</InscricaoMunicipal>

             </IdentificacaoPrestador>

             <RazaoSocial>EMPRESA DE TESTE</RazaoSocial>

             <NomeFantasia>EMPRESA DE TESTE</NomeFantasia>

             [<Endereco>](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)

                      <Endereco>AV\. PRESIDENTE TANCREDONEVES</Endereco>

                      <Numero>222</Numero>

                      <Bairro>ZACARIAS</Bairro>

                      <CodigoMunicipio>3113404</CodigoMunicipio>

                      <Uf>MG</Uf>

                      <Cep>35300102</Cep>

              </Endereco>

              [<Contato>](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)

                       <Telefone>3333216183</Telefone>

                       <Email>teste@teste\.com</Email> 

              [</Contato>](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)

          </PrestadorServico>

          [<OrgaoGerador>](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)

              <CodigoMunicipio>3113404</CodigoMunicipio>

              <Uf>MG</Uf>

          </OrgaoGerador>

          [<DeclaracaoPrestacaoServico>](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)

            [<InfDeclaracaoPrestacaoServico Id="__InfDec\_10066518__">](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)

                        <Competencia>2016\-11\-01</Competencia>

                       [<Servico>](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml) 

                             [<Valores>](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)

                                  <ValorServicos>100\.00</ValorServicos>

                                  <ValorDeducoes>0\.00</ValorDeducoes>

                                  <ValorPis>0\.00</ValorPis>

                                  <ValorCofins>0\.00</ValorCofins>

                                  <ValorInss>0\.00</ValorInss>

                                  <ValorIr>0\.00</ValorIr>

                               <ValorCsll>0\.00</ValorCsll>

                               <OutrasRetencoes>0\.00</OutrasRetencoes>

                               <ValorIss>3\.00</ValorIss>

                               <Aliquota>0\.0300</Aliquota>

                               <DescontoIncondicionado>0\.00</DescontoIncondicionado>

                               <DescontoCondicionado>0\.00</DescontoCondicionado>

                           </Valores>

                           <IssRetido>1</IssRetido>

                           <ItemListaServico>01\.01</ItemListaServico>

                           <CodigoCnae>0000000</CodigoCnae>

                           <CodigoTributacaoMunicipio>0101</CodigoTributacaoMunicipio>

                           <Discriminacao>dghdfh</Discriminacao>

                           <CodigoMunicipio>3113404</CodigoMunicipio>

                           <ExigibilidadeISS>1</ExigibilidadeISS>

                           <MunicipioIncidencia>3113404</MunicipioIncidencia>

                      </Servico>

                      [<Prestador>](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)

                           [<CpfCnpj>](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)

                                 <Cnpj>00000000000000</Cnpj>

                           </CpfCnpj>

                           <InscricaoMunicipal>30854</InscricaoMunicipal>

                      </Prestador>

                      [<Tomador>](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)

                            [<IdentificacaoTomador>](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)

                                  [<CpfCnpj>](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)

                                        <Cnpj>00000000000000</Cnpj>

                                  </CpfCnpj>

                                  <InscricaoMunicipal>1233</InscricaoMunicipal>

                             </IdentificacaoTomador>

                             <RazaoSocial>FIADOR</RazaoSocial>

                             [<Endereco>](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)

                                   <Endereco>Rua Coronel Galdino Pires</Endereco>

                                   <Numero>50</Numero>

                                   <Complemento>Ap300</Complemento>

                                   <Bairro>Centro</Bairro>

                                   <CodigoMunicipio>3113404</CodigoMunicipio>

                                   <Uf>MG</Uf>

                                     <Cep>35300048</Cep>

                               </Endereco>

                               [<Contato>](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)

                                     <Email>[teste@teste\.com</Email](mailto:teste@teste.com%3c/Email)>

                               </Contato>

                          </Tomador>

                          <RegimeEspecialTributacao>2</RegimeEspecialTributacao>

                          <OptanteSimplesNacional>2</OptanteSimplesNacional>

                          <IncentivoFiscal>2</IncentivoFiscal>

                    </InfDeclaracaoPrestacaoServico>

                   </InfNfse>

                 </DeclaracaoPrestacaoServico>

               </Nfse>

             </CompNfse>

           </ListaNfse>

         </ConsultarNfseServicoPrestadoResposta>

__MFS11924__

__RN10__

__Regra para o campo <?xml version="1\.0" encoding="UTF\-8"?> __Tag relacionada à formatação do arquivo deve conter o texto fixo: __<?xml version="1\.0" encoding="utf\-8"?> __TAG obrigatória\.

__MFS11924__

__RN11__

__Regra para o campo __[__<ConsultarNfseServicoPrestadoResposta>__](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)__ __Tag relacionada à abertura da resposta do serviço com o texto fixo: __<ConsultarNfseServicoPrestadoResposta>__ TAG obrigatória\.

__MFS11924__

__RN12__

__Regra para o campo __[__<__[__ListaNfse>__](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)__ __Tag relacionada à abertura da lista das notas fiscais com o texto fixo: __<__[__ListaNfse>__](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)__ __TAG obrigatória\.

__MFS11924__

__RN13__

__Regra para o campo __[__<__[__CompNfse>__](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)__ __Tag relacionada à abertura da estrutura de compartilhamento de dados de uma NFS\-e com o texto fixo: __<__[__CompNfse>__](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)__ __TAG obrigatória\.

__MFS11924__

__RN14__

__Regra para o campo __[__<Nfse versao= “__2\.02__” >__](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)__ __Tag relacionada à versão da nota fiscal\.  Preencher com o valor fixo __“2\.02”__\. TAG obrigatória\.

__MFS11924__

__RN14\.a__

__Para o município de José Bonifácio, __

__Regra para o campo __[__<Nfse versao= “__2\.01__” >__](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)__ __Tag relacionada à versão da nota fiscal\.  Preencher com o valor fixo __“2\.01”__\. TAG obrigatória\.

__MFS40578__

__RN15__

__Regra para o campo __[__<InfNfse Id="__ __">__](file:///C:/Users/u6038715/Desktop/MasterSaf%20DW/Backlog%20Novo%20e%20Evolução/MFS%20-%20Municipal/MFS_11924%20-%20IPATINGA_MG/xml_tomada.xml)__  __Tag relacionada à abertura da informação de ID da NFS\-e, será preenchido com o valor ‘nulo’\.

__MFS11924__

__RN16__

__Regra para o campo <Numero> da TAG </Numero>__

Esse campo identifica o número da nota fiscal de serviço eletrônica\.

Preencher com:

__Tela\-A__ 🡸__  Modulo: __Básicos >> Parâmetros__ Menu:__ Preliminares >> __Parametrização para Número do Documento Fiscal de Serviço \(60 Posições\)__

Se o campo __COD\_ESTAB__ selecionado na geração for __=__ o campo __COD\_ESTAB__ da __Tela\-A__

 __E__

Campo __Data\_fiscal __for maior ou igual o campo __Data Inicio__ da __Tela\-A__ 

 __E__

Campo __NUM\_DOCFIS\_SERV __da tabela __DWT\_DOCTO\_FISCAL__ estiver preenchido

__ __ 

Então, Preencher com o campo __NUM\_DOCFIS\_SERV__ da tabela __DWT\_DOCTO\_FISCAL__

__Senão __

Preencher com o campo __NUM\_DOCFIS__ da tabela __DWT\_DOCTO\_FISCAL__

TAG Obrigatória\.

Formato: 999999999999999 

Tamanho: 15 posições

Tipo: Numérico

__MFS11924__

__RN17__

__Regra para o campo <CodigoVerificacao> da TAG </CodigoVerificacao>__

Essa TAG será preenchida com o valor: ‘nulo’\. 

__MFS11924__

__RN18__

__Regra para o campo <DataEmissao> da TAG </DataEmissao>__

Esse campo identifica à data de emissão do documento fiscal\. Preencher com a informação do campo __DATA\_EMISSAO __da tabela __DWT\_DOCTO\_FISCAL \(campo 11 da SAFX07\)__

Tem o formato __AAAA\-MM\-DDTHH:MM:SS__ onde:

- __AAAA__ representa o ano com quatro caracteres, 
- __MM__ representa o mês com dois caracteres, 
- __DD__ representa o dia com dois caracteres, 
- __T__ representa o caractere de formatação __\(devendo ser usado um espaço em branco\)__ que deve existir separando a data da hora, 
- __HH__ representa a hora com dois caracteres, 
- __MM__ representa os minutos com dois caracteres; 
- __SS__ representa os segundos com dois caracteres 

TAG Obrigatória\.

Formato: AAAA\-MM\-DDTHH:MM:SS Exemplo: 2016\-11\-01T00:00:00

Tamanho: 19 posições

Tipo: Data

__MFS11924__

__RN19__

__Regra para o campo <ValoresNfse> __Tag que identifica à abertura do conjunto de valores que compõem o documento fiscal com o texto fixo: __<ValoresNfse>  __TAG obrigatória\.

__ MFS11924__

__ RN20__

__Regra para o campo <BaseCalculo> da TAG </BaseCalculo>__

Esse campo identifica a base de cálculo do serviço\. Preencher com o somatório do campo __VLR\_BASE\_ISS\_1 OU VLR\_BASE\_ISS\_2__ da tabela __DWT\_ITENS\_SERV__\.

__Observação:__ No item da NF não permite o preenchimento das duas bases, ou seja, será preenchida uma ou outra\.

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 17 posições \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘3456789123456\.45’\.

- Se o campo <BaseCalculo> estiver com o tamanho acima do máximo permitido \(15,2 posições\)\. Exibir uma mensagem no log: “O campo <BaseCalculo> está com o tamanho acima do permitido, favor verificar”\.

Formato: 9999999999999\.99 \- Exemplo: 1\.234,56 = 1234\.56

Tamanho: 15,2 posições

Tipo: Numérico

__MFS11924__

__RN21__

__Regra para o campo <Aliquota> da TAG </Aliquota>__

Esse campo identifica a alíquota do serviço\. Preencher com o campo __ALIQ\_TRIBUTO\_ISS__ da tabela __DWT\_ITENS\_SERV __

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 3,4 \(3 inteiros/ 4 decimais\), então para atender a obrigação deverão ser desconsideradas as duas primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. *Exemplo:* 123,4567, gravar 3\.4567

__Observação: __O layout enviado pelo cliente exige o tamanho de 4,2 \(duas casas com Inteiros e duas casas decimais\)\. Porém, no exemplo do XML e arquivo XSD o formato é diferente\. Sendo assim, seguiremos com o formato do exemplo do XML\.

Tipo: Numérico

Formato: 9\.9999 – Exemplo: 1,1234= 1\.1234

Ta 

__MFS11924__

__RN22__

__Regra para o campo <ValorIss> da TAG </ValorIss>__

Esse campo identifica o valor do ISSQN\. Preencher com o somatório do campo __VLR\_TRIBUTO\_ISS__ da tabela __DWT\_ITENS\_SERV__\.

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 17 posições \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘3456789123456\.45’\.

- Se o campo <ValorIss> estiver com o tamanho acima do máximo permitido \(15,2 posições\)\. Exibir uma mensagem no log: “O campo <ValorIss> está com o tamanho acima do permitido, favor verificar”\.

Formato: 9999999999999\.99 \- Exemplo: 1\.234,56 = 1234\.56

Tamanho: 15,2 posições

Tipo: Numérico

__MFS11924__

__RN23__

__Regra para o campo <ValorLiquidoNfse> da TAG </ValorLiquidoNfse>__

Esse campo identifica o valor líquido da Nfse \(ValorServicos \- ValorPIS \-ValorCOFINS \- ValorINSS \-ValorIR \- ValorCSLL \-

OutrasRetençoes \- ValorISSRetido \- DescontoIncondicionado \- DescontoCondicionado\);

Preencher com o campo VLR\_SERVICO menos o valor de VLR\_PIS\_RETIDO \- VLR\_COFINS\_RETIDO \- VLR\_INSS\_RETIDO \- VLR\_TRIBUTO\_IR \- VLR\_CSLL \- VLR\_RET\_NF \- VLR\_RET\_SERV \- VLR\_TRIBUTO\_ISS \- VLR\_TRIBUTO\_ISS \- VLR\_DESCONTO

__\(campo 14 da SAFX09__\) da tabela DWT\_ITENS\_SERV\.

__Observação:__ Esse campo será preenchido com o somatório do valor da NFSE \(caso exista mais de um item na NFSE\)

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 17 posições \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘3456789123456\.45’\.

- Se o campo <ValorLiquidoNfse> estiver com o tamanho acima do máximo permitido \(15,2 posições\) ou não estiver preenchido\. Exibir uma mensagem no log: “O campo <ValorLiquidoNfse> não está preenchido ou está com o tamanho acima do permitido, favor verificar”\.

TAG obrigatória\.

Formato: 9999999999999\.99 \- Exemplo: 1\.234,56 = 1234\.56

Tamanho: 15,2 posições

Tipo: Numérico

__MFS11924__

__RN24__

__Regra para o campo </ValoresNfse> __Tag que identifica o fechamento do conjunto de valores que compõem o documento fiscal com o texto fixo:    __</ValoresNfse>  __TAG obrigatória

__MFS11924__

__RN25__

__Regra para o campo <ValorCredito> da TAG </ValorCredito> __

Essa TAG será gerada com o valor zerado, formato “0\.00”\.

__MFS11924__

__RN26__

__Regra para o campo <PrestadorServico> __Tag que identifica à abertura das informações do prestador de serviço com o texto fixo:   __<PrestadorServico> __

TAG obrigatória

__MFS11924__

__RN27__

__Regra para o campo <IdentificacaoPrestador> __Tag que identifica à abertura da identificação dos dados do prestador de serviço com o texto fixo:   __<IdentificacaoPrestador> __TAG obrigatória 

__MFS11924__

__RN28__

__Regra para o campo <CpfCnpj> __Tag relacionada à abertura da informação do CPF ou CNPJ do prestador de serviço com o texto fixo: __<CpfCnpj > __TAG obrigatória 

__MFS11924__

__RN29__

__Regra para o campo <Cnpj>__ __da TAG__ __<Cnpj>__

Esse campo identifica o documento do CPF ou CNPJ do Prestador\. Preencher a informação do campo CPF\_CGC __\(campo 06\)__ da tabela __X04\_PESSOA\_FIS\_JUR\.__ Deve conter 11 \(para CPF\) ou 14 \(para CNPJ\)\. 

__Observação:__ Apenas números, sem pontos, traços, espaços ou qualquer outro caracter\.

__Tratamento: __

- Se no cadastro da Pessoa Física/Jurídica o campo CPF\_CGC estiver preenchido com 14 posições gerar a TAG como <Cnpj></Cnpj> OU se estiver preenchida com 11 posições mudar para <Cpf></Cpf> no arquivo XML\.

TAG Obrigatória

Formato: 99999999999999

Tamanho: 11 / 14 posições

Tipo: Alfanumérico

__MFS11924__

__RN30__

__Regra para o campo <CpfCnpj> __Tag relacionada ao fechamento da informação do CPF ou CNPJ do prestador de serviço com o texto fixo: __</CpfCnpj> __TAG obrigatória 

__MFS11924__

__RN31__

__Regra para o campo <InscricaoMunicipal> da TAG </InscricaoMunicipal>__

Esse campo identifica o número da inscrição municipal do prestador\. Preencher a informação do campo INSC\_MUNICIPAL __\(campo 09\)__ da tabela __X04\_PESSOA\_FIS\_JUR__\.

Formato: 999999999999999 

Tamanho: 15 posições

Tipo: Numérico

__MFS11924__

__RN32__

__Regra para o campo </IdentificacaoPrestador> __Tag relacionada ao fechamento da identificação dos dados do prestador de serviço com o texto fixo:   __<IdentificacaoPrestador>__ 

TAG obrigatória 

__MFS11924__

__RN33__

__Regra para o campo <RazaoSocial> da TAG </RazaoSocial>__

Identifica a razão social do prestador do serviço\. Preencher com a informação do campo RAZAO\_SOCIAL __\(Campo 05\)__ da tabela __X04\_PESSOA\_FIS\_JUR\.__

TAG Obrigatória

Formato: XXXXXXXXXXX\.\.\./

Tamanho: 150 posições

Tipo: Alfanumérico

__MFS11924__

__RN34__

__Regra para o campo <NomeFantasia> da TAG </NomeFantasia>__

Identifica o número do endereço do prestador\. Preencher com a informação do campo NOME\_FANTASIA __\(Campo 11\)__ da tabela __X04\_PESSOA\_FIS\_JUR\.__

Formato: XXXXXXXXXX\.\.\.\./ 

Tamanho: 60 posições

Tipo: Alfanumérico

__MFS11924__

__RN35__

__Regra para o campo <Endereco> __Tag relacionada à abertura do endereço do prestador do serviço com o texto fixo:__ <Endereco> __TAG obrigatória

__MFS11924__

__RN36__

__Regra para o campo <Endereco> da TAG </Endereco>__

Identifica o tipo e o nome do logradouro do prestador\. Preencher com a informação do campo TP\_LOGRADOURO __\(Campo 42\)__ \+ ENDERECO __\(campo 12\)__ da tabela __X04\_PESSOA\_FIS\_JUR\.__

Formato: XXXXXXXX\.\.\./ 

Tamanho: 125 posições

Tipo: Alfanumérico

__MFS11924__

__RN37__

__Regra para o campo <Numero> da TAG </Numero>__

Identifica o número do endereço do prestador\. Preencher com a informação do campo NUM\_ENDERECO __\(campo 13\)__ da tabela __X04\_PESSOA\_FIS\_JUR\.__

Formato: XXXXXXXX\.\.\./ 

Tamanho: 10 posições

Tipo: Alfanumérico

__MFS11924__

__RN38__

__Regra para o campo <Complemento> da TAG </Complemento>__

Identifica o complemento do endereço do prestador\. Preencher com a informação do campo COMPL\_ENDERECO __\(campo 14\)__ da tabela __X04\_PESSOA\_FIS\_JUR\.__

Formato: XXXXXXXXXXXX\.\.\./

Tamanho: 60 posições

Tipo: Alfanumérico

__MFS11924__

__RN39__

__Regra para o campo <Bairro> da TAG </Bairro >__

Identifica o Bairro do prestador\. Preencher com a informação do campo BAIRRO __\(campo 15\)__ da tabela __X04\_PESSOA\_FIS\_JUR\.__

Formato: XXXXXXXXXXXX\.\.\./

Tamanho: 60 posições

Tipo: Alfanumérico

__MFS11924__

__RN40__

__Regra para o campo <CodigoMunicipio> da TAG </CodigoMunicipio__

Identifica o código do município do prestador conforme IBGE\. Preencher com a concatenação do Código UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do município \(COD\_MUNICIPIO da tabela MUNICIPIO\), referente ao campo COD\_MUNICIPIO da tabela SAFX04\.

__Observação: __Apenas números, sem pontos, traços, espaços ou qualquer outro Caracter\.

Formato: 9999999 

Tamanho: 7 posições

Tipo: Numérico

__MFS11924__

__RN41__

__Regra para o campo <Uf> da TAG </Uf>__

Identifica a sigla da unidade federativa do prestador\. Preencher com a informação do campo UF __\(campo 19\)__ da tabela __X04\_PESSOA\_FIS\_JUR__\.

Formato: XX 

Tamanho: 2 posições

Tipo: Alfanumérico

__MFS11924__

__RN42__

__Regra para o campo <Cep> da TAG </Cep>__

Identifica o CEP da localidade do prestador\. Preencher com a informação do campo CEP __\(campo 20\)__ da tabela __X04\_PESSOA\_FIS\_JUR__

Formato: 99999999

Tamanho: 8 posições

Tipo: Numérico

__MFS11924__

__RN43__

__Regra para o campo </Endereco> __Tag relacionada ao fechamento do endereço do prestador do serviço com o texto fixo: __</Endereco>__ TAG obrigatória

__MFS11924__

__RN44__

__Regra para o campo <Contato> __Tag relacionada à abertura do contato da pessoa \(físico\-jurídica\) com o texto fixo:__ <Contato> __

__MFS11924__

__RN45__

__Regra para o campo <Telefone> da TAG </Telefone>__

Identifica o Telefone do Prestador do serviço\. Preencher com a informação do campo DDD __\(campo 22\) \+__ TELEFONE __\(campo 23\)__ da tabela __X04\_PESSOA\_FIS\_JUR__\.

Formato: XXXXXXXXX\.\./ 

Tamanho: 20 posições

Tipo: Alfanumérico

__MFS11924__

__RN46__

__Regra para o campo <Email> da TAG </Email>__

Identifica o email do prestador\. Preencher com a informação do campo E\_MAIL __\(campo 40\)__ da tabela __X04\_PESSOA\_FIS\_JUR__\.

Formato: XXXXXXXXXXXX\.\.\./ 

Tamanho: 80 posições

Tipo: Alfanumérico

__MFS11924__

__RN47__

__Regra para o campo </Contato> __Tag relacionada ao fechamento do contato da pessoa \(físico\-jurídica\) com o texto fixo:__ </Contato> __

__MFS11924__

__RN48__

__Regra para o campo </PrestadorServico> __Tag relacionada ao fechamento das informações do prestador de serviço com o texto fixo:__ </PrestadorServico> __TAG obrigatória

__MFS11924__

__RN49__

__Regra para o campo <OrgaoGerador> __Tag relacionada à abertura dos dados para identificação do órgão gerador com o texto fixo:__ <OrgaoGerador> __TAG obrigatória

__MFS11924__

__RN50__

__Regra para o campo <CodigoMunicipio> da TAG </CodigoMunicipio__

Identifica o código do município do prestador conforme IBGE\. Preencher com a concatenação do Código UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do município \(COD\_MUNICIPIO da tabela MUNICIPIO\), referente ao campo COD\_MUNICIPIO da tabela SAFX04\.

__Observação: __Apenas números, sem pontos, traços, espaços ou qualquer outro Caracter\.

__Tratamento: __

- Se o campo <CodigoMunicipio> não estiver preenchido\. Exibir uma mensagem no log: “O campo <CodigoMunicipio> não está preenchido, favor verificar”\.

TAG Obrigatória

Formato: 9999999 

Tamanho: 7 posições

Tipo: Numérico

__MFS11924__

__RN51__

__Regra para o campo <Uf> da TAG </Uf>__

Identifica a sigla da unidade federativa do prestador\. Preencher com a informação do campo UF __\(campo 19\)__ da tabela __X04\_PESSOA\_FIS\_JUR__\.

Formato: XX 

Tamanho: 2 posições

Tipo: Alfanumérico

__MFS11924__

__RN52__

__Regra para o campo </OrgaoGerador> __Tag relacionada ao encerramento dos dados para identificação do órgão gerador com o texto fixo:__ </OrgaoGerador> __TAG obrigatória

__RN53__

__Regra para o campo <DeclaracaoPrestacaoServico> __Tag relacionada à abertura da estrutura da declaração da prestação do serviço  com o texto fixo: __<DeclaracaoPrestacaoServico> __TAG obrigatória\.

__MFS11924__

__RN54__

__Regra para o campo <InfDeclaracaoPrestacaoServico id = __“ ”__> __ Essa TAG será preenchida com o valor: ‘nulo’\. 

__MFS11924__

__RN55__

__Regra para o campo <Competencia> da TAG </Competencia>__

Identifica o ano e mês da competência\. Esse campo será preenchido com o primeiro dia da competência que o serviço foi prestado\.

Exemplo: Serviço Prestado dia 24/08/2017 a Tag virá preenchida com 2017\-08\-01\.

TAG Obrigatória\.

Formato: AAAA\-MM\-DD Exemplo: 2017\-08\-09

Tamanho: 10 posições

Tipo: Data

__MFS11924__

__RN56__

__Regra para o campo <Servico> __Tag relacionada à abertura do serviço com o texto fixo:__ <Servico> __TAG obrigatória

__MFS11924__

__RN57__

__Regra para o campo <Valores> __Tag relacionada à abertura do conjunto de valores que compõe a NFS\-e com o texto fixo:__ </Valores> __TAG obrigatória

__MFS11924__

__RN58__

__Regra para o campo <ValorServicos> da TAG </ValorServicos>__

Preencher com o somatório do campo __VLR\_SERVICO__ da tabela DWT\_ITENS\_SERV __\(Campo 14 da SAFX09\)\.__

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 17 posições \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘3456789123456\.45’\.

- Se o campo <ValorServicos> estiver com o tamanho acima do máximo permitido \(15,2 posições\) ou não estiver preenchido\. Exibir uma mensagem no log: “O campo <ValorServicos> não está preenchido ou está com o tamanho acima do permitido, favor verificar”\.

TAG obrigatória\.

Formato: 9999999999999\.99 \- Exemplo: 1\.234,56 = 1234\.56

Tamanho: 15,2 posições

Tipo: Numérico

__MFS11924__

__RN59__

__Regra para o campo <ValorDeducoes> da TAG </ValorDeducoes>__

Preencher com o somatório do campo __VLR\_DEDUCAO\_ISS __da tabela DWT\_ITENS\_SERV __\(Campo 59 da SAFX09\)\.__

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 17 posições \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘3456789123456\.45’\.

- Se o campo <ValorDeducoes> estiver com o tamanho acima do máximo permitido \(15,2 posições\), exibir uma mensagem no log: “O campo <ValorDeducoes> está com o tamanho acima do permitido, favor verificar”\.
- Se o campo não possuir valor, preencher com zeros, conforme exemplo do XML\.

Formato: 9999999999999\.99 \- Exemplo: 1\.234,56 = 1234\.56

Tamanho: 15,2 posições

Tipo: Numérico

__MFS11924__

__RN60__

__Regra para o campo <ValorPis> da TAG </ValorPis>__

Preencher com o somatório do campo __VLR\_PIS\_RETIDO__ da tabela DWT\_ITENS\_SERV\. __\(Campo 79 da SAFX09\)\.__

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 17 posições \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘3456789123456\.45’\.

- Se o campo <ValorPis> estiver com o tamanho acima do máximo permitido \(15,2 posições\), exibir uma mensagem no log: “O campo <ValorPis> está com o tamanho acima do permitido, favor verificar”\.
- Se o campo não possuir valor, preencher com zeros, conforme exemplo do layout\.

Formato: 9999999999999\.99 \- Exemplo: 1\.234,56 = 1234\.56

Tamanho: 15,2 posições

Tipo: Numérico

__MFS11924__

__RN61__

__Regra para o campo <ValorCofins> da TAG </ValorCofins>__

Preencher com o somatório do campo __VLR\_COFINS\_RETIDO__ da tabela DWT\_ITENS\_SERV __\(Campo 80 da SAFX09\)\.__

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 17 posições \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘3456789123456\.45’\.

- Se o campo <ValorCofins> estiver com o tamanho acima do máximo permitido \(15,2 posições\), exibir uma mensagem no log: “O campo <ValorCofins> está com o tamanho acima do permitido, favor verificar”\.
- Se o campo não possuir valor, preencher com zeros, conforme exemplo do XML\.

 

Formato: 9999999999999\.99 \- Exemplo: 1\.234,56 = 1234\.56

Tamanho: 15,2 posições

Tipo: Numérico

__MFS11924__

__RN62__

__Regra para o campo <ValorInss> da TAG </ValorInss>__

Preencher com o somatório do campo __VLR\_INSS\_RETIDO__ da tabela DWT\_ITENS\_SERV __\(Campo 77 da SAFX09\)\.__

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 17 posições \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘3456789123456\.45’\.

- Se o campo <ValorInss> estiver com o tamanho acima do máximo permitido \(15,2 posições\), exibir uma mensagem no log: “O campo <ValorCofins> está com o tamanho acima do permitido, favor verificar”\.
- Se o campo não possuir valor, preencher com zeros, conforme exemplo do XML\.

Formato: 9999999999999\.99 \- Exemplo: 1\.234,56 = 1234\.56

Tamanho: 15,2 posições

Tipo: Numérico

__MFS11924__

__RN63__

__Regra para o campo <ValorIr> da TAG </ValorIr>__

Preencher com o somatório do campo __VLR\_TRIBUTO\_IR__ da tabela DWT\_ITENS\_SERV 

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 17 posições \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘3456789123456\.45’\.

- Se o campo <ValorIr> estiver com o tamanho acima do máximo permitido \(15,2 posições\), exibir uma mensagem no log: “O campo <ValorIr> está com o tamanho acima do permitido, favor verificar”\.
- Se o campo não possuir valor, preencher com zeros, conforme exemplo do XML\.

Formato: 9999999999999\.99 \- Exemplo: 1\.234,56 = 1234\.56

Tamanho: 15,2 posições

Tipo: Numérico

__MFS11924__

__RN64__

__Regra para o campo <ValorCsll> da TAG </ValorCsll>__

Preencher com o somatório do campo __VLR\_CSLL__ da tabela DWT\_ITENS\_SERV __\(Campo 45 da SAFX09\)__

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 17 posições \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘3456789123456\.45’\.

- Se o campo <ValorCsll> estiver com o tamanho acima do máximo permitido \(15,2 posições\), exibir uma mensagem no log: “O campo <ValorCsll> está com o tamanho acima do permitido, favor verificar”\.
- Se o campo não possuir valor, preencher com zeros, conforme exemplo do XML\.

Formato: 9999999999999\.99 \- Exemplo: 1\.234,56 = 1234\.56

Tamanho: 15,2 posições

Tipo: Numérico

__MFS11924__

__RN65__

__Regra para o campo <OutrasRetencoes> da TAG </OutrasRetencoes>__

Preencher com o somatório dos campos __VLR\_RET\_NF , VLR\_RET\_SERV__ da tabela DWT\_ITENS\_SERV __\(Campo 95 e 96 da SAFX09\)__,

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 17 posições \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser desconsideradas as primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘3456789123456\.45’\.

- Se o campo <OutrasRetencoes> estiver com o tamanho acima do máximo permitido \(15,2 posições\), exibir uma mensagem no log: “O campo <OutrasRetencoes> está com o tamanho acima do permitido, favor verificar”\.
- Se o campo não possuir valor, preencher com zeros, conforme exemplo do XML\.

Formato: 9999999999999\.99 \- Exemplo: 1\.234,56 = 1234\.56

Tamanho: 15,2 posições

Tipo: Numérico

__MFS11924__

__RN66__

__Regra para o campo <ValorIss> da TAG </ValorIss>__

Esse campo identifica o valor do ISSQN\. Preencher com o campo __VLR\_TRIBUTO\_ISS__ da tabela __DWT\_ITENS\_SERV__\.

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 17 posições \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser consideradas as posições do número conforme nossa tabela para atender a Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘123456789123456__\.__45’\.

- Se o campo <ValorIss> estiver com o tamanho acima do máximo permitido \(15,2 posições\), exibir uma mensagem no log: “O campo <ValorIss> está com o tamanho acima do permitido, favor verificar”\.
- Se o campo não possuir valor, preencher com zeros, conforme exemplo do XML\.

Formato: 9999999999999\.99 \- Exemplo: 1\.234,56 = 1234\.56

Tamanho: 15,2 posições

Tipo: Numérico

__MFS11924__

__RN67__

__Regra para o campo <Aliquota> da TAG </Aliquota>__

Esse campo identifica a alíquota do serviço\. Preencher com o campo __ALIQ\_TRIBUTO\_ISS__ da tabela __DWT\_ITENS\_SERV __

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 3,4 \(3 inteiros/ 4 decimais\), então para atender a obrigação deverão ser desconsideradas as duas primeiras posições do número inteiro para atender o tamanho exigido pela Prefeitura\. *Exemplo:* 123,4567, gravar 3\.4567

__Observação: __O layout enviado pelo cliente exige o tamanho de 4,2 \(duas casas com Inteiros e duas casas decimais\)\. Porém, no exemplo do XML e arquivo XSD o formato é diferente\. Sendo assim, seguiremos com o formato do exemplo do XML\.

Tipo: Numérico

Formato: 9\.9999 – Exemplo: 1,1234= 1\.1234

Tamanho: 1,5

Ta  

__MFS11924__

__RN68__

__Regra para o campo <DescontoIncondicionado> da TAG </DescontoInondicionado>__

Preencher com o somatório do campo __VLR\_DESCONTO __da tabela DWT\_ITENS\_SERV __\(Campo 21 da SAFX09\)__

__Tratamento:__

- Nossa tabela permite gravar no tamanho de 17 posições \(15 inteiros/ 2 decimais\), então para atender a obrigação deverão ser consideradas as posições do número conforme nossa tabela para atender a Prefeitura\. 

*             Exemplo:* Para o valor de 123456789123456,45 deverá ser informado ‘123456789123456__\.__45’\.

- Se o campo <DescontoIncondicionado> estiver com o tamanho acima do máximo permitido \(15,2 posições\), exibir uma mensagem no log: “O campo <DescontoIncondicionado> está com o tamanho acima do permitido, favor verificar”\.
- Se o campo não possuir valor, preencher com zeros, conforme exemplo do XML\.

Formato: 9999999999999\.99 \- Exemplo: 1\.234,56 = 1234\.56

Tamanho: 15,2 posições

Tipo: Numérico

__MFS11924__

__RN69__

__Regra para o campo <DescontoCondicionado> da TAG </DescontoCondicionado>__

Essa TAG será preenchida com zeros\. Nas obrigações municipais não geramos esse campo\.

Preencher no formato “0\.00” conforme exemplo do XML

__MFS11924__

__RN70__

__Regra para o campo <Valores> __Tag relacionada ao encerramento do conjunto de valores que compõe a NFS\-e com o texto fixo:__ </Valores> __TAG obrigatória

__MFS11924__

__RN71__

__Regra para o campo <IssRetido> da TAG </IssRetido>__

Identifica se o ISS foi retido ou não\.

Verificar o local da prestação do serviço \(campo COD\_MUNIC da tabela DWT\_DOCTO\_FISCAL\)\. Se o mesmo não estiver preenchido, recuperar o município do estabelecimento \(campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\)\.

Preencher com:

__“1” \- Sim\.__

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “1" e se o local da prestação do serviço = município do módulo selecionado __OU __
- Se na tabela X2098\_ALIQ\_SERVICO, o campo IND\_TOM\_TRIBUT\_ISS = “S” para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO e se o local da prestação do serviço = município do módulo selecionado __OU__
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV estiver preenchido e se o local da prestação do serviço = município do módulo selecionado\.

Senão, preencher com:

__“2” \- Não\.__

TAG obrigatória

Formato: 9 \(1\-Sim ou 2\-Não\)

Tipo: Numérico

Tamanho: 1

__MFS11924__

__RN72__

__Regra para o campo <ItemListaServico> da TAG </ItemListaServico>__

Identifica o Grupo do Código de Atividade do Serviço\. 

Preencher com o conteúdo do campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal\.

__Tratamento:__

Se o código de serviço da lei 116 não estiver cadastrado na SAFX2018, deverá ser gravado com 00\.00 \(zeros\) e emitida a mensagem de log: O código da Lei 116 no cadastro do serviço para o serviço informado na nota fiscal não está preenchido, favor verificar\.

TAG obrigatória

Formato: 99\.99

Tipo: Numérico

Tamanho: 5

__MFS11924__

__RN73__

__Regra para o campo <CodigoCnae> da TAG </CodigoCnae>__

Esse campo identifica o código atividade econômica\. Preencher a informação do campo COD\_ATIVIDADE __\(campo 07\) __da tabela __X04\_PESSOA\_FIS\_JUR\.__

Formato: 9999999 

Tamanho: 7 posições

Tipo: Numérico

__MFS11924__

__RN74__

__Regra para o campo <CodigoTributacaoMunicipio> da TAG </CodigoTributacaoMunicipio> __

Identifica o Grupo do Código de Atividade do Serviço\. 

Preencher com o conteúdo do campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal\.

__Tratamento:__

Se o código de serviço da lei 116 não estiver cadastrado na SAFX2018, deverá ser gravado com 0000 \(zeros\) e emitida a mensagem de log: O código da Lei 116 no cadastro do serviço para o serviço informado na nota fiscal não está preenchido, favor verificar\.

Formato: 9999

Tipo: Numérico

Tamanho: 4

__MFS11924__

__RN75__

__Regra para o campo <Discriminacao> da TAG </Discriminacao> __

Preencher com o campo DSC\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao\(s\) serviço\(s\) cadastrado\(s\) no item da nota fiscal\.

TAG Obrigatória

Formato: XXXXXXXXXXXXXXXXXX\(\.\.\.\)

Tamanho: 2000 posições \- É permitida a quebra de linha para este campo\.

Tipo: Alfanumérico

__MFS11924__

__RN76__

__Regra para o campo <CodigoMunicipio> da TAG </CodigoMunicipio> __

Identifica o código do município do prestador conforme IBGE\. Preencher com a concatenação do Código UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do município \(COD\_MUNICIPIO da tabela MUNICIPIO\), referente ao campo COD\_MUNICIPIO da tabela SAFX04\.

__Observação: __Apenas números, sem pontos, traços, espaços ou qualquer outro Caracter\.

TAG Obrigatória

Formato: 9999999 

Tamanho: 7 posições

Tipo: Numérico

__MFS11924__

__RN77__

__Regra para o campo <ExigibilidadeISS> da TAG </ExigibilidadeISS> __

Identifica a exigência da tributação do ISS da prestação do serviço\. 

Preencher com:

__“2” \- Não Incidência\.__

Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “432” no módulo: Parâmetros para Município\.

__“3” \- Isenção\.__

Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “10”; __OU__

Se não estiver preenchido, verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “433” no módulo: Parâmetros para Município\.

__“4” \- Exportação\.__

Se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “520” no módulo: Parâmetros para Município\.

__“5” \- Imunidade\.__

Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “07”; __OU__

Se não estiver preenchido, verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “420” no módulo: Parâmetros para Município\.

__“6” \- Exigibilidade Suspensa por Decisão Judicial\.__

Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “09”; __OU__

Se não estiver preenchido, verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estão parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “427” no módulo: Parâmetros para Município\.

__“7” \- Exigibilidade Suspensa por Processo Administrativo\.__

Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “11”; __OU__

Se não estiver preenchido, verificar se o serviço e o município do prestador \(Pessoa Fis/Jur\) cadastrados na nota estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “485” no módulo: Parâmetros para Município\.

Se nenhuma das opções anteriores for verdadeira, preencher com:

__“1” \- Exigível\.__

TAG Obrigatória

Formato: 9

Tipo: Numérico

Tamanho: 1

__MFS11924__

__RN78__

__Regra para o campo <MunicipioIncidencia> da TAG </ MunicipioIncidencia > __

Identifica o código do município do prestador conforme IBGE\. Preencher com a concatenação do Código UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do município \(COD\_MUNICIPIO da tabela MUNICIPIO\), referente ao campo COD\_MUNICIPIO da tabela SAFX07\.

__Observação: __Apenas números, sem pontos, traços, espaços ou qualquer outro Caracter\.

Formato: 9999999 

Tamanho: 7 posições

Tipo: Numérico

__MFS11924__

__RN79__

__Regra para o campo </Servico> __Tag relacionada ao encerramento do serviço com o texto fixo:__ </Servico> __TAG obrigatória

__MFS11924__

__RN80__

__Regra para o campo <Prestador> __Tag relacionada à abertura dos dados de identificação do prestador com o texto fixo:__ <Prestador> __TAG obrigatória

__MFS11924__

__RN81__

__Regra para o campo <CpfCnpj> __Tag relacionada à abertura da informação do CPF ou CNPJ do prestador de serviço com o texto fixo:__ <CpfCnpj>  __TAG obrigatória\.

__MFS11924__

__RN82__

__Regra para o campo <Cnpj> da TAG <Cnpj>__

Esse campo identifica o documento do CPF ou CNPJ do Prestador\. Preencher a informação do campo CPF\_CGC __\(campo 06\)__ da tabela __X04\_PESSOA\_FIS\_JUR\.__ Deve conter 11 \(para CPF\) ou 14 \(para CNPJ\)\. 

__Observação:__ Apenas números, sem pontos, traços, espaços ou qualquer outro caracter\.

__Tratamento: __

- Se no cadastro da Pessoa Física/Jurídica o campo CPF\_CGC estiver preenchido com 14 posições gerar a TAG como <Cnpj></Cnpj> OU se estiver preenchida com 11 posições mudar para <Cpf></Cpf> no arquivo XML\.

TAG Obrigatória

Formato: 99999999999999

Tamanho: 11 / 14 posições

Tipo: Alfanumérico

__MFS11924__

__RN83__

__Regra para o campo </CpfCnpj> __Tag relacionada ao fechamento da informação do CPF ou CNPJ do prestador de serviço fixo:__ </CpfCnpj>  __TAG obrigatória\.

__MFS11924__

__RN84__

__Regra para o campo <InscricaoMunicipal> da TAG </InscricaoMunicipal>__

Esse campo identifica o número da inscrição municipal do prestador\. Preencher a informação do campo INSC\_MUNICIPAL __\(campo 09\)__ da tabela __X04\_PESSOA\_FIS\_JUR__\.

Formato: 999999999999999 

Tamanho: 15 posições

Tipo: Numérico

__MFS11924__

__RN85__

__Regra para o campo </Prestador> __Tag relacionada ao encerramento dos dados de identificação do prestador com o texto fixo:__ </Prestador> __TAG obrigatória

__MFS11924__

__RN86__

__Regra para o campo <Tomador> __Tag relacionada à abertura dos dados de identificação do tomador com o texto fixo:__ <Tomador> __TAG obrigatória

__MFS11924__

__RN87__

__Regra para o campo <IdentificacaoTomador> __Tag relacionada à abertura da identificação do Tomador com o texto fixo:__ <IdentificacaoTomador > __TAG obrigatória

__MFS11924__

__RN88__

__Regra para o campo <CpfCnpj> __Tag relacionada à abertura da informação do CPF ou CNPJ do Tomador de serviço fixo:__ <CpfCnpj>  __TAG obrigatória\.

__MFS11924__

__RN89__

__Regra para o campo <Cnpj> da TAG <Cnpj>__

Esse campo identifica o documento do CPF ou CNPJ do Prestador\. Preencher a informação do campo CPF\_CGC __\(campo 06\)__ da tabela __ESTABELECIMENTO\.__ Deve conter 11 \(para CPF\) ou 14 \(para CNPJ\)\. 

__Observação:__ Apenas números, sem pontos, traços, espaços ou qualquer outro caracter\.

TAG Obrigatória

Formato: 99999999999999

Tamanho: 11 / 14 posições

Tipo: Alfanumérico

__MFS11924__

__RN90__

__Regra para o campo </CpfCnpj> __Tag relacionada ao fechamento da informação do CPF ou CNPJ do Tomador de serviço fixo:__ </CpfCnpj>  __TAG obrigatória\.

__MFS11924__

__RN91__

__Regra para o campo <InscricaoMunicipal> da TAG </InscricaoMunicipal>__

Esse campo identifica o número da inscrição municipal do prestador\. Preencher a informação do campo __INSC\_MUNICIPAL__ da tabela __ESTABELECIMENTO__

Formato: 999999999999999 

Tamanho: 15 posições

Tipo: Numérico

__MFS11924__

__RN92__

__Regra para o campo <IdentificacaoTomador> __Tag relacionada ao fechamento da identificação do Tomador com o texto fixo:__ <IdentificacaoTomador > __TAG obrigatória

__RN93__

__Regra para o campo <RazaoSocial> da TAG </RazaoSocial> __

Identifica a razão social do Contribuinte\. Preencher com o campo __RAZAO\_SOCIAL__ da tabela __ESTABELECIMENTO__

Formato: XXXXXXXXXXXXXXX\.\.\./

Tamanho: 150

Tipo: Alfanumérico

__MFS11924__

__RN94__

__Regra para o campo <Endereco> __Tag relacionada à abertura dos dados de endereço do tomador com o texto fixo:__ <Endereco> __TAG obrigatória

__MFS11924__

__RN95__

__Regra para o campo <Endereco> da TAG </Endereco> __

Identifica o tipo e nome do logradouro do Tomador\. Preencher com o campo __TP__\___LOGRADOURO__ __\+__ __ENDERECO__ da tabela __ESTABELECIMENTO__

Formato: XXXXXXXXXXXXXXX\.\.\./

Tamanho: 125

Tipo: Alfanumérico

__MFS11924__

__RN96__

__Regra para o campo <Numero> da TAG </Numero> __

Identifica o número do endereço do Tomador\. Preencher com o campo __NUM\_ENDERECO__ da tabela __ESTABELECIMENTO__

Formato: XXXXXXXXXX

Tamanho: 10

Tipo: Alfanumérico

__MFS11924__

__RN97__

__Regra para o campo <Complemento> da TAG </Complemento> __

Identifica o complemento do endereço do Tomador\. Preencher com o campo __COMPL\_ENDERECO__ da tabela __ESTABELECIMENTO__

Formato: XXXXXXXXXXXXXXX\.\.\./

Tamanho: 60

Tipo: Alfanumérico

__MFS11924__

__RN98__

__Regra para o campo <Bairro> da TAG </Bairro> __

Identifica o nome do Bairro do Tomador\. Preencher com o campo __BAIRRO__ da tabela __ESTABELECIMENTO__

Formato: XXXXXXXXXXXXXXX\.\.\./

Tamanho: 60

Tipo: Alfanumérico

__MFS11924__

__RN99__

__Regra para o campo <CodigoMunicipio> da TAG </CodigoMunicipio> __

Identifica o Código do Município \(IBGE\) do Tomador\. Preencher com a concatenação do Código UF \(campo COD\_UF da tabela MUNICIPIO\) \+ Código do Município \(COD\_MUNICIPIO da tabela MUNICIPIO\), referente ao campo COD\_MUNICIPIO da tabela ESTABELECIMENTO

Formato: 9999999

Tamanho: 7

Tipo: Numérico

__MFS11924__

__RN100__

__Regra para o campo <Uf> da TAG </Uf> __

Identifica a sigla do estado do tomador\. Preencher com o campo __UF __da tabela __ESTABELECIMENTO__

Formato: XX

Tamanho: 2

Tipo: Alfanumérico

__MFS11924__

__RN101__

__Regra para o campo <Cep> da TAG </Cep> __

Identifica o Cep do tomador\. Preencher com o campo __CEP__ da tabela __ESTABELECIMENTO__

Formato: 99999999

Tamanho: 8

Tipo: Numérico

__MFS11924__

__RN102__

__Regra para o campo </Endereco> __Tag relacionada ao encerramento dos dados de endereço do tomador com o texto fixo:__ </Endereco> __TAG obrigatória

__MFS11924__

__RN103__

__Regra para o campo <Contato> __Tag relacionada à abertura dos dados de contato do tomador com o texto fixo:__ </Contato> __

__MFS11924__

__RN104__

__Regra para o campo <Email> da TAG </Email> __

Identifica o Email do tomador\. Preencher com o campo __EMAIL__ da tabela __ESTABELECIMENTO__

Formato: XXXXXXXXXXXXX\.\./

Tamanho: 80

Tipo: Alfanumérico

__MFS11924__

__RN105__

__Regra para o campo <Telefone> da TAG </Telefone> __

Identifica o Telefone do Prestador do serviço\. Preencher com a informação do campo DDD __\+__ TELEFONE da tabela __ESTABELECIMENTO__\.

Formato: XXXXXXXXX\.\./ 

Tamanho: 20 posições

Tipo: Alfanumérico

__MFS11924__

__RN106__

__Regra para o campo </Contato> __Tag relacionada ao encerramento dos dados de contato do tomador com o texto fixo:__ </Contato> __

__MFS11924__

__RN107__

__Regra para o campo </Tomador> __Tag relacionada ao fechamento dos dados de identificação do tomador com o texto fixo:__ </Tomador> __TAG obrigatória\.

__MFS11924__

__RN108__

__Regra para o campo <RegimeEspecialTributacao> da TAG </RegimeEspecialTributacao> __

Esse campo identifica o regime especial de tributação\. 

Preencher com:

__“1” \- Microempresa municipal\.__

Se o campo IND\_CLASSE\_EMP da tabela X04\_PESSOA\_FIS\_JUR \(campo 27 da SAFX04\) = “04 – Microempresa \(ME\)” referente o prestador cadastrado na nota fiscal\.

__“2” \- Estimativa\.__

Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “08 \- Regime de Estimativa” referente o prestador cadastrado na nota fiscal\.

__“3” \- Sociedade de Profissionais\.__

Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “06 \- Sociedade Profissional” referente o prestador cadastrado na nota fiscal\.

__“4” \- Cooperativa\.__

Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “02 \- Cooperativa” OU “05 \- Cooperativa de Transporte” referente o prestador cadastrado na nota fiscal\.

__“5” \- Microempresário Individual \(MEI\)\.__

Se o campo IND\_CLASSE\_EMP da tabela X04\_PESSOA\_FIS\_JUR \(campo 27 da SAFX04\) = “05 – MEI \(Micro Empreendedor Individual\)” referente o prestador cadastrado na nota fiscal\.

__“6” \- Microempresário e Empresa de Pequeno Porte \(ME EPP\)\.__

Se o campo IND\_CLASSE\_EMP da tabela X04\_PESSOA\_FIS\_JUR \(campo 27 da SAFX04\) = “01 \- EPP \(Empresa de Pequeno Porte\)” referente o prestador cadastrado na nota fiscal\.

Formato: 9

Tamanho: 1

Tipo: Numérico

__MFS11924__

__RN109__

__Regra para o campo <OptanteSimplesNacional> da TAG </OptanteSimplesNacional>__

Esse campo identifica se o prestador é optante do Simples Nacional\. 

Preencher com:

__“1” \- Sim\.__

Se o campo __IND\_SIMPLES\_NAC__ da tabela X04\_PESSOA\_FIS\_JUR __\(campo 43 da SAFX04\)__ for igual “S” referente o prestador cadastrado na nota fiscal\.

Senão, preencher com:

__“2” \- Não\.__

TAG obrigatória\.

Formato: 9

Tamanho: 1

Tipo: Numérico

__MFS11924__

__RN110__

__Regra para o campo <IncentivoFiscal> da TAG </IncentivoFiscal>__

Esse campo identifica se o prestador possui incentivo fiscal\. 

Se o campo __IND\_INCENTIVO\_CULTURAL__ da tabela __X04\_PESSOA\_FIS\_JUR =__ marcado, preencher com a opção __‘1’ \(Sim\),__

Senão preencher com__ ‘2’ \(Não\)\.__

TAG obrigatória\.

Formato: 9

Tamanho: 1

Tipo: Numérico

__MFS11924__

__RN111__

__Regra para o campo </InfDeclaracaoPrestacaoServico> __Tag relacionada ao encerramento das informações declaração da prestação de serviços com o texto fixo:__ </InfDeclaracaoPrestacaoServico>  __TAG obrigatória\.

__MFS11924__

__RN112__

__Regra para o campo </DeclaracaoPrestacaoServico> __Tag relacionada ao encerramento da declaração da prestação de serviços com o texto fixo:__ </DeclaracaoPrestacaoServico>  __TAG obrigatória\.

__MFS11924__

__RN113__

__Regra para o campo </InfNfse> __Tag relacionada ao encerramento das informações da nota fiscal de serviço eletrônica com o texto fixo:__ </InfNfse>  __TAG obrigatória\.

__MFS11924__

__RN114__

__Regra para o campo </Nfse> __Tag relacionada ao encerramento da nota fiscal de serviço eletrônica com o texto fixo:__ </Nfse> __TAG obrigatória\.

__MFS11924__

__RN115__

__Regra para o campo </CompNfse> __Tag relacionada ao encerramento da estrutura de compartilhamento de dados de uma NFS\-e com o texto fixo:__ </CompNfse>  __TAG obrigatória\.

__MFS11924__

__RN116__

__Regra para o campo </ListaNfse> __Tag relacionada ao encerramento da lista das notas fiscais com o texto fixo:__ </ListaNfse> __

TAG obrigatória\.

__MFS11924__

__RN117__

__Regra para o campo </ConsultarNfseServicoPrestadoResposta> __Tag relacionada ao encerramento da chamada dos serviço da resposta do serviço com o texto fixo:__ </ConsultarNfseServicoPrestadoResposta> __TAG obrigatória\.

__MFS11924__

__RN118__

__Regra p/ inclusão do módulo no Manager – Pirajuí:__

O módulo “Pirajuí” deve ficar localizado no grupo “Municipal”\.

Descrição do módulo:__ “Consiste no envio e processamento da declaração mensal das notas fiscais de serviços eletrônica tomados do município de Pirajuí”\.__

__MFS31709__

__RN119__

__Regra p/ abertura do módulo no Manager – Pirajuí:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “38907” \(Pirajuí\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Pirajuí, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS31709__

__RN120__

__Regra p/ inclusão do módulo no Manager – Água Boa:__

O módulo “Água Boa” deve ficar localizado no grupo “Municipal”\.

Descrição do módulo: “Consiste no envio e processamento da declaração mensal das notas fiscais de serviços eletrônica tomados do município de Água Boa”\.

__MFS31775__

__RN121__

__Regra p/ abertura do módulo no Manager – Água Boa:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “MT” e ao código de município do IBGE igual a “201” \(Água Boa\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Água Boa, Mato Grosso\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS31775__

__RN122__

__Regra p/ inclusão do módulo no Manager – Ponta Grossa:__

__O módulo “Ponta Grossa” deve ficar localizado no grupo “Municipal”\.__

__Descrição do módulo: “Consiste no envio e processamento da declaração mensal das notas fiscais de serviços eletrônica tomados do município de Ponta Grossa”\.__

__MFS31767__

__RN123__

__Regra p/ abertura do módulo no Manager – Ponta Grossa:__

__Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “PR” e ao código de município do IBGE igual a “201” \(Ponta Grossa\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:__

__“Este estabelecimento não pertence ao município de Ponta Grossa, Paraná\. Alguns dados não estarão disponíveis\. Deseja continuar?”__

__Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.__

__MFS31767__

__RN124__

__Regra p/ inclusão do módulo no Manager – Andirá:__

O módulo “Andirá” deve ficar localizado no grupo “Municipal”\.

Descrição do módulo: “Consiste no envio e processamento da declaração mensal das notas fiscais de serviços eletrônica tomados do município de Andirá”\.

__MFS29822__

__RN125__

__Regra p/ abertura do módulo no Manager – Andirá:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “PR” e ao código de município do IBGE igual a “1101” \(Andirá\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Andirá, Paraná\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS29822__

__RN126__

__Regra p/ inclusão do módulo no Manager – José Bonifácio:__

O módulo “José Bonifácio” deve ficar localizado no grupo “Municipal”\.

Descrição do módulo: “Consiste no envio e processamento da declaração mensal das notas fiscais de serviços eletrônica tomados do município de José Bonifácio”\.

__MFS40578__

__RN127__

__Regra p/ abertura do módulo no Manager – José Bonifácio:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “SP” e ao código de município do IBGE igual a “25706” \(José Bonifácio\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de José Bonifácio, São Paulo\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\. O botão “Não” é default\.

__MFS40578__

