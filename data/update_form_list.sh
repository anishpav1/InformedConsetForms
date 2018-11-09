#!/bin/bash

CLINICAL='clinical_forms'
RESEARCH='research_forms'

ls -1 ${CLINICAL} > clinical_form_list.csv
ls -1 ${RESEARCH} > research_form_list.csv
