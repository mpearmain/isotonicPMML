# Sklearn Isotonic Regression to PMML
A simple implementation to convert python sklearn IsotonicRegression to PMML.

## Motivation
There are a few great libraries on github for converting sklearn models to pmml code (https://github.com/jpmml/sklearn2pmml)

This repo is missing the ability to convert isotonic regressions into pmml.  

This repo aims to solve that problem.

# Example
A quick example can be found in `example_isotonicPMML.py` which uses the example (http://scikit-learn.org/stable/auto_examples/plot_isotonic_regression.html#example-plot-isotonic-regression-py) from sklearn to create an isotonic regression that can be converted to PMML.

## Production use.
This repo solves the sklearn to pmml problem for isotonic regression, but does not solve the engine to run the code in, (say) a production environment.
An open license C++ implementation for this problem can be found at the freepmml repo: https://github.com/freepmml/libpmml
