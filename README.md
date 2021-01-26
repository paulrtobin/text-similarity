# text-similarity-app by Paul Tobin
## A simple web application to compute the similarity between two text samples. 

## Approach
There are many ways to go about computing the similarity between two texts. The simplest approach possible would be to compare words at each location within the text and count up the number of matches. A more state of the art approach could be to train a deep neural network to encode the meaning of the phrases and output a similarity. The approach taken here is very naiive. For each word in the first text sample, that word is searched for in the second text. If the matching words occur in the same position, a score of 1 is given. If the word doesn't exist in the second text, a score of 0 is given. If the same word occurs in each text but they occur at different positions, a score between 0 and 1 is calculated where the score is higher if the positions are closer. Additionally, everytime there are two matches in a row, an additional score of 1 is given in an attempt to reward sequences of matching words even if the positions are different between the two texts. To compute the overall similarity metric, all of the scores given throughout this process are averaged. 

**Additional details:** The input text strings are broken into individual tokens based on whitespace and the puncuation characters: '.', ',', '?', and '!'. So each word is it's own token and each of the previously listed punctuation marks get their own tokens. These tokens were chosen because they are the most common and significantly impact the meaning of the text.  

## How to run
This app has been placed within a Docker container and pushed to docker hub. In order to run it, the container can be pulled and run as follows: 

### 1. **Run command** `docker pull paulrtobin/text-similarity-app`

---

### 2. **Run container with command:** `docker run -p 5000:5000 text_sim_image`

The output should look similar to this:

   ```
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
   ```

---

### 3. **Open http://0.0.0.0:5000/ in a web browser. The page will look like this:** 

![home_image](/docs/Home_page.png)

---

### 4. **Enter some text in the text fields that you'd like to compare, here's an example:**

![text_image](/docs/Entry_example.png)

---

### 5. **Press Go!**

The similarity calculation will run and you will be redirected to a page showing the results that should look like this: 

![GitHub Logo](/docs/Results_page.png)
