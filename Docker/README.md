# Uso de docker

**By: Dexne**

¿Qué es Docker?

Docker es una plataforma de virtualización de contenedores ampliamente utilizada en desarrollo y despliegue de aplicaciones. Permite empaquetar aplicaciones y sus dependencias en entornos aislados llamados "contenedores," lo que simplifica la gestión de aplicaciones y garantiza la portabilidad entre diferentes sistemas. Docker es esencial para el desarrollo ágil y la implementación consistente de aplicaciones, ya que resuelve problemas de compatibilidad y entorno. Los contenedores Docker son versátiles, ligeros y eficientes en términos de recursos, lo que acelera el desarrollo, garantiza la consistencia del entorno y facilita la escalabilidad. Se utiliza en una variedad de casos, desde desarrollo local hasta implementación en la nube.

Insrtalación de Docker:

En mi caso me encuentro en un sistema operativo linux con la distribución Feroda en su versión 37, los pasos pueden cambiar dependiendo el sistema operativo.

1. Deberemos de desintalar las versiones viejas de Docker que tengamos instalas:
   sudo dnf remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-selinux \
                  docker-engine-selinux \
                  docker-engine
2. Nos apoyamos de la página oficial para entraer los comandos necesarios:
  sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
3. Nos pedira que instalemos unas dependencias más, las aceptamos.

Para poder continuar con el desarrollo es necesario que iniciemos Docker, para eso podemos apoyarnos de los siguientes comandos:
  sudo systemctl status docker (esto para verificar el status de docker, en algunas ocaciones puede comenzar sin que nosotros lo hallamos activado.
  En caso de no estar activo, podemos inciarlo con (sudo sysmtectl start docker)
  Además de esto deberemos de agregar nuestro usuario al grupo de docker, si no sabes cual es tu usuario puedes saberlo con el comando (whoami).
  Para agregar nuestro usuario al grupo podemos hacer los siguinete:
    cat /etc/group | grep docker (verificar si existe el grupo llamado docker)
    sudo groupadd docker (en caso de no existir el grupo)
    sudo usermod -aG docker $USER (reemplazar $USER por nuestro usuario)
    sudo service docker restart (aplicar cambios)
  Ahora que nuestro usuario se encuentra en el grupo, podemos crear nuestro docker
    docker buold -t servicio-clima .
    docker run -p 5000:5000 servicio-clima (especificamos que deseamos usar el puerto 5000)
    
