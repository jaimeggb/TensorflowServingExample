# Tensorflow Serving Example with Fashion MNIST

<details open>
<summary> <b>Brief Review</b></summary>

This is an example of use with Tensorflow Serving and the Fashion MNIST tensorflow dataset.  The main concept is that you could use tensorflow serving to deploy the model in your cloud storage or your local computer and not load the model everytime you start your application, if the server is running, then you can send a request to the server and wait for the response. 

This applications function as follows. 
- We fist use *TrainAndSaveModel.py* to make a model using the Fashion MNIST dataset.
- Next we use docker to serve the model (this is the easy way).
- Finally use *TestServer.py* to make test the request to the server.

Some prerequisites are:
- You need to be installed with Windows XX Pro.
- [Docker Edge have to be installed](https://hub.docker.com/editions/community/docker-ce-desktop-windows/).
- Have to install all packages of the *requirements.txt* if using Anaconda.
- [Have to install Tensorflow Serving](https://www.tensorflow.org/tfx/serving/docker)

</details>

<details close>
<summary> <b>Testing the Tensorflow Server Example</b></summary>

Anaconda Virtual Environment and Dependencies.
- Create a virtual environment with conda or your favorite virtual environment tool
~~~
conda create -n tfx python==3.8
~~~
- Activate the environment and install the dependencies to run
~~~
conda activate tfx
pip install -r requirements.txt
~~~

Putting Docker Edge in Service
- Download and Install Docker Edge on Windows
- Run the demo to ensure Docker is working
- When docker is running:
  - Go to the docker logo
  - Right click and select settings 
  - On Docker Engine change the value of `experimental` in the json file to `true`.
    ~~~
    {
    "registry-mirrors": [],
    "insecure-registries": [],
    "debug": true,
    "experimental": true
    }
    ~~~
- Restart the docker service

Putting Tensorflow Serving up and running
- Go to the [official tensorflow serving guide](https://www.tensorflow.org/tfx/serving/docker) to install with docker
- Follow the next steps, for this example I am in the `Downloads` folder of my computer.
- Download the TensorFlow Serving Docker image and repo
    ~~~
    docker pull tensorflow/serving
    ~~~
- Clone tensorflow serving from the repository
    ~~~
    git clone https://github.com/tensorflow/serving
    ~~~
- [OPTIONAL] If you like to create variables in windows powershell here is an example how:
    ~~~
    Set-Variable -Name "MODEL_BASE_PATH" -Value "//C/Users/<your_user>/AppData/Local/Temp/1"
    ~~~
- Launch tensorflow serving in the command prompt with Docker (Remember I am in the Downloads folder)
    ~~~
    docker run -p 8501:8501 -p 8500:8500 --mount type=bind,source=$(pwd)/serving/tensorflow_serving/servables/tensorflow/testdata/saved_model_half_plus_two_cpu,target=/models/half_plus_two -e MODEL_NAME=half_plus_two -t tensorflow/serving
    ~~~
- If the OS tells you that want to share the folder, press `Yes`.
- You should see on powershell the current output
    <details close>
        <summary><b>Output</b></summary>

        2020-09-03 22:46:50.954005: I tensorflow_serving/model_servers/server.cc:87] Building single TensorFlow model file config:  model_name: half_plus_two model_base_path: /models/half_plus_two
        2020-09-03 22:46:50.954319: I tensorflow_serving/model_servers/server_core.cc:464] Adding/updating models.
        2020-09-03 22:46:50.954345: I tensorflow_serving/model_servers/server_core.cc:575]  (Re-)adding model: half_plus_two
        2020-09-03 22:46:51.120633: I tensorflow_serving/core/basic_manager.cc:739] Successfully reserved resources to load servable {name: half_plus_two version: 123}
        2020-09-03 22:46:51.120722: I tensorflow_serving/core/loader_harness.cc:66] Approving load for servable version {name: half_plus_two version: 123}
        2020-09-03 22:46:51.120767: I tensorflow_serving/core/loader_harness.cc:74] Loading servable version {name: half_plus_two version: 123}
        2020-09-03 22:46:51.125018: I external/org_tensorflow/tensorflow/cc/saved_model/reader.cc:31] Reading SavedModel from: /models/half_plus_two/00000123
        2020-09-03 22:46:51.134737: I external/org_tensorflow/tensorflow/cc/saved_model/reader.cc:54] Reading meta graph with tags { serve }
        2020-09-03 22:46:51.134863: I external/org_tensorflow/tensorflow/cc/saved_model/loader.cc:234] Reading SavedModel debug info (if present) from: /models/half_plus_two/00000123
        2020-09-03 22:46:51.137322: I external/org_tensorflow/tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN)to use the following CPU instructions in performance-critical operations:  AVX2 FMA
        To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
        2020-09-03 22:46:51.201657: I external/org_tensorflow/tensorflow/cc/saved_model/loader.cc:199] Restoring SavedModel bundle.
        2020-09-03 22:46:51.243018: I external/org_tensorflow/tensorflow/cc/saved_model/loader.cc:183] Running initialization op on SavedModel bundle at path: /models/half_plus_two/00000123
        2020-09-03 22:46:51.249882: I external/org_tensorflow/tensorflow/cc/saved_model/loader.cc:303] SavedModel load for tags { serve }; Status: success: OK. Took 124880 microseconds.
        2020-09-03 22:46:51.253430: I tensorflow_serving/servables/tensorflow/saved_model_warmup_util.cc:59] No warmup data file found at /models/half_plus_two/00000123/assets.extra/tf_serving_warmup_requests
        2020-09-03 22:46:51.275317: I tensorflow_serving/core/loader_harness.cc:87] Successfully loaded servable version {name: half_plus_two version: 123}
        2020-09-03 22:46:51.280626: I tensorflow_serving/model_servers/server.cc:367] Running gRPC ModelServer at 0.0.0.0:8500 ...
        [warn] getaddrinfo: address family for nodename not supported
        2020-09-03 22:46:51.282416: I tensorflow_serving/model_servers/server.cc:387] Exporting HTTP/REST API at:localhost:8501 ...
        [evhttp_server.cc : 238] NET_LOG: Entering the event loop ...

    </details>


