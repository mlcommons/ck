import pandas as pd
import argparse
import os


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Sample test dataset from the original dataset.")
    parser.add_argument(
        '--dataset-path',
        required=True,
        help="Path to the input dataset (pickle file).")
    parser.add_argument(
        '--output-path',
        default=os.path.join(
            os.getcwd(),
            "mixtral-test-dataset.pkl"),
        help="Path to save the output dataset (pickle file).")
    parser.add_argument(
        '--samples',
        default=2,
        help="Number of entries to be extracted from each group.")

    args = parser.parse_args()
    dataset_path = args.dataset_path
    output_path = args.output_path
    no_of_samples = int(args.samples)

    try:
        # Load the dataset from the specified pickle file
        print(f"Loading dataset from {dataset_path}...")
        df = pd.read_pickle(dataset_path)

        # Check if 'group' column exists
        if 'dataset' not in df.columns:
            raise ValueError(
                "The input dataset must contain a 'dataset' column to identify data set groups.")

        # Sample 2 entries from each group
        print(f"Sampling {no_of_samples} entries from each group...")
        sampled_df = df.groupby('dataset').apply(
            lambda x: x.sample(
                n=no_of_samples)).reset_index(
            drop=True)

        # Save the sampled dataset to the specified output path
        print(f"Saving the sampled dataset to {output_path}...")
        sampled_df.to_pickle(output_path)

        print("Dataset processing and saving completed successfully!")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)


if __name__ == '__main__':
    main()
