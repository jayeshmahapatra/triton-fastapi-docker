# Notebooks

This folder contains Jupyter notebooks that demonstrate different aspects of the machine learning workflow for the bee vs ant classification task. 

## Folder Structure

The notebooks folder has the following structure:

```
notebooks/
├── bee_vs_ant_example.ipynb
└── LICENSE
```

- **bee_vs_ant_example.ipynb**: This Jupyter notebook (`bee_vs_ant_example.ipynb`) is used to finetune a pre-trained ResNet18 model to classify bees vs ants. The code in this notebook is based on the official PyTorch finetuning tutorial, which can be found [here](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html?highlight=transfer%20learning%20ant%20bees). It includes additional code to convert the trained model into a TorchScript model and save it in the Triton model repository for our Triton service.

- **LICENSE**: The `LICENSE` file contains the license for the PyTorch tutorial code. As the code is licensed under the BSD 3-Clause License, this subfolder is also licensed under the same license.

## Running the Example


- **bee_vs_ant_example.ipynb**: This Jupyter notebook (`bee_vs_ant_example.ipynb`) is used to finetune a pre-trained ResNet18 model to classify bees vs ants. The code in this notebook is based on the official PyTorch finetuning tutorial, which can be found [here](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html?highlight=transfer%20learning%20ant%20bees). It includes additional code to convert the trained model into a TorchScript model and save it in the Triton model repository for our Triton service.

- **LICENSE**: The `LICENSE` file contains the license for the PyTorch tutorial code. As the code is licensed under the BSD 3-Clause License, this subfolder is also licensed under the same license.

## Running the Example

To run the example notebook (`bee_vs_ant_example.ipynb`), make sure you have the following dependencies installed:

- torch
- numpy
- matplotlib
- torchvision

Please install these dependencies before running the notebook. You can use package managers like pip or conda to install them.

Once you have the dependencies installed, follow these steps:

1. First, download the sample bee vs ant dataset from the following [link](https://download.pytorch.org/tutorial/hymenoptera_data.zip) and extract it inside the `data` folder in the root of the repository. Make sure the extracted dataset folder is named `hymenoptera_data`.

2. Open the `bee_vs_ant_example.ipynb` notebook in Jupyter or a compatible environment.

3. Follow the instructions in the notebook to execute the code cells sequentially. The notebook provides step-by-step guidance on finetuning the model, saving it as a TorchScript model, and preparing it for deployment with Triton.

Please note that the example notebook assumes that you have set up the necessary environment and dependencies mentioned in the main repository readme.

## License

The content in this subfolder is licensed under the BSD 3-Clause License. Please refer to the [LICENSE](LICENSE) file for more information.