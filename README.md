# Informed Consent Form Study
This repository contains tooling to manage informed consent forms collected from the public domain in attempt to understand permissions, obligations, and the related process of obtaining and providing consent. This effort will make use of the [Informed Consent Ontology](https://github.com/ICO-ontology/ICO), which is currently under development and NLP techniques in order to test the possibility of executing semantic queries on unstructured informed consent forms. The explicit goal is to build interoperable semantic models that can enrich traditional information systems used to store biospecimens and data collected for research, or as part of a clinical procedure.

At present this work is not yet peer-reviewed.

## Data
The data in `data/` is informed consent forms in `.txt` format that have been collected from publicly available resources.

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
