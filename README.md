<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- [![Contributors][contributors-shield]][contributors-url] -->
<!-- [![Forks][forks-shield]][forks-url] -->
<!-- [![Issues][issues-shield]][issues-url] -->
<!-- [![MIT License][license-shield]][license-url] -->

<!-- PROJECT LOGO -->
<!-- <br />
<div align="center">
  <a href="https://github.com/ASU-Lim-Lab/Spike_mutation_tracker">
    <img src="logo.png" alt="Logo" width="80" height="80">
  </a> -->

  <h3 align="center">Spike mutation tracker</h3>

  <p align="center">
    Directory
    <br />
    <a href="https://github.com/ASU-Lim-Lab/Spike_mutation_tracker/tree/main/sequence%20analysis"><strong>Sequence analysis »</strong></a>
    <br />
    <a href="https://github.com/ASU-Lim-Lab/Spike_mutation_tracker/tree/main/visualization"><strong>Visualization »</strong></a>
    <br />
    <br />
<!--     <a href="https://github.com/ASU-Lim-Lab/Absolute-Q/">any_criteria</a> -->
<!--     · -->
<!--     <a href="https://github.com/ASU-Lim-Lab/Absolute-Q/">any_criteria</a> -->
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#sequence-analysis">Sequence analysis</a></li>
    <li><a href="#visualization">visualization</a></li>
<!--     <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributors">Contributors</a></li> -->
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

This repository contains scripts used to analyze and visualize mutations in the SARS-CoV-2 spike gene. <br>

Current efforts involve detection of evolutionarily convergent SARS-CoV-2 spike mutations, mutations that enable mAb and antiviral resistance, and mutations that increase transmissibility of the disease. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Scripts are compatable with Python 3.7 - Python 3.11, Pandas 1.5.1+, Biopython 1.79+, Streamlit 1.18.0+.
  - Anaconda distribution package recommended for conda installations.
  - Pip installation requires pip 19.3+.


### Prerequisites

* [![Python][Python]][Python-url]
* [![Pandas][Pandas]][Pandas-url]
* [![Biopython][Biopython]][Biopython-url]
* [![Streamlit][Streamlit]][Streamlit-url]
* [![Plotly][Plotly]][Plotly-url]


### Installation
#### Pandas
  ```sh
  conda install pandas
  ```
  ```sh
  pip install pandas
  ```
#### Biopython
  ```sh
  conda install -c conda-forge biopython
  ```
  ```sh
  pip install biopython
  ```
#### Streamlit
  ```sh
  conda install -c conda-forge streamlit
  ```
  ```sh
  pip install streamlit
  ```
#### Plotly
  ```sh
  conda install -c plotly plotly_express
  ```
  ```sh
  pip install plotly_express
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Sequence Analysis


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Visualization

Data visualization was performed on the sequence analysis output for SARS-CoV-2 sequences submitted to GISAID for the state of Arizona within the last 90 days. Visualization was performed using the python library plotly express and presented in a dashboard using the python library streamlit. 

Local directory structure should emulate the format in the visualization folder for this repository.
- The main streamlit script should be in the parent directory while dashboard pages, and data should reside in their respective sub-directories. 
- For more information on how to execute the script, visit 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [ ] Continued development of analysis and visualization script.
<!-- - [ ] Feature 2 -->
<!-- - [ ] Feature 3 -->
<!-- - [ ] Nested Feature -->
<!-- 
[Open issues](https://github.com/ASU-Lim-Lab/Absolute-Q/issues)

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- CONTRIBUTING -->
<!-- ## Contributors
<br />
<div align="left">
    <a href="https://github.com/ASU-Lim-Lab/Absolute-Q/graphs/contributors"><strong>Contributors »</strong></a>
</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ASU-Lim-Lab/Absolute-Q.svg?style=for-the-badge
[contributors-url]: https://github.com/ASU-Lim-Lab/Absolute-Q/graphs/contributors
[Biopython]: https://img.shields.io/badge/Biopython-1.80-blue
[Biopython-url]: https://biopython.org/
[Pandas]: https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org/
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[streamlit]: https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white
[streamlit-url]: https://docs.streamlit.io/library/get-started/installation
[Plotly]: https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white
[Plotly-url]: https://plotly.com/python/getting-started/
