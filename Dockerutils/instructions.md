
## Basic instructions of a python jupyter working environment


### Download the data

This repository has the basic data for run a python jupyter data science environment.

```bash
git clone https://github.com/tgquintela/educational-scripts/tree/master/Dockerutils
```
The files of that repository are:
* `instructions.md`: the current file of instructions.
* `Dockerfile`: the basic file to build a python data science container.

### Build an image

Using the Dockerfile present in the folder you are going to create a specific image to work with.

```bash
docker build . -t name_of_image:latest
```

You should use the proper `name_of_image`.

### Run the environment

To run the environment and create the
You should follow the next steps:
* Do the previous steps.
* Have your input data in a folder `data/input` and other data in your folder `data/`.

After that you can run the following command.

```bash
docker run -rm --name name_of_container -v /path/to/data:/working -p 8888:8888 -it name_of_image
```

You should substitute `name_of_container`, `/path/to/data` and `name_of_image` by the names and path suitable for your project.