- Ensure the container is runing, type this on Windows Powershell
    ~~~
    docker container list
    ~~~
- You should see something similar to the next output
    ~~~
    CONTAINER ID        IMAGE                COMMAND                  CREATED             STATUS              PORTS                              NAMES
    3a0bc4167285        tensorflow/serving   "/usr/bin/tf_serving…"   21 minutes ago      Up 21 minutes       8500/tcp, 0.0.0.0:8501->8501/tcp   compassionate_leavitt
    ~~~

Install Curl for Windows
- Go to this address and [download curl for windows](https://curl.haxx.se/windows/)
- Unzip to a folder named curl, for example in the Downloads folder
- Cut and paste the folder to `C:\Program Files`
- Go to your environental variables and on the `Path` variable add `C:\Program Files\curl\bin`, then press OK and OK again.
- Test curl opening a `cmd` (Windows+R, then write `cmd`, then ENTER).
- Write `curl --help`, you should se an output

[OPTIONAL] Install wget on Windows
- Go to this address and [download wget for windows](http://gnuwin32.sourceforge.net/packages/wget.htm) by [downloading binaries](http://downloads.sourceforge.net/gnuwin32/wget-1.11.4-1-bin.zip) and [dependencies files](http://downloads.sourceforge.net/gnuwin32/wget-1.11.4-1-dep.zip).
- Unzip to a folder named wget each zip, for example in the Downloads folder
- Cut and paste the folder to `C:\Program Files`
- Go to your environental variables and on the `Path` variable add `C:\Program Files\wget\bin`, then press OK and OK again.
- Test wget opening a `cmd` (Windows+R, then write `cmd`, then ENTER).
- Write `wget --help`, you should se an output

Testing Tensorflow Server
- Close the cmd prompt if open and open it again
- Run this command
    ~~~
    curl -d "{\"instances\": [1.0, 2.0, 5.0]}" -X POST http://localhost:8501/v1/models/half_plus_two:predict
    ~~~
- The served model gets the inputs, divide by two and add two. You should see the next output
    ~~~
    {
        "predictions": [2.5, 3.0, 4.5
        ]
    }
    ~~~

Stopping the Docker Tensorflow Server

- First list the containers that are up and running
    ~~~
    docker container list
    ~~~
- You should see the next output
    ~~~
    CONTAINER ID        IMAGE                COMMAND                  CREATED             STATUS              PORTS                              NAMES
    3a0bc4167285        tensorflow/serving   "/usr/bin/tf_serving…"   21 minutes ago      Up 21 minutes       8500/tcp, 0.0.0.0:8501->8501/tcp   compassionate_leavitt
    ~~~
- Next stop the server
    ~~~
    docker stop 3a0bc4167285
    ~~~
</details>


<details open>
<summary> <b>Training and Deploying Fashion MNIST with Tensorflow Serving<b></summary>

- NOTES: 
    - I assume you completed the previous steps
    - For this example I am in the `Downloads` Folder of my PC.

- Training the Model
    - Run the file TrainAndSaveModel
        ~~~
        python TrainAndSaveModel.py
        ~~~
        
    - This will give you an output like

        <details close>
        <summary> <b>Output<b></summary>

            2020-09-03 18:32:00.032216: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'cudart64_101.dll'; dlerror: cudart64_101.dll not found
            2020-09-03 18:32:00.042233: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
            2.3.0

            train_images.shape: (60000, 28, 28, 1), of float64
            test_images.shape: (10000, 28, 28, 1), of float64
            2020-09-03 18:32:25.811847: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'nvcuda.dll'; dlerror: nvcuda.dll not found
            2020-09-03 18:32:25.843324: W tensorflow/stream_executor/cuda/cuda_driver.cc:312] failed call to cuInit: UNKNOWN ERROR (303)
            2020-09-03 18:32:25.878382: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:169] retrieving CUDA diagnostic information for host: DESKTOP-SEL3I01
            2020-09-03 18:32:25.888706: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:176] hostname: DESKTOP-SEL3I01
            2020-09-03 18:32:25.986509: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN)to use the following CPU instructions in performance-critical operations:  AVX2
            To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
            2020-09-03 18:32:26.726943: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x1fba6949eb0 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
            2020-09-03 18:32:26.770629: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
            Model: "sequential"
            _________________________________________________________________
            Layer (type)                 Output Shape              Param #
            =================================================================
            Conv1 (Conv2D)               (None, 13, 13, 8)         80
            _________________________________________________________________
            flatten (Flatten)            (None, 1352)              0
            _________________________________________________________________
            Softmax (Dense)              (None, 10)                13530
            =================================================================
            Total params: 13,610
            Trainable params: 13,610
            Non-trainable params: 0
            _________________________________________________________________
            Epoch 1/5
            1875/1875 [==============================] - 5s 3ms/step - loss: 0.5349 - accuracy: 0.8140
            Epoch 2/5
            1875/1875 [==============================] - 5s 3ms/step - loss: 0.3942 - accuracy: 0.8620
            Epoch 3/5
            1875/1875 [==============================] - 5s 3ms/step - loss: 0.3596 - accuracy: 0.8734
            Epoch 4/5
            1875/1875 [==============================] - 5s 3ms/step - loss: 0.3396 - accuracy: 0.8796
            Epoch 5/5
            1875/1875 [==============================] - 5s 3ms/step - loss: 0.3247 - accuracy: 0.8839
            313/313 [==============================] - 1s 2ms/step - loss: 0.3553 - accuracy: 0.8732

            Test accuracy: 0.873199999332428
            export_path = C:\Users\issaiass\AppData\Local\Temp\1

            WARNING:tensorflow:From C:\Users\issaiass\anaconda3\envs\tf\lib\site-packages\tensorflow\python\training\tracking\tracking.py:111: Model.state_updates (from tensorflow.python.keras.engine.training) is deprecated and will be removed in a future version.
            Instructions for updating:
            This property should not be used in TensorFlow 2.0, as updates are applied automatically.
            2020-09-03 18:33:02.444038: W tensorflow/python/util/util.cc:348] Sets are not currently considered sequences, but this may change in the future, so consider avoiding using them.
            WARNING:tensorflow:From C:\Users\issaiass\anaconda3\envs\tf\lib\site-packages\tensorflow\python\training\tracking\tracking.py:111: Layer.updates (from tensorflow.python.keras.engine.base_layer) is deprecated and will be removed in a future version.
            Instructions for updating:
            This property should not be used in TensorFlow 2.0, as updates are applied automatically.

            Saved model:
            ['assets', 'saved_model.pb', 'variables']
        </details>

    - Note the model outpt is in: 
        ~~~
        C:\Users\<your_user>\AppData\Local\Temp\1
        ~~~
