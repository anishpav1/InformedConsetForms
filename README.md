# Informed Consent Form Study
This repository contains tooling to manage informed consent forms in attempt to understand permissions, obligations, and the related process of obtaining and providing consent. Consent forms were gathered from the public domain or by request from institutions using such forms, and were designed for biospecimen research or clinical procedures. This effort will make use of the [Informed Consent Ontology](https://github.com/ICO-ontology/ICO), which is currently under development, and NLP techniques in order to test the possibility of executing semantic queries on unstructured informed consent forms. The explicit goal is to build interoperable semantic models that can enrich traditional information systems used to manage biospecimens and their associated data.

At present this work is not yet peer-reviewed.

## Data
The data in `data/` are informed consent forms in `.txt` format that have been collected from publicly available resources or by request from institutions using such forms. Forms are organized according to type, either for research studies or clinical procedures.

The data in `research_forms/` are presently limited to studies in which biospecimens are collected.
The data in `clinical_forms/` reflect a range of clinical procedures, not limited to those in which biospecimens are collected.

## Status
This is a preliminary repository to organize tooling for annotation efforts. None of the products in this repository are tested for production settings. Users of this material do so at their own risk.

## Development
This project will make use of  [CLAMP](https://clamp.uth.edu/), a clinical NLP tool developed by The University of Texas Health Science Center at Houston.

## Annotation Steps
1. Start CLAMP
1. Create a new project
1. Select 'Corpus Annotation'
1. Replace the `typedef.xml` file in the clamp project directory with the `typedef.xml` file in the [clamp](clamp/) folder.
1. Add all `.txt` files in `data/` of this repository to the `train` directory in the CLAMP workspace
1. Convert all `.txt` files into `.xmi` files by double-clicking on them
1. Annotate away!

## Contact
TDB
