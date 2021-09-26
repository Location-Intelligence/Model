# atms	banks	churches	gas_stations	hospitals	mosques	pharmacies	restaurants	schools	Males	Females	Children	Working	Elderly	rating	competitors

model = torch.load('classification_model.h5')
def predict(row, model):
    # convert row to data
    row = Tensor([row])
    # make prediction
    yhat = model(row)
    # retrieve numpy array
    yhat = yhat.detach().numpy()
    return yhat
test_values = torch.tensor([1,9,7,3,3,0,2,28,4,145225,163770,75491,225517,7987,20])
mean = pd.read_csv('mean.csv',header = None, index_col = 0, squeeze = True)
std = pd.read_csv('std.csv',header = None, index_col = 0, squeeze = True)
test_values=(test_values-mean)/std
rate = (5-argmax(predict(test_values, model)))
print(rate)