- Running the tensorflow serving container
    - Run the command below to start the server
        ~~~
        docker run -p 8501:8501 -p 8500:8500 --mount type=bind,source=//C/Users/issaiass/AppData/Local/Temp,target=/models/fashion_mnist -e MODEL_NAME=fashion_mnist -t tensorflow/serving
        ~~~
    - This will give you this output
        <details close>
        <summary> <b>Output<b></summary>

        2020-09-03 23:44:07.641855: I tensorflow_serving/model_servers/server.cc:87] Building single TensorFlow model file config:  model_name: fashion_mnist model_base_path: /models/fashion_mnist
        2020-09-03 23:44:07.642183: I tensorflow_serving/model_servers/server_core.cc:464] Adding/updating models.
        2020-09-03 23:44:07.642212: I tensorflow_serving/model_servers/server_core.cc:575]  (Re-)adding model: fashion_mnist
        2020-09-03 23:44:14.674936: I tensorflow_serving/core/basic_manager.cc:739] Successfully reserved resources to load servable {name: fashion_mnist version: 1}
        2020-09-03 23:44:14.675014: I tensorflow_serving/core/loader_harness.cc:66] Approving load for servable version {name: fashion_mnist version: 1}
        2020-09-03 23:44:14.675049: I tensorflow_serving/core/loader_harness.cc:74] Loading servable version {name: fashion_mnist version: 1}
        2020-09-03 23:44:14.676700: I external/org_tensorflow/tensorflow/cc/saved_model/reader.cc:31] Reading SavedModel from: /models/fashion_mnist/1
        2020-09-03 23:44:14.684050: I external/org_tensorflow/tensorflow/cc/saved_model/reader.cc:54] Reading meta graph with tags { serve }
        2020-09-03 23:44:14.684108: I external/org_tensorflow/tensorflow/cc/saved_model/loader.cc:234] Reading SavedModel debug info (if present) from: /models/fashion_mnist/1
        2020-09-03 23:44:14.685944: I external/org_tensorflow/tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN)to use the following CPU instructions in performance-critical operations:  AVX2 FMA
        To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
        2020-09-03 23:44:14.726331: I external/org_tensorflow/tensorflow/cc/saved_model/loader.cc:199] Restoring SavedModel bundle.
        2020-09-03 23:44:14.778317: I external/org_tensorflow/tensorflow/cc/saved_model/loader.cc:183] Running initialization op on SavedModel bundle at path: /models/fashion_mnist/1
        2020-09-03 23:44:14.789234: I external/org_tensorflow/tensorflow/cc/saved_model/loader.cc:303] SavedModel load for tags { serve }; Status: success: OK. Took 112588 microseconds.
        2020-09-03 23:44:14.793297: I tensorflow_serving/servables/tensorflow/saved_model_warmup_util.cc:59] No warmup data file found at /models/fashion_mnist/1/assets.extra/tf_serving_warmup_requests
        2020-09-03 23:44:14.801450: I tensorflow_serving/core/loader_harness.cc:87] Successfully loaded servable version {name: fashion_mnist version: 1}
        2020-09-03 23:44:14.804189: I tensorflow_serving/model_servers/server.cc:367] Running gRPC ModelServer at 0.0.0.0:8500 ...
        [warn] getaddrinfo: address family for nodename not supported
        2020-09-03 23:44:14.805312: I tensorflow_serving/model_servers/server.cc:387] Exporting HTTP/REST API at:localhost:8501 ...
        [evhttp_server.cc : 238] NET_LOG: Entering the event loop ...
        </details>
    - Next on the cmd prompt run this command
        ~~~
        python TestServer.py
        ~~~
    - You should see the current output
        <details close>
        <summary> <b>Output<b></summary>    
        ~~~
        2020-09-03 18:58:17.434740: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'cudart64_101.dll'; dlerror: cudart64_101.dll not found
        2020-09-03 18:58:17.451207: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
        test_images.shape: (10000, 28, 28, 1), of float64

        Testing A single Request

        Data: {"signature_name": "serving_default", "instances": ...  [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0]]]]}


        Ground Truth = Ankle boot class 9, Prediction = Ankle boot class 9


        Testing multiple requests

        Ground Truth = Ankle boot class 9, Prediction = Ankle boot class 9
        Ground Truth = Pullover class 2, Prediction = Pullover class 2
        Ground Truth = Trouser class 1, Prediction = Trouser class 1
        ~~~
        </details>

