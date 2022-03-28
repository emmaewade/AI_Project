```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```

## Installing miniconda

Miniconda is an environment manager tool that makes it easier for us to install software including dadi and many other bioinformatic tools. So I recommend that first of all you guys install miniconda as the following in your directories, by typing the following in the terminal:

```{bash, eval=F}
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```

Now try to run conda version as:

```{bash, eval=F}
conda --version
```
if it worked, you have successfully managed to install conda :D ! 

If it doesn't try this, and try again

```{bash, eval=F}
export PATH=~/miniconda3/bin:$PATH
```

Now that we have conda installed, we will create an environment especially for this given project. You can call it anything, and I will call it "summer_project". In this project we will add every software needed for our analyses during the summer project, so whenever you work on the cluster you will have those packages organized and ready to be used in the given environment. And the most import, you will have version control of your analyses!

To do so, we need to call conda and tell it to create a new environment as:

```{bash, eval=F}
conda create --name summer_project
```

To learn more about what conda can do, please access [here](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

Now that we have created our conda environment to be able to use it we need to **"activate"** it. To do so we type:

```{bash, eval=F}
conda activate summer_project

```

if this doesn't work, try this one

```{bash, eval=F}
source activate summer_project

```

if you have successfully installed and activated this environment you will see at the left most side of the screen the name of the project followed by your username. 

Perfect! Now we can install **inside of this environment** all the other packages we will be using to run fitdadi. 

We start it by installing dadi. If we look at the website for the dadi software [here](https://dadi.readthedocs.io/en/latest/user-guide/installation/), they recommend that we use the following code:

```{bash, eval=F}
conda install -c conda-forge hmmlearn
```

These will also probably be needed (there's a way to install all of these when you create your environment, but I'm adding as I go :) )

```{bash, eval=F}
conda install -c conda-forge pandas
conda install -c conda-forge numpy
conda install -c conda-forge seaborn
conda install -c conda-forge matplotlib
```

It requires that we install multiple packages (dependencies), you just need to type 'y' and enter to proceed with the installation. 
To check whether dadi was successfully installed, we can just call the software on terminal. Since it is a python module, than you should first call python:

```{bash, eval=F}
python
import hmmlearn
```


If it does not complain, then you have succeed on its installation. Congratulations!!!
