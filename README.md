# LibSVMConverter
Converts .csv files into LibSMV data format for machine learning purposes. Furthermore splits into train and test files can be performed for use in cross validation.

### Configuration
Before you start think of editing the `config.cfg` file. Edit how many folds do you prefer (in case of using the splitting functionality as well) and at which index the class label occur. The `LibSVMConverter` needs to know which i-th element in the .csv file is actually the class label.

### Usage - Converting only
If you just want to convert .csv files into LibSVM data format all you need to do is executing `LibSVMConverter.py`. The script assumes the data to convert being present in the `/data` folder and outputs the resulting files into `/output_lib_svm/original`.

### Usage - Converting and splitting
If you also want your newly created LibSVM data files to be split in `n` folds you can execute the `Run.py` which will output the train and test files into `/output_buckets/folder_name`. 

### Example data
The project contains some sample data in the `data` folder to start with. Note that the class label, i.e. the target variable to predict for, is the 7th element in each row, so you need to write 6 into the config file.
