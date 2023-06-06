"""
Baseline model.
"""

from sklearn.calibration import CalibratedClassifierCV
from sklearn.svm import LinearSVC


def build_model():
    return CalibratedClassifierCV(base_estimator=LinearSVC())
