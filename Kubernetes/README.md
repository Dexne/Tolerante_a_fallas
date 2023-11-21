# Kubernetes
### By: Dexne

**¿Qué es kubernetes?:**

Kubernetes es una plataforma portable y extensible de código abierto para administrar cargas de trabajo y servicios. Kubernetes facilita la automatización y la configuración declarativa. Tiene un ecosistema grande y en rápido crecimiento. El soporte, las herramientas y los servicios para Kubernetes están ampliamente disponibles.

Kubernetes no es una Plataforma como Servicio (PaaS) convencional. Ya que Kubernetes opera a nivel del contenedor y no a nivel del hardware, ofrece algunas características que las PaaS también ofrecen, como deployments, escalado, balanceo de carga, registros y monitoreo. Dicho esto, Kubernetes no es monolítico y las soluciones que se ofrecen de forma predeterminada son opcionales e intercambiables.

**¿Qué es Ingress?:**

Kubernetes Ingress es un objeto de Kubernetes que gestiona el acceso externo a los servicios del clúster de Kubernetes. Permite exponer rutas HTTP y HTTPS desde fuera del clúster de Kubernetes a los servicios dentro del clúster. Un Ingress nos permite controlar muchos aspectos de nuestra red en nuestro clúster de Kubernetes.

Para utilizar Ingress, debes tener el Controlador Ingress en el clúster Kubernetes. Este controlador no viene como parte del clúster de Kubernetes como otros controladores del clúster, no se inicia automáticamente en el clúster. Podemos desplegar cualquier número de controladores de ingreso en el clúster de Kubernetes.

**¿Qué es LoadBalancer?:**

Un balanceador de carga actúa como único punto de contacto para los clientes. El balanceador de carga distribuye el tráfico entrante de aplicaciones entre varios destinos, tales como instancias EC2, en varias zonas de disponibilidad. Esto aumenta la disponibilidad de la aplicación.

Elastic Load Balancing admite los siguientes balanceadores de carga: balanceadores de carga de aplicaciones, balanceadores de carga de red, balanceadores de carga de gateway y balanceadores de carga clásicos. Puede seleccionar el tipo de balanceador de carga que mejor se adapte a sus necesidades.

**Proceso:**

Para esta práctica se ha diseñado un pequeño servicio realizado en el lenguaje de programación Go.

Simplemente se ha realizado la interfaz básica con un mensaje escrito, para demostrar que funciona se levanta el servicio de manera local en el puerto 3000.

