# Machine Learning
## Transfer Learning ##  
Here I used a pretrained ResNet50 and part of the CIFAR100 dataset for a transfer learning side project.  
Classifying man, woman, boy and girl as "person" and streetcarsas "car".  
Steps:  
 - Loading the cifar dataset  
 - Coosing the relevant classes  
 - Loading the Resnet50 model(pre trained weights, without last layer)  
  - Resizing the CIFAR images and splitting the data to training and validation(75:25)  
  - Adding a Softmax layer for my classification("person" / "car")  
  - Training the model  
  
  
## RecongnitionOfRussianBots ##  
This is our final software engineering project.  
Here Eugeny(my partner), Prof. Valery(our supervisor), Prof. Zeev(our advisor) and my humble self are trying to distinguish between human and bot written tweets using first derivative word saliency.  

