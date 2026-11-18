# TesteIOT

Projeto acadêmico introdutório para praticar o uso do GitHub e a clonagem de um repositório em um terminal da AWS.

## Objetivo

Criar arquivos, registrar versões no GitHub e copiar o repositório para a AWS utilizando Git.

## Arquivos

- `README.md`: descrição e instruções do projeto.
- `teste.txt`: arquivo de texto para conferir a cópia.
- `exemplo.py`: programa simples que mostra leituras fictícias de temperatura.

As temperaturas são apenas dados de exemplo. Não há sensor físico nem conexão com dispositivos IoT.

## Como clonar na AWS

No terminal do AWS CloudShell, execute cada comando em uma linha:

```bash
git clone https://github.com/PedroMessiass/TesteIOT.git
cd TesteIOT
ls
cat teste.txt
python3 exemplo.py
```

O comando `git clone` copia o repositório. O comando `ls` lista os arquivos; `cat` mostra o texto; `python3` executa o exemplo.

## Resultado esperado

O programa exibe três temperaturas fictícias: 23.5, 24.0 e 24.5 graus Celsius, e termina.
