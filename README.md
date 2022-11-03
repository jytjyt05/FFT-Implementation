# Overview
The Fast Fourier Transform (FFT) is an algorithm that computes the Discrete Fourier Transform (DFT) of a signal in O(nlogn) time. The algorithm to compute the DFT directly runs in O(n2) time (Chugg, 2021). The DFT calculates a signal’s frequency spectrum (ScienceDirect Topics). In other words, the DFT shows which frequencies occur in a signal. As such, in graphing the DFT, one can see which frequencies occur most often in a signal, a practical use of the DFT. As such, all of this can be done quicker with the FFT, considering its faster running time than the DFT. 

Although Python’s Numpy package includes a built in FFT function, we implemented the FFT function in Python. We compared our results with the built in FFT function in Numpy, verified that both runs in O(nlogn) time. Later, we used our FFT to analyze average daily temperature data for six major US cities.

# Usage
```diff
- To use the code, click the file 'FFT.py' and copy the code
```

# Content

- **Paper**, click the PDF file 'TeethSeg.pdf'
- **Main code**, click the jupyter notebook 'FFT.ipynb'

# Contact
Yuting Ji - jiyz@bc.edu
Scott Winters - wintersg@bc.edu
