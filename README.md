<a name="readme-top"></a>
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/julienbrs)
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/julienbrs/space_invaders">
    <img src="Assets/Space_Invaders_Logo.png" alt="Logo" width="128" height="55">
  </a>

  </p>
</div>

<!-- TABLE OF CONTENTS -->

<summary>Table of Contents</summary>
<ol>
<li>
    <a href="#about-the-project">About The Project</a>
</li>
<li>
    <a href="#getting-started">Getting Started</a>
    <ul>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    </ul>
</li>
<li><a href="#contact">Contact</a></li>
</ol>

<br />

<!-- ABOUT THE PROJECT -->

## About The Project

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

Approximation of the value of pi by the Monte Carlo method. The graphical display is done with the `draw.py` script while the approximation of the value can be done independently with `approximation.py`. Developed in python

<br />
<p align="center">
  <img src="ressources/show_result.gif" alt="Product Name Screen Shot"/>
</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

- python
  ```sh
  sudo apt install python3
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/julienbrs/space_invaders.git
   ```
2. Rights to execute
   ```sh
   chmod +x draw.py
   chmod +x approximate_pi.py
   ```
3. Then run the program, see more info about parameters in the [Usage](#usage) section
   ```sh
   ./draw.py 600 5000 5
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

By running `approximate.pi` directly, you need to put the number of points as a parameter. The result will be displayed in the terminal.

```sh
./approximate_pi.py 5000
```

![screenshot approximation.py result](ressources/approx_cmd.png)

By running `draw.py`, you need to put:

- the size of output image result
- the number of points
- the number of digits after the decimal point
- optional parameter: `false` to disable cleaning of the last result

```sh
./draw.py 600 5000 5
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Bourseau Julien - _1st year student at Ensimag, 2021/2022_ - julien.bourseau@gmail.com

Project Link: [https://github.com/julienbrs/space_invaders](https://github.com/julienbrs/space_invaders)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/julien-bourseau-ba2239228
