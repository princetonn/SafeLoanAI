function predictions = predictModel(inputTable)
    % Load the trained model
    loadedData = load('trainedModel.mat');
    RFModel = loadedData.randomForestModel;

    % Predict using the model
    predictions = predict(RFModel, inputTable);
end