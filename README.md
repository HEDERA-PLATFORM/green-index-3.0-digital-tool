# The Green Index 3.0 (Digital tool)

The Digital Green Index 3.0 (**Digital GI3.0**) is the first open-source assessment tool for the
green inclusive finance sector which combines data ownership, aligmnent with latest standards, and the option for automatic data sharing with other stakeholders.

See below for further details. Please direct any questions or comments to [green-index-feedback@hedera.online](mailto:green-index-feedback@hedera.online)


## License

The Software is released under an open-source [MIT License](https://opensource.org/licenses/MIT). See the [licese file](https://github.com/HEDERA-PLATFORM/green-index-3.0-digital-tool/blob/master/LICENSE) for detail.

Customization, distribution, reproduction (commercial and non-commercial use) are allowed, provided the following acknowledgemen/copyright statement is included:

*The Green Index 3.0 Digital Tools has been implemented by [HEDERA Sustainable Solutions](https://hedera.online) (Alfonso Caiazzo) as a service for the Green Inclusive and Climate-Smart Finance Action Group of the [European Microfinance Platform](https://e-mfp.eu), based on the [Green Index 3.0](https://www.e-mfp.eu/green-index) tool developed by the GICSF-AG.*


## About

### About the Green Index 3.0

The Green Inclusive and Climate Smart Finance Action Group (GICSF AG) has developed and implemented the [Green Index 3.0](https://www.e-mfp.eu/green-index) since 2014. 
The Green Index 3.0 (GI3.0) is the latest version of this assessment tool, which has been piloted since October 2021 and officially launched in March 2022. 

The GI3.0 has been developed in close collaboration with the 7th Environmental Dimension of the USSEPM of SPTF+CERISE, developed by the joint work of the GICSF AG.
This collaboration ensures that the two tools can be aligned at the level of standards and essential practices.


### About the digital tool

The digital version of the GI3.0 has been conceptualized by Davide Forcella (YAPU Solutions & CERMI) and Natalia Realpe Carrillo (HEDERA Sustainable Solutions), heads of the GICSF-AG, based on the GI3.0 
The digital version has been implemented by Alfonso Caiazzo, Responsible of Impact Management & Software Development at [HEDERA Sustainable Solutions](https://hedera.online).



## Usage of the GI3.0

The goal of the **Digital GI 3.0** is to promote both self- and guided-assessment of environmental practices of financial service providers, fostering actve collaboration and data sharing between stakeholders, but without a priori restriction to data ownership.
With the Digital GI3.0 institutions can decide whether they want to host (and manage) their data, or if they prefer to use existing databases, selecting also the particular provider.
API to share data between actors are available, and dedicated APIs to share the data at the level of Dimension 7 of the USSEPM will be provided as well.

Three options are currently available.

### Demo (fill-only)
Users can access  a free demo of the web survey [here](https://hedera.online/gicsf_ag_tools/try-the-green-index-3-0.html). This allows to navigate the questions
and submit the results (in a single session). On request, the submitted data can be processed and scored. However, usage of the demo version for real audit is not recommended, as the demo server might change in the future and the maintanance of the data is not ensured.

### Fill & Edit (without hosting)
A most reliable option for green index assessment is to use a dedicated installation of the tool. You can contact the GICSF-AG heads or [HEDERA](https://hedera.online) for support.
Depending on the requirements of the project, you will be able to have full access to the data, or only need to complete the webform, in order to receive an assessment audit.

The user credentials will allow users to have access their own instance of the tool (hosted by HEDERA in the same ODK Central instance),
revise and edit entered data, as well as download of raw CSV file (including also APIs to R, python, and Power BI)

### Self-hosted
For more advanced users, it is also possible to self-install ODK Central, upload the XLS Form provided in this repository directly, and host and manage the data independently.
This will allow full control on the technical aspects. However, users are responsible of maintaining the survey up to date, in order to ensure full compatibility between their database and the official database of assessment of the GICSF-AG. 
If the survey is used as it is provided, aligmnent with the GI will be ensured also for self-hosted instances.

**Note**: Cost of server infrastructure should be covered (around 10 USD/month would be enough to begin with). See below for detailed instructions.

## Detailed instructions for self-hosting

### Server (for experts)
You need to have (or rent) a cloud server and cloud space. There are several options available. If you have no idea how, go to the next step and follow the suggested choice
([DigitalOcean](https://digitalocean.com).

### 1.ODK Central
ODK Central is an open source data management app developed and maintained by the
[ODK](https://getodk.org) community. 
Follow these [instructions](https://docs.getodk.org/central-install/) to get started. In particular, you will also see how to acquire a suitable cloud space. 
Alternatively, you can ask for commercial support (e.g., [ODK Cloud](https://getodk.org)
or [HEDERA](https://hedera.online)).

### 2.Digital GI3.0 sources
Once the ODK Central installation is available at, e.g., https://<your-odk-central>.<your-domain>.com, you can clone the repository on your local machine.
Create a folder `data/` in the main folder of the project.

### 3.Deployment
From ODK Central, follows these steps:
- create a new project
- add new form
- upload the `green_index_3_0.xlsx` file
- publish the form
- create a public link, so that this will be accessile from any browser.
- create app users and setup the QR codes if you need to use the tool on mobile devices (e.g., Tablets)

**Important**: Take note of the ODK Central and of the Digital GI3.0 version numbers, as these might change in the future and compatibility with previous versions is not ensured

### 4.Usage

Users can enter data via the web link and submissions can be managed directly via the ODK Central interface. For the scoring, download the CSV Table from ODK Central to your local machine into the `data/` folder created (Step 2 above). Modify the `input.json.example` file provided with this repository. In particular, use the name of the data file and the rule to select the audit you want to process.
Run `python scoring.py input.json` to create an excel file containing the scores of each indicator.



## Dashboard

Work in progress

## Alignment with USSEPM

Work in progress

## Tech Stack

### Enketo Express
The web-version of the Digital GI3.0 has been implemented using [Enketo](https://enketo.org), an open-source framework for creating web surveys
based on the (standard) [XLSForm](https://xlsform.org)

### ODK Central
The GI3.0 app (backend and database) is hosted using [ODK Central](https://docs.getodk.org/central-intro/), an open-source server-side application 
of the [ODK](https://getodk.org/) project. 
The current version of ODK Central includes automatically Enketo for rendering webforms.

### Python
Scoring and automated analysis are implemented in python.


