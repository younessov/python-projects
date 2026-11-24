# Coin Classification Using OpenCV

## Overview

This project is a guided Python mini-project developed as part of a course followed through the **365 Data Science** learning platform.

The objective is to detect and classify coins in an image using classical computer vision techniques implemented with OpenCV and NumPy.

The program identifies circular objects, extracts basic visual features, classifies the detected coins using predefined rules, and estimates their total monetary value.

## Objectives

The main learning objectives are:

- Understand basic image processing techniques using OpenCV.
- Apply Gaussian Blur to reduce image noise.
- Detect circular objects using the Hough Circle Transform.
- Extract visual features from detected objects.
- Understand rule-based classification using geometric and intensity features.
- Manipulate image data and perform numerical calculations using NumPy.

## Technologies and Libraries

| Technology | Purpose |
|---|---|
| Python 3 | Programming language |
| OpenCV | Image processing and circle detection |
| NumPy | Numerical operations and image analysis |

## Methodology

The classification process consists of five main stages.

### 1. Image Loading and Preprocessing

The input image is loaded in grayscale for image analysis. A Gaussian Blur filter is applied to reduce noise and improve circle detection.

### 2. Circle Detection

The Hough Circle Transform (`cv2.HoughCircles`) is used to detect circular objects in the image.

For each detected circle, the algorithm extracts:
- X and Y coordinates of the center.
- Circle radius.

### 3. Feature Extraction

Two features are extracted for each detected coin:

- **Radius:** represents the approximate size of the coin.
- **Average Brightness:** calculated as the mean pixel intensity within a small region around the center of the detected coin.

### 4. Rule-Based Classification

The coins are classified using predefined thresholds based on their radius and average brightness.

The classification rules are:

| Average brightness | Radius | Predicted denomination |
|---|---|---|
| High (> 150) | Large (> 110) | 10p |
| High (> 150) | Small (≤ 110) | 5p |
| Low (< 150) | Large (> 110) | 2p |
| Low (< 150) | Small (< 110) | 1p |

These thresholds are heuristic values selected for the input image and are not learned from a training dataset.

### 5. Visualization and Total Value Estimation

The detected circles are drawn on the original image.

Each detected coin is annotated with its predicted denomination. Finally, the estimated total monetary value is calculated and displayed.

## Project Structure

```text
coin-classification/
├── coin_classification.py
├── README.md
├── requirements.txt
└── assets/
    └── capstone_coins.png
```

## Installation

Clone the repository:

```bash
git clone https://github.com/younessov/python-projects.git
cd python-projects
```

Install the required dependencies:

```bash
pip install -r 04-libraries/opencv/mini-projects/coin-classification/requirements.txt
```

## Execution

Run the program from the repository root:

```bash
python 04-libraries/opencv/mini-projects/coin-classification/coin_classification.py
```

The program displays the original image with detected circles, predicted denominations, and the estimated total value.

**Note:** The implementation requires a graphical environment because it uses `cv2.imshow()` to display the result.

## Limitations

This project is an introductory demonstration of classical computer vision and rule-based classification.

Its main limitations include:

- Classification depends on manually defined radius and brightness thresholds.
- Detection performance depends on image quality, lighting conditions, and coin positioning.
- The classification rules are specific to the characteristics of the input image and coin set.
- The algorithm does not use machine learning or a trained classification model.
- The implementation does not guarantee reliable classification on arbitrary coin images.

## Learning Context and Attribution

This mini-project was completed as a guided practical exercise while following a course on the 365 Data Science learning platform.

The implementation was studied, executed, tested, and examined step by step to understand the purpose and behavior of its main instructions and image-processing operations.

It is included in this repository as part of my Python learning journey and practical exploration of computer vision.


