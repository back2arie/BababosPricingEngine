## Architecture Diagram
We use [Diagrams](https://diagrams.mingrammer.com/) to generate diagram from code ("Diagram as Code").

**Setup**

We assume you already have python & Homebrew installed, next we need to install `graphviz`:

```sh
$ brew install graphviz
```

Install diagrams:
```sh
$ python3 -m pip install diagrams
```

To generate the diagram, just run:

```sh
$ python3 diagram.py
```

## Entity Relationship Diagram
We use [DBML](https://www.dbml.org/) to define our database schema and structure, we also use [dbml-renderer](https://github.com/softwaretechnik-berlin/dbml-renderer) to renders DBML files to SVG images.

**Setup**
We assume you already have Node.js, npm & Homebrew installed, next we need to install:

```sh
$ npm install -g @softwaretechnik/dbml-renderer
$ brew install librsvg
```

Generate ERD:
```sh
$ dbml-renderer -i database.dbml -o erd.dot -f dot && dot -Tsvg erd.dot -o erd.svg
```

It will generate svg, to convert it to png, run:
```sh
$ rsvg-convert -h 1300 erd.svg -b white > erd.png
```

> **Note:** You can adjust the -h parameter to set the height so that image quality is good & also maintain file size.

## Flowchart Diagram

We use [Mermaid](https://mermaid.js.org/).

```
$ npm i -g mermaid mermaid.cli
```

Convert to png:
```
$ mmdc -i flowchart.mmd -o flowchart.png
```
