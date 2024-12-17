% Predict labels on the test data
predictedLabels = predict(randomForestModel, dataTest(:, 1:20));
predictedLabels = categorical(predictedLabels);
trueLabels = categorical(dataTest.Class);

% Plot Confusion Matrix
figure;
confusionchart(trueLabels, predictedLabels);
title('Confusion Matrix for Test Data');

% Testing for Overfit
predictedLabelsTrain = predict(randomForestModel, dataTrain(:, 1:20));
predictedLabelsTrain = categorical(predictedLabelsTrain);
trueLabelsTrain = categorical(dataTrain.Class);

figure;
confusionchart(trueLabelsTrain, predictedLabelsTrain);
title('Confusion Matrix for Train Data');

% Optionally, save the confusion matrix as an image
saveas(gcf, 'confusion_matrix_train.png');

% Plot Feature Importance
figure;
bar(randomForestModel.OOBPermutedVarDeltaError);
xlabel('Predictors');
ylabel('Feature Importance');
title('Out-of-Bag Predictor Importance');

% Save the Feature Importance Plot as an Image
saveas(gcf, 'feature_importance.png'); % Saves as PNG