![CódigoFuente](https://github.com/Dexne/Tolerante_a_fallas/blob/main/Kubernetes/assets/1_codigo_fuente_go.jpeg)

Si ingresamos al navegador y escribimos en el siguiente texto podremos visualizar el servicio ejecutandose.
```
localhost:3000
```

He hecho zoom para poder apreciar mejor el contenido.

![ejecucion](https://github.com/Dexne/Tolerante_a_fallas/blob/main/Kubernetes/assets/2_levantamos_el_servicio.jpeg)

Para poder mejorarlo y llegar a poder implementar kubernetes en algun momento es necesario realizar un serie de acciones, primeramente deberemos de realizar la imagen de docker. Podemos apoyarnos del siguiente comando:
```
docker build -t tuUsuario/nombre_de_tu_aplicacion .
```

Algo tal que así:

![ImagenDocker](https://github.com/Dexne/Tolerante_a_fallas/blob/main/Kubernetes/assets/3_Creamos_imagen_docker.jpeg)

Consultamos nuestras imagenes para verificar que se creo, de igual forma podemos hacer esto con el comando siguiente:

```
docker images | grep tuUsuario/nombre_de_tu_aplicacion
```
![consultaDocker](https://github.com/Dexne/Tolerante_a_fallas/blob/main/Kubernetes/assets/4_Consultamos_dockerizada.jpeg)

Levantamos nuestro servicio pero ahora desde docker, aquí podemos especificar en que puertos deseamos que se ejecute nuestro servicio.

![levantarDesdeDocker](https://github.com/Dexne/Tolerante_a_fallas/blob/main/Kubernetes/assets/5_Levantamos_con_docker.jpeg)

Ingresamos al naveagor en el puerto especificado desde localhsot para verificar que esta funcionando.

![funcionaDocker](https://github.com/Dexne/Tolerante_a_fallas/blob/main/Kubernetes/assets/6_Verificamos_docker.jpeg)

Una vez que ya sabemos que nuestro proyecto esta funcionando correctamente podemos hacerle un push a DockerHub.

![DockerHub](https://github.com/Dexne/Tolerante_a_fallas/blob/main/Kubernetes/assets/7_Push.jpeg)

Verificamos que si existe la conexión entre nuestro entorno de trabajo y DockerHub.

![DockerHubConnected](https://github.com/Dexne/Tolerante_a_fallas/blob/main/Kubernetes/assets/8_Comprobamos_DockerHub.jpeg)

Como siguiente paso deberemos de crear nuestro Cluster, aquí es donde crearemos los kubernetes.
Para ellos nos apoyaremos de DigitalOcean. Deberemos de crearnos una cuenta, cabe mencionar que nos pedirán una verificación con nuestra tarjeta de crédito, no te preocupes, para lo que estamos realizando no gastaremos dinero.
Podemos darle un nombre a nuestro Cluster, en mi caso lo e dejado por defecto.

![DigitalOcean](https://github.com/Dexne/Tolerante_a_fallas/blob/main/Kubernetes/assets/9_CreamosCluster.jpeg)

Creamos el cluster.

![CreamosCluster](https://github.com/Dexne/Tolerante_a_fallas/blob/main/Kubernetes/assets/10_Cluster_creado_kubernetes.jpeg)

 Una vez creado deberemos de esperar un poco en lo que termina de configurarse. Una vez que termine los procesos debemos de descargar el archivo de las configuraciones que nos proporciona la página misma. Es importante que no compartas este archivo con nadie.

 ![download config file](https://github.com/Dexne/Tolerante_a_fallas/blob/main/Kubernetes/assets/11_Config_File.jpeg)

 Lo siguiente es mover nuestro archivo que acabamos descargar a la carpeta raíz donde tenemos instalado kubectl. Para ello nos apoyaremos del siguiente comando:

```
mv nombre_de_tu_archivo.yaml ~7.kube/config
```

Al mover el archivo con las configuraciones a la carpeta raíz podremos consultar los nodos:

```
kubectl get nodes
```

![ConsultaNodos](https://github.com/Dexne/Tolerante_a_fallas/blob/main/Kubernetes/assets/12_get_nodes.jpeg)

Después deberemos de aplicar las configuraciones que tenemos implementadas en nuestro archivo "development.yml". Nos apoyaremos del siguiente comando:

```
kubectl apply -f development.yml
```

Y volvemos a consultar los nodos, notarás que ahora tenemos más información de ellos.

![nodosMasInfo](https://github.com/Dexne/Tolerante_a_fallas/blob/main/Kubernetes/assets/13_get_developments.jpeg)

Ahora aplicamos las configuraciones del archivo "service.yml"

```
kubectl apply -f service.yml
```

Y consultamos los servicios

```
kubectl get services
```

![serviceyml](https://github.com/Dexne/Tolerante_a_fallas/blob/main/Kubernetes/assets/15_get_services.jpeg)

Notaremos que tenemos una dirección IP, la copiamos y la consultamos en nuestro navegador.

Podremos ver que nuestro servicio se esta desplegando con exito.

![desplegado](https://github.com/Dexne/Tolerante_a_fallas/blob/main/Kubernetes/assets/16_Consultamos.jpeg)

Finalmente consultamos en DigitalOcean los procesos.

![DigitalOceanProcess](https://github.com/Dexne/Tolerante_a_fallas/blob/main/Kubernetes/assets/17_DigitalOcean.jpeg)


### Referencias:

Qué es Kubernetes. (2022, July 17). ¿Qué es Kubernetes? Kubernetes. https://kubernetes.io/es/docs/concepts/overview/what-is-kubernetes/

‌Ingress. (2023, October 19). Ingress. Kubernetes. https://kubernetes.io/docs/concepts/services-networking/ingress/

‌https://www.facebook.com/grokkeepcoding. (2022, June). ¿Qué es Ingress Controller en Kubernetes? KeepCoding Bootcamps. https://keepcoding.io/blog/que-es-ingress-controller-en-kubernetes/

‌howtoforge. (2021, June 2). Qué es el Controlador Ingress y cómo desplegar el Controlador Ingress de Nginx en el Cluster Kubernetes en AWS usando Helm - HowtoForge. HowtoForge. https://howtoforge.es/que-es-el-controlador-ingress-y-como-desplegar-el-controlador-ingress-de-nginx-en-el-cluster-kubernetes-en-aws-usando-helm/

‌¿Qué es un Application Load Balancer? - Elastic Load Balancing. (2023). Amazon.com. https://docs.aws.amazon.com/es_es/elasticloadbalancing/latest/application/introduction.html

‌KodeKloud. (2018). Kubernetes For Beginners: Taints & Tolerations [YouTube Video]. In YouTube. https://www.youtube.com/watch?v=mo2UrkjA7FE

‌Amazon Web Services. (2017). Spire Labs: Fault-tolerance with Kubernetes on AWS [YouTube Video]. In YouTube. https://www.youtube.com/watch?v=xvXy2BiaWrQ

‌TechWorld with Nana. (2020). Benefits of Kubernetes | Scalability, High Availability, Disaster Recovery | Kubernetes Tutorial 16 [YouTube Video]. In YouTube. https://www.youtube.com/watch?v=g8Sf-6EsgZM
‌
