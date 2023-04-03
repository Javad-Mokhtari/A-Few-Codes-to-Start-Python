# **Machine Learning Classic Algorithms from Scratch**

## Naive Bayes
<p align="justify">Naive Bayes is a probabilistic algorithm used for classification tasks. It is based on Bayes' theorem, which provides a way to calculate the probability of a hypothesis given evidence. Naive Bayes assumes that the features are independent of each other, which is not always true in real-world scenarios. Despite this, it is often used in practical applications because of its simplicity and efficiency. Naive Bayes can handle large datasets and has low computational cost.
</p>

## KNN (K-Nearest Neighbors)
<p align="justify">KNN is a non-parametric algorithm used for both classification and regression tasks. It works by finding the k-nearest neighbors 
to a new data point, and then using the labels or values of those neighbors to predict the label or value of the new point. KNN can be computationally expensive, especially with large datasets, but it can be an effective algorithm when the underlying structure of the data is complex.</p>

## K-means
<p align="justify">K-means is a clustering algorithm that partitions a dataset into k clusters. It works by iteratively assigning each data point to the cluster whose centroid is closest, and then updating the centroids based on the new assignments. K-means is a simple and fast algorithm, but it can be sensitive to the initial choice of centroids and can sometimes converge to a suboptimal solution.
</p>

## MLP (Multi-Layer Perceptron)
<p align="justify">MLP is a type of artificial neural network that is used for both classification and regression tasks. It consists of multiple layers of interconnected neurons, where each neuron computes a weighted sum of its inputs and applies a non-linear activation function. MLP is a powerful algorithm that can learn complex relationships in data, but it can be prone to overfitting and can require careful tuning of its hyperparameters.
</p>

## RBF (Radial Basis Function):
<p align="justify">RBF is a type of artificial neural network that is used for both classification and regression tasks. It consists of multiple layers of neurons, where each neuron applies a radial basis function to its inputs. RBF is a powerful algorithm that can learn complex relationships in data, but it can be computationally expensive and can require careful tuning of its hyperparameters.
</p>

## SOM (Self-Organizing Map)
<p align="justify">SOM is an unsupervised learning algorithm used for clustering and visualization tasks. It works by mapping a high-dimensional input space onto a low-dimensional grid of neurons, where each neuron represents a region of the input space. SOM is a powerful algorithm for visualizing high-dimensional data, but it can be sensitive to the initial configuration of the map and can require careful tuning of its hyperparameters.</p>

## Mixture of Experts (MoE)
<p align="justify">Mixture of Experts is a machine learning technique used for modeling complex relationships between inputs and outputs in a data set. The MoE approach combines the predictions of multiple "experts" models, each specialized in a particular subset of the data, to create a final prediction that is more accurate and robust than the prediction of any individual model. The MoE technique involves two main components: gating and expert models. The gating model, which is typically a neural network, is responsible for determining which expert model(s) should be used to predict the output for a given input. The gating model takes in the input and outputs a set of probabilities indicating the relevance of each expert model for this input. The expert models are typically simpler models, such as linear regression models or decision trees, that are trained on specific subsets of the data to learn a specialized aspect of the relationship between inputs and outputs.</p>
<p align="justify">The overall MoE model is created by combining the predictions of the expert models using the probabilities outputted by the gating model. Specifically, the final prediction is a weighted sum of the predictions of each expert model, where the weights are the probabilities outputted by the gating model. MoE models have been successfully used in a variety of applications, including speech recognition, image classification, and natural language processing. One of the advantages of the MoE approach is that it can handle complex relationships between inputs and outputs, as well as situations where different inputs require different models to make accurate predictions. However, MoE models can be more difficult to train and tune than simpler models, and may require larger amounts of data and computational resources.</p>
