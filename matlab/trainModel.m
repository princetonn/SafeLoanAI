% Specify the file name
filename = 'german.data.txt';

% Read the data as a table
data = readtable(filename);
data.Properties.VariableNames{'Var21'} = 'Class';

% Splitting data
cv = cvpartition(size(data,1),'HoldOut',0.3);
idx = cv.test;

% Separate to training and test data
dataTrain = data(~idx,:);
dataTest  = data(idx,:);

% Predictor and Response
predictors = dataTrain(:, 1:20);
response = dataTrain.Class;
response = categorical(response);

% Preprocess data
for i = 1:width(predictors)
    if ~isnumeric(predictors.(i))
        predictors.(i) = categorical(predictors.(i));
    end
end

% False positive cost = 1.2, False negative cost = 1
costMatrix = [0 1; 5 0];

% Train a Random Forest
numTrees = 1000; % Specify the number of trees
randomForestModel = TreeBagger(numTrees, predictors, response, ...
    'Method', 'classification', 'OOBPredictorImportance', 'on', ...
    'PredictorSelection', 'curvature', ...
    'Cost', costMatrix);

% Save model
save('trainedModel.mat', 'randomForestModel');





