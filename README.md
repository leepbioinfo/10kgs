10k genome
================
- [ ] Cotar os substratos de GFP das fosfolipases. 
- [ ] Protocolo de extração de lipodeos e massa.
- [ ] Falar com o perere do Dock
- [ ] Aonde fazer o serviço de GC-MSMS
- [ ] Acabar as analises de 10kg (Grupos de vizinhos, candidatos de tox, C-terminais, Analises dos candidatos em banco de dados abertos)
- [ ] Se vamos ou não pedir o plasmideos com o controle positivo do paper das phospholipases de Vibrio.
### Para o dia 03/01/2022 
- [ ] Tabela com as toxinas por tipo de sistema classificado
- [ ] Calssificação dos tipos de T6SS incluindo comparação com o que sabe (paper Bao.)


## Work folders

|                 Subject                  | work directory |                          observatio                          |
|:----------------------------------------:|:--------------:|:------------------------------------------------------------:|
|   Bastion HMM models agains merged2db    |    20210209    |                    Models from BastionHMM                    | 
|          First data inspection           |    20210805    |                          source.py                           |
|        Cluster of T6SS neighbors         |    20210805    |                          source2.py                          |
|             Jaccard distance             |    20210805    |                          source3.py                          |
|          New_tox model creation          |    20210805    |            source4.py and putative new tox folder            |
|         Add new tox to the data          |    20210818    |                              -                               |
| Search for tox in unknow region all data |    20210819    |                              -                               |
| Firs anaylysis with Moreira data         |    20210827    |                                                              |
|   Tabela enviada por email para Ethel    |    work dir    |         ./analise_grande  variavel selected correto          |
| Análise dos genomas do paper do Bao      |    20210901    |      Analise inicial usando apenas modelos de HMM            |
| Nova analise dos 10k com alguns ajustes  |    20210929    |             ajustes da analise para ser a final              |
|    Busca por efetores em P.aruginosa     |    20211001    | Avaliando se o pipeline pode ser usado para outras bacterias |
|        Arvore proteinas do T6SS          |    20211207    |   árvore de todos os componentes baseado anotação Rocha      |
| Vizinhos do Mix (pergunta email Luize)   |    20211208    |                             -                                |
|Preparação de tabela toxina (similar Robs)|    20211220    | USar dados do Robson para criar uma tabelo toxina por T6ss   |




## Layout do artigo 
*Identificar todo o repertorio de toxinas secretadas por T6SS, incluindo as descritas e principalmente as novas.*  
Analise do C-terminal (abaixo). Bastion correlacionando com a vizinhança.   
 - Pensar em estrátégias de antieucarioticas. 
   - Cluster muito conservado (NP_459268.1) apresentou  homologia remota com FHA, que pode estar envolvida no T3SS. Sempre na vizinahnça de ImpE
   -
 - Quais tipos de T6SS temos?  SPI-6, SPI-19, ou outros.     
 - Quantas toxinas por genomas?
 - Associação de grupos de toxinas com diferentes T6SS.
 - Clonagem dos candidatos
## To do list
### To friday 03/09/2021
- [ ] Finish unknow domains part.
- [ ] Save the unknow domain in folders with xlsx files of neighbhroods and architectures.

### Analysis of the unkown part of the follow proteins:
- [ ] Remover dominio rocha T6SSi_tssH da marcação de componentes. 
- [ ] Considerar DUF4150, PAAR, VgrG e HCP como efetores.
- [x] PAAR, 
- [x] DUF4150,
- [x] HCP,
- [x] VgrG,
- [x] RHS
- [ ] Mix/Fix (CDD)  (Dor Salomon)
- [ ] Modelos Bastion (Modelo de efetores de outros sistemas)
- [ ] [Modelo](https://www.ncbi.nlm.nih.gov/Structure/cdd/cddsrv.cgi?uid=235715) do paper [Identification of type VI secretion system toxic effectors using adaptors as markers](https://pubmed.ncbi.nlm.nih.gov/33304467/) 
    - [ ] Adptadores  
    - [ ] DUF4123 Adptadores
    - [ ] DUF1795 Adptadores
    - [ ] DUF2169 
    - [ ] Existe algum dominio fusionado a esses adptadores ?

### Analysis of T6SS classification
- [ ] Cross the Bao data with our data Folder(20210901)

## Notebooks links:
[Robson's analysis](./Robson_analysis.md)    
[Models created by Gian](./data/mymodels/tox_first_curation.md)  
[2 round of models created by Gian](./data/mymodels/my_models_2.md)  
[T6SS Classification](./data/etc/T6SS_classification.md)    
[Putative T6SS toxins (crossing frequency data with Robson toxins annotation)](./data/etc/putative_tox_all.md)  


## Questions 
- 1  Incluir genômica comparativa? (Só é viável se tivermos o background de genomas sabidamente negativos T6SS
- 2  Classificar T6SS Baseado em organização (ordem dos genes). Quais os tipos de T6SS? Usar Jaccard?
- 3  Quantas toxinas por genoma?
- 4  Quantas antitoxinas por genomas?
- 5  Quais grupos estão associados a quais T6SS?
- 6  Verificação experimental de uma seleção das toxinas preditas.
- 7  Strain selection
    - [ ] Blast selected proteins against. List:
      - [ ] https://www.genome.jp/dbget-bin/www_bget?seo:STM14_0336
      - [ ] https://www.kegg.jp/dbget-bin/www_bget?sey:SL1344_0283
      - [ ] https://www.kegg.jp/dbget-bin/www_bget?stm:STM0288
    - [ ] Find isolates with the highest number of selected toxins
    - [ ] Build alignments for families of selected toxins
- 8 - analisar regiões variáveis dentro do T6SS cluster a procura por toxinas

