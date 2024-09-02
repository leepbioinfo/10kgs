## Robson's analysis
Files path: 
```bash
/projects/salmonella/work/20210726
```
The sources present at this folder will create the follow variables:

|       Variable       |                                                          content                                                          |
|:--------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| MIN_CTERMINAL_LENGTH |                      Minimal length for selecting C-terminal unannotated regions with toxic potential                     |
|         cgrf         |  Gene neighborhood of putative T6SS gene clusters. Built by applying the neighborhs() method to the genome NeighborhoodDF |
|       curated        |                                   Manually selected c80e3 clusters with toxic potential                                   |
|        domain        |                            Table of coordinates for domains within proteins (one domain per row                           |
|        genome        |                                            Full *Salmonella* genome annotation                                            |
|        md10k         |                         10K Salmonella genome assembly properties and putative toxins distribution                        |
|       moreira        |                         Genomes selected for cloning (based on availability and number of toxins)                         |
|         scat         |                                               Function to concatenate series                                              |
|       selected       |                                                 Temporary list of columns                                                 |
|       t6ssmap        |                                                Table to rename T6SS domains                                               |
|        toxann        |                                 Table used to rename toxic domains while building toxdist                                 |
|       toxdist        |                                Distribution of known toxin domains among Salmonella genomes                               |
|        toxins        |                                Putative toxins detected using HMM models (Aravind and Pfam)                               |
|        toxsig        |                                      Manually curated list of toxin domains from Pfam                                     |


The toxin table source  code:
| Code |   Source  |
|:----:|:---------:|
|  P   |    PFAM   |
|  B   |  BastionX |
|  A   |  Aravind  |
|  R   |     Rocha     |
|  C   |     CDD     |

Tabela toxins X é no genoma todo e o Y é na vizinhança do T6SS

Curated usar o pid e ignorar o c80e3old.  
E cruzar os grupos com a tabela workcopy no googledrive aba selection Ethel 20 total.
