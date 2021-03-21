## Python code generator from text prompts using Transformer

### DATA PREPROCESSING
#### Data cleaning:
* Initially each of the examples were segregated such a way that, for each of the programs the “objective” begins with a “#” character. This is the only way to list out all the examples separately. The constraint in this procedure is there can be comments also starting with the character “#”. So, keeping these things in mind we have segregated each different example.
* Once we have the examples, we have to separate the code part and the objective. By using the same logic that the objective will have a “#” in the beginning the code and objective separation was done and from the objective the first character which is “#” is also removed.
* Now for the code part we have to take care of escape sequences like new line, tab and spaces. In the provided dataset, a lot of inconsistencies are there for the indentation part, where in some case “tab” was used for it and for some cases “space” was it and sometimes for first level of indentation 3 “space”s are used and for second level of indentation 7”space”s were used. So, all these inconsistencies are removed and all the “tab”s are replaced with 4 “space”s and the indentations are represented as multiple of 4 “space”s.
* Finally we created a list of dictionaries where the “obj” represents the objective of the code and “code” represents the code part in a dictionary format.


Please follow the files in the link for the pro-precessing steps [preprocessing](https://github.com/rubelchowdhury20/END-NLP/tree/master/codes/session-14/data%20preprocessing) .

#### Data extension strategy:
The data extension strategy we thought of was, using the token type information from each of the tokens in the code to generate synthetic data. To explain it better, we can get all the variable names in the code and use a different name based on the type of the variable. To implement this strategy a lot of possibilities we have to keep in mind. So, because of time constraints we haven't implemented it here.

#### Embedding training:
* We have randomly chosen 5000 files out of 68k python files from “Raw Python Code Corpus” to create a corpus.
* The corpus is tokenized using pygments tokenizer.
* The training notebook is given [here](https://github.com/rubelchowdhury20/END-NLP/blob/master/codes/session-14/glove%20embedding%20training.ipynb)


We have trained our embeddings for very few epochs because of the limitation of the resource and because of that we didn’t see much of a difference, without using the trained embeddings. Given the embeddings trained on a bigger corpus size for a larger number of epochs, it might have given a better performance. So, for this experiment we haven't used any pretrained embeddings and went ahead with training the embedding in the embedding layer of the Transformer only.


### ARCHITECTURE EXPERIMENTS
Transformer model demonstrates excellent performance for normal text but in the given problem, the python script has a different pattern compared to normal text. This pattern/structure is attributed to the syntax and keywords that need to be used is a predetermined order. 
For the model to produce good results, it needs to understand and learn the syntax i.e., patterns like: 
* ‘def’ keyword needs to be followed by a variable name. 
* A variable can hold different data types, string, int, float
* Keywords like ‘if’ and ‘else’ come together etc.

We observed that a classic transformer model was not efficiently learning this. This information needs to be learnt or explicitly fed to model for good performance. To enforce this, we hypothesised that adding this token type information into the model may help. We extracted  token type information from the [Pygments](https://pygments.org/) package which is a syntax highlighting package. We used this to obtain tokens and token type from the code snippets. Broad categories of token types are:

![code 1](https://i.imgur.com/4402wr8.png)

This has a vocabulary of 28 token types. To add this to the model, we created token type embedding with dim = 10, combined it with the combination of token and position embedding using a fully connected layer and fed to the transformer model. There is room of experimentation in the way these token type embedding is added to the input. We observed that this technique worked the best. The intuition is that the model is reinforced to learn the syntax of keywords and how they are combined to produce syntactically correct results.

To ensure the model is learning this pattern, we wanted to ensure that the loss function is also driving the model in this direction. So, we extended the output of the model to also predict the sequence of token types corresponding to the sequence of predicted tokens. The cross entropy loss between the predicted and target token type was added to the cross entropy loss between the  predicted and target tokens. Essentially, optimizing the sum of two losses. The intuition to this approach was that the model is forced to predict the correct token type(whether it is a string or a keyword or an integer etc) if not the correct token. We confined the experiments to using cross entropy loss and focussed on ways to ensure that the model learns the specific structure in the dataset as the difference in this problem is the data type and not the prediction format.

Another approach to this problem would be to train the embedding using a larger corpus of python code, using the token type information to learn the embedding. This seemed far-fetched an idea for the given time frame as embedding training using the GloVe algorithm with the above mentioned corpus was too expensive in terms of time and resources. Besides, the window size can be arbitrarily large in python code.To counter this, we considered using variable window size and combining the results. In any case, it required a lot of time and resources for a large corpus. If we were to use just our dataset, we would be overfitting the data. So we omitted this.

We reduced the capacity of the model to reduce the complexity as we had limited dataset. We further reduced the encoder capacity as the text input to the encoder is short and simple. Other regularization techniques like L2 regularization produced worse results. So stuck to Dropout regularization.

### ANALYSIS
* It is observed that the model performs well for small simple code snippets.

![code 2](https://i.imgur.com/30sbGqf.png)

![code 3](https://i.imgur.com/DnWm6uM.png)

* In some cases, the algorithm is incorrect but close to the concept.

![code 4](https://i.imgur.com/kkH4wMe.png)

* But the results are going for a toss for larger, more complex programs. It is observed that those programs that require indexing data structures like dictionaries or lists are producing syntactically incorrect results(indentation, bracket pairs are messed up, etc). 

![code 5](https://i.imgur.com/qsvyxpD.png)

* From one of the examples to predict area of square, it can be observed that the word ‘area’ has high correlation with ‘side’, ‘*’, ‘*’, ‘2’ in the attention matrix which speaks to the performance of the model.

![code 6](https://i.imgur.com/gWc6b0a.png)

* One major problem with this was overfitting that could not be resolved.

*All these problems can be tackled by getting more data and training with more parameters.*

### SCOPE FOR IMPROVEMENT

* Another tangential thought would be to focus on ways to train the embedding using python syntactic rules.
* We could also use different data structures to represent python code. For example, it may help to pass code snippets as Abstract Syntax Tree(AST) so the model can learn the understanding of the structure from the hierarchy point of view.







