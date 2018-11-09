# Data
Informed consent forms stored in two directories. All files are in plaintext format (`.txt`) and contain `utf-8` decodable characters. We do not store binary file types like `.pdf`.

## Tools
There are two tools in this directory.

1. [`update_form_list.sh`](update_form_list.sh) is a simple command-line tool to update lists of filename for each type of consent. To invoke:

    ./update_form_list.sh

1. [`corpus_analysis.py`](corpus_analysis.py) is a python3 command-line tool to generate a `.csv` file containing high-level data for all files in a specified directory. This command requires three positional arguments: (1) `--src` is the root directory for the search. (2) `--type` is the file type, specified as a string value corresponding to a valid extension (ex. '.txt'). (3) `--dest` is the name and destination of the output file. Example below:

    ./corpus_analysis.py --src ./ --type .txt --dest ./analysis_output.csv

## Metadata
This is an active area of development for us. Coming soon.

1. A list of clinical consent form filenames can be found [here](clinical_form_list.csv).
1. A list of research consent form filenames can be found [here](research_form_list.csv).

## List of Files Converted from OCR
1. Cambridge_Consent_ivsedation2.txt
1. Cambridge_Consent_oralsurgery4.txt
1. Cambridge_Consent_ortho2.txt
1. Cambridge_Consent_photographs.txt
1. Cambridge_Consent_postsandretentionpins.txt
1. Cambridge_Consent_scalingrootplaning1.txt
1. Cambridge_Consent_silveramalgam.txt
1. Cambridge_Consent_tmjtherapy.txt
1. DesertPearl Dentistry)Patient Info Sharing Consent.txt
1. Gulf Coast MRI and Diagnostic_mri-contrast-consent-form.txt
1. Health Village Imaging_MRI Consent From.txt
1. Highland Hospital_Device Implant Consent.txt
1. HMH - Procedure Consent.txt
1. HMH Sedation Consent.txt
1. Huntington_blood-transfusion-english.txt
1. National Network for Oral Health Access_Extraction-of-Teeth-2-English.txt
1. National Network for Oral Health Access_Treatment-by-Extern-Dentist-English.txt
1. Penn Medicine_CVC Informed Consent Document.txt
1. Regional Blood Service_GHANA_ Blood Consent-Form.txt
1. St Josephs_MRI IV Contrast Questionaire - English.txt
1. Stony Brook Medicine_CVC Note and Consent.txt
1. They Physician Network_Varicella Immunization Consent.txt
1. Tischler_ConsentForDentalTx.txt
1. Tischler_ConsentForExtraction.txt
1. Tischler_EndodonticTx_RC_.txt
1. Tischler_FixedProsthodontocsTx.txt
1. Tischler_LanapConsentTx.txt
1. Cambridge_Consent maxillarysinuselevation.txt
1. Cambridge_Consent_amalgamreplace.txt
1. Cambridge_Consent_compositefillings.txt
1. Cambridge_Consent_crownandbridge.txt
1. Cambridge_Consent_dentures2.txt
1. Cambridge_Consent_endodontics5.txt
1. Cambridge_Consent_endodontics10.txt
1. Cambridge_Consent_endoretreatment.txt
1. Cambridge_Consent_general1.txt
