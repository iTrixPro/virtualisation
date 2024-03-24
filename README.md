<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<br />
<div align="center">
  <h3 align="center">Virtualization Project</h3>

  <p align="center">
    Final project for our virtualization class.
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#launch">Launch</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

We developed a streamlined Python Flask application enabling users to seamlessly register and subsequently log in. Our primary focus was to leverage our expertise in Docker and Kubernetes throughout the project, enhancing its scalability and deployment efficiency.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![MySQL][MySQL]][MySQL-url]
* [![Kubernetes][Kubernetes]][Kubernetes-url]
* [![Docker][Docker]][Docker-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Before you begin, make sure you have the following technologies installed on your computer:

* Docker
* Minikube
* Helm

### Prerequisites

Firstly, you have to clone our repo :
```sh
git clone "https://github.com/iTrixPro/virtualisation"
cd virtualisation/
```

Secondly, you will pull our docker image from the hub : 
```sh
docker pull itrixpro/app:0.0.2.RELEASE
```

### Launch

Now, we are ready to begin.

1. Begin by launching minikube
```sh
minikube start
```

2. After that make use of traefik
```sh
helm repo add traefik https://traefik.github.io/charts
helm repo update
helm install traefik traefik/traefik
```

3. We implemented a setup script to make it easy for us but also for you
```sh
./setup.sh
```

4. Then, you will have to connect to the database
```sh
kubectl exec -it <mysql-pod-name> -n authentication  -- mysql -h mysql-service -u root -p  
Enter password: root
```

5. Create the table User
```sh
CREATE TABLE USERS( 
    -> id INT AUTO_INCREMENT PRIMARY KEY,
    -> username TEXT,
    -> pwd TEXT
    -> );
```

6. Finally, you just have to access our service 
```sh
minikube service traefik
```


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/iTrixPro/virtualisation/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/iTrixPro/virtualisation/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/iTrixPro/virtualisation/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/iTrixPro/virtualisation/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/iTrixPro/virtualisation/blob/master/LICENSE.txt


[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org
[MySQL]: https://shields.io/badge/MySQL-lightgrey?logo=mysql&style=plastic&logoColor=white&labelColor=blue
[MySQL-url]: https://www.mysql.com
[Kubernetes]: https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white
[Kubernetes-url]: https://kubernetes.io/fr/
[Docker]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com
