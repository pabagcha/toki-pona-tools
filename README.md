# TOKI PONA TRANSLATOR AND GRAMMAR TOOLS

Repository to share the final tools developed for my Bachellor final Project. It consists on a Toki Pona to English translator, a sentence generator and a parser.

## Instalation

The initial requirement for the installation is to have git, python 3.9 and pip installed.

You also need git lfs. If you don't have it installed, download it from here: https://docs.github.com/es/repositories/working-with-files/managing-large-files/installing-git-large-file-storage

Then you need to download the repository and enter the folder:

~~~
git clone https://github.com/pabagcha/toki-pona-tools.git
cd toki-pona-tools
git lfs pull
~~~

Finally you must install all the dependencies with the command:

~~~
pip install -r requirements.txt
~~~

## Usage

### Translator

To use the translator execute with python the program `translate.py` with the option `-s`\\`--sentence` written directly as an argument. For example:
~~~
python translate.py -s "mi moku e kili"
~~~

With the option `-f`\\`--file` you can pass as an argument a text file containing a sentence per line. For example:

~~~
python translate.py -f "test.txt"
~~~

### Sentence Generator

In order to use the sentence generator. We can just execute the program `generate.py` with python:

~~~
python generate.py
~~~

In addition, we can use the option `-n`\\`--number` to indicate the number of desired generated sentences:

~~~
python generate.py -n 10
~~~

### Parser

The parser is used just executing the program `CYK_Parser.py` without arguments:

~~~
python CYK_Paser.py
~~~

After that, the program will ask you to input the sentence. After that it will tell you if the sentence is correct or not.

## Author
Pablo Baggetto Chamero.

Please, cite me and my work if you use the software and models presented in the repository.

## Acknowledgments

These projects have been used as a base to develop the projects in the repository:

- [Marian-NMT](https://github.com/marian-nmt/)
- [OPUS-MT](https://github.com/Helsinki-NLP/OPUS-MT-train)
- [Iker Garc??a Ferrero's CYK](https://github.com/ikergarcia1996) 