- Stopping the Docker Tensorflow Server

  - First list the containers that are up and running
    ~~~
    docker container list
    ~~~
  - You should see the next output
    ~~~
    CONTAINER ID        IMAGE                COMMAND                  CREATED             STATUS              PORTS                              NAMES
    3a0bc4167285        tensorflow/serving   "/usr/bin/tf_serving…"   21 minutes ago      Up 21 minutes       8500/tcp, 0.0.0.0:8501->8501/tcp   compassionate_leavitt
    ~~~
  - Next stop the server
    ~~~
    docker stop 3a0bc4167285
    ~~~
</details>

<details open>
<summary> <b>Video Explanation<b></summary>

You could see the results on this youtube video where I explain the usage of this repository.

<p align="center">

[<img src= "https://img.youtube.com/vi/qaJqO5TvJqw/0.jpg" />](https://youtu.be/qaJqO5TvJqw)

</p>

</details>

>

<details open>
<summary> <b>Issues<b></summary>

Currently are no issues present.

</details>

<details open>
<summary> <b>Contributiong<b></summary>

Your contributions are always welcome! Please feel free to fork and modify the content but remember to finally do a pull request.

</details>

<details open>
<summary> :iphone: <b>Having Problems?<b></summary>

<p align = "center">

[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/riawa)
[<img src="https://img.shields.io/badge/telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/>](https://t.me/issaiass)
[<img src="https://img.shields.io/badge/instagram-%23E4405F.svg?&style=for-the-badge&logo=instagram&logoColor=white">](https://www.instagram.com/daqsyspty/)
[<img src="https://img.shields.io/badge/twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" />](https://twitter.com/daqsyspty) 
[<img src ="https://img.shields.io/badge/facebook-%233b5998.svg?&style=for-the-badge&logo=facebook&logoColor=white%22">](https://www.facebook.com/daqsyspty)
[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/riawe)
[<img src="https://img.shields.io/badge/tiktok-%23000000.svg?&style=for-the-badge&logo=tiktok&logoColor=white" />](https://www.linkedin.com/in/riawe)
[<img src="https://img.shields.io/badge/whatsapp-%23075e54.svg?&style=for-the-badge&logo=whatsapp&logoColor=white" />](https://wa.me/50766168542?text=Hello%20Rangel)
[<img src="https://img.shields.io/badge/hotmail-%23ffbb00.svg?&style=for-the-badge&logo=hotmail&logoColor=white" />](mailto:issaiass@hotmail.com)
[<img src="https://img.shields.io/badge/gmail-%23D14836.svg?&style=for-the-badge&logo=gmail&logoColor=white" />](mailto:riawalles@gmail.com)

</p

</details>

<details open>
<summary> <b>License<b></summary>
<p align = "center">
<img src= "https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg" />
</p>
</details>