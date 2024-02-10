
# MediaEval 2023- NewsImages

This repository contains an implementation of the NewsImages task of MediaEval 2023, using CLIP (Contrastive Language-Image Pretraining). It aims to match news articles with the most appropriate header image.


The Mean Reciprocal Rank (MRR) is used to evaluate the rank of of each predicted image against the ground truth.



## Model

 CLIP learns a shared embedding space for images and their corresponding textual descriptions, fostering a unified understanding of multimodal relationships. The contrastive learning framework enhances the model's robustness by maximizing the similarity of correct image-text pairs and minimizing the similarity of incorrect pairs. CLIP's capability for zero-shot learning helps in scenarios with diverse datasets, such as news articles with varying topics.


 The model is composed of three main sections-the image encoder, text encoder, and a module for the projection of the embeddings. 


 



## Results

The results across datasets are summarized in the table below:


| Metric              	| Baseline 	| GDELT-P1 	| GDELT-P2 	|
|---------------------	|----------	|----------	|----------	|
| matchIn100          	| 100/1500 	| 796/1500 	| 886/1500 	|
| MeanReciprocalR100  	| 0.00346  	| 0.07839  	| 0.09134  	|
| MeanReciprocalAt5   	| 0.00333  	| 0.10933  	| 0.12600  	|
| MeanReciprocalAt10  	| 0.00667  	| 0.16867  	| 0.20257  	|
| MeanReciprocalAt50  	| 0.03333  	| 0.40600  	| 0.45533  	|
| MeanReciprocalAt100 	| 0.06667  	| 0.53067  	| 0.59067  	|
## Examples

The code returns the top 100 images for a given news heading, in order of decreasing relevance. 

For example, the statement:



"Oxford researcher to watch Barbie as 'dessert' to Oppenheimer amid dual premiere"

yields the following results:





## Authors

- [Pooja Premnath](https://github.com/PoojaPremnath2003)
- [Y.V. Ojus](https://github.com/Ojus999)



## Acknowledgements


1. A. Lommatzsch, B. Kille, Ö. Özgöbek, M. Elahi, D.-T. Dang-Nguyen, News images in mediaeval 2023, in: Proceedings of the MediaEval Benchmarking Initiative 2023, CEU Workshop Proceedings,2024
2. M. M. Shariatnia, Simple CLIP, 2021. doi:10.5281/zenodo.6845731.






