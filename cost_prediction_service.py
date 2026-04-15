class CostPredictionService:
    def __init__(self, models, feature_importance_model):
        self.models = models  # A list of trained ML models
        self.feature_importance_model = feature_importance_model  # Model for importance analysis

    def predict_cost(self, features):
        predictions = [model.predict(features) for model in self.models]
        average_cost = sum(predictions) / len(predictions)
        return average_cost

    def calculate_cost_breakdown(self, features):
        # This will provide a breakdown of the cost components
        breakdown = {}  # Placeholder for breakdown logic
        return breakdown

    def analyze_feature_importance(self, features):
        importance = self.feature_importance_model.predict(features)
        return importance
