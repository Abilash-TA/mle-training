# Use a Ubuntu base image
FROM ubuntu:latest

# Install python3 and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Setting the author name
LABEL author = "Abilash"

# Copy the file to which contains all the required packages
COPY requirements.txt .

# Copy the wheel file of package we created
COPY housinglib-0.1.0-py3-none-any.whl .

COPY scripts/* .


# Install all the required packages
RUN pip install -r requirements.txt

# Install the wheel file
RUN pip install housinglib-0.1.0-py3-none-any.whl

# Setting working direactery
WORKDIR /mle-training

# Copy the project files
COPY . /mle-training

# Expose port for MLflow UI
EXPOSE 5000
# Start the MLflow server first then run the python script
CMD ["bash","run.sh"]
