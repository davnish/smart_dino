<div align = 'center'>

# smart_dino
<p><img src="misc/dino_model_7.gif" width="500" /></p>

This is the pytorch implementation of the DQN algorithm which is used to solve the chrome's dino game.
Chrome's dino environment is captured through [selenium](https://selenium-python.readthedocs.io/).

</div>

## files/folders structure

```
.
├── .gitignore
├── DQN.py (Implementation of DeepQLearning class and createNetwork class)
├── README.md
├── dino.png (temporary image file, which will be created and updated while running the env, which will be feed to the model)
├── dino_env.yml (requirements file for creating the conda env)
├── env.py (Class implementation of WebDino, which containes all the necessary functions and attributes for creating the environment)
├── main.py (Here all the classes come together and the model is sent into training)
├── misc
│   └── dino_model.gif
├── results
│   ├── DQ.png
├── models (Contains the pretrained model)
│   ├── ckpt.pt 
└── vis.py
```

## overview architecture
<p align="center">
<img width="1000" alt="overview_arch" src="https://github.com/davnish/smart_dino/blob/main/misc/overview_lat.jpg">
</p>

## dependencies
- `pytorch`
- `selenium` for interacting with the browser.
- `pandas` for creating and storing rewards graphs.
- `pillow` for the taking the screenshots on a specified location on display.
- `opencv` for image processing before feeding to model.

## install
> [!Important]
> To install conda or miniconda follow this [link](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)

If you have conda already installed, then to create the separate env which will contain all the necessary libraries run the below commands.
```
git clone https://github.com/davnish/smart_dino # cloning the repo
cd smart_dino # Moving inside the repo
conda env create --name dino --file=dino_env.yml # Installing the libraries
```
Then just activate the environment by, 
```
conda activate dino
```

