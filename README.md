# DeepCAN
Precise and quick monitoring of key cytometric features such as cell count, cell size, cell morphology and DNA content is crucial for life research and development. Cytometry is important for numerous applications in biotechnology, medical sciences, and cell culture research laboratories. Flow cytometry that relies on aligning cell flow and their characterization by optical or electrical detection has been the dominant cytometry approach for high throughput applications. Recent advances in digital microscopy revealed image cytometry as a viable alternative that can lead to simpler, more compact and less expensive solutions. Traditionally, image cytometry relies on the use of a hemocytometer accompanied with visual inspection of an operator under the microscope. This approach is prone to error due to subjective decisions of the operator. Machine learning approaches have recently emerged as powerful tools enabling quick and highly accurate image cytometric analysis that are easily generalizable to different cell types. Here, we demonstrate a modular deep learning system (DeepCAN) that provides a complete solution for automated cell counting and viability analysis. DeepCAN employs three different neural network blocks called Parallel Segmenter, Cluster CNN, and Viability CNN that are trained for initial segmentation, cluster separation, and cell viability analysis, respectively. Parallel Segmenter and Cluster CNN blocks achieve highly accurate segmentation of individual cells while Viability CNN block performs viability classification A modified U-Net network, a well-known deep neural network model for bio-image analysis, is used in Parallel Segmenter while LeNet-5 architecture and itss modifid versions are used for Cluster CNN and Viability CNN, respectively. We trained the Parallel Segmenter using 15 images of A2780 cells and 5 images of yeasts cells containing 14742 individual cell images. Similarly, 6101 and 5900 A2480 cell images were employed for training of Cluster CNN and Viability CNN models. 2514 individual A2780 cell images were used to test the overall segmentation performance of Parallel Segmenter combined with Cluster CNN, revealing a high precision of 96.52%. Overall cell counting/viability analysis performance of DeepCAN was tested with A2780 (2514 cells), A549 (601 cells), Colo (356 cells), and MDA-MB-231 (857 cells) cell images revealing high counting/viability accuracies of 93.82 %/95.93 %, 92.18 %/97.90 %, and 85.32 %/97.40 %, respectively.

 
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6278011.svg)](https://doi.org/10.5281/zenodo.6278011)
