import numpy as np


def generate_dataset(target_mean, dataset_size):
    # Generate a dataset with random numbers between 0 and 100, and a set standard deviation of 10
    dataset = np.random.randint(0, 100, dataset_size)

    # Scale the dataset to achieve the target mean
    # scaled_dataset = dataset - np.mean(dataset)
    scaled_dataset = dataset * (target_mean / np.mean(dataset))

    return scaled_dataset


# Set the desired average and dataset size
target_mean = [90, 25, 50, 57, 30, 64, 91, 5, 35, 7, 45, 85, 65, 67, 79, 62, 64, 81]
dataset_size = 20

result_datasets = []

# Generate the dataset
for mean in target_mean:
    generated_dataset = generate_dataset(mean, dataset_size)
    result_datasets.append(generated_dataset)
    print(generated_dataset)

survey_results = []
for i in range(len(result_datasets[0])):
    survey_i = []
    for dataset in result_datasets:
        survey_i.append(dataset[i])
    survey_results.append(survey_i)

for i in range(len(survey_results)):
    print("Person " + str(i+1) + ":", end=" ")
    # print the survey results, rounded to the nearest integer
    print([round(x) for x in survey_results[i]])

