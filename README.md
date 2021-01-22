# text-similarity
# A simple web application to compute the similarity between two text samples. 

## Approach
There are many ways to go about computing the similarity between two texts. The simplist appraoch possible would be to compare words at each location within the text and count up the number of matches. A more state of the art approach could be to train a deep neural network to encode the meaning of the phrases and output a similarity. The approach taken here is very naiive. The general idea is to determine similarity based on how close in position two words occur between the texts. 

## How to run
This app has been placed within a Docker container and pushed to docker hub. In order to run it, the container can be pulled and run as follows: 

1. Run command `docker pull paulrtobin/text-similarity-app`

2. Run container with command:

`docker run -p 5000:5000 text_sim_image`


