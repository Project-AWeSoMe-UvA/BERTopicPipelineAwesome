# BERTopic Analysis of TikTok Hashtag Replication Data

## Overview

This repository contains a complete pipeline for topic modeling of TikTok hashtag data using BERTopic. The project processes ~5.3 million TikTok videos, extracts topics from hashtag patterns, and provides tools for topic validation and analysis.

## Features

- Preprocessing pipeline for TikTok hashtag data
- Two-stage BERTopic modeling (main + outlier processing)
- Topic merging and hierarchical categorization
- Quantitative evaluation (coherence, diversity metrics)
- Qualitative evaluation
- Manual coding sheets

## Anonymization note

Please note that the notebooks below will only reproduce some outputs if certain, sensitive files are saved in the directory, and those files are missing because sensitive data files cannot be shared publicly.
Within the notebooks, original output that contains sensitive data was erased, and some outputs are retained only for inspections, and can only be reproduced by researchers who hold the sensitive data files or are reproduced with your own data.

## Installation

### Prerequisites Fuzzy Matching (Script 0)

- An SQLite `tiktok_database.db` file
- Python 3.11, PyArrow downgraded to v20.0

### Prerequisites BERTopic (Script 1-5)

- Python 3.10.18
- CUDA-capable GPU (recommended: NVIDIA GeForce RTX 3070 Ti)
- Miniconda

### Setup

```bash
# Create conda environment for fuzzy matching (Script 0)
conda env create -f fuzzy_environment.yml
conda activate fuzzy_environment

# Create conda environment for BERTopic (Script 1-5)
conda env create -f tiktok_gpu.yml
conda activate tiktok_gpu
```

## Project Structure

```
.
├── README.md
├── tiktok_gpu.yml                               # Conda environment for Script 1-4
├── config.py                                    # Configuration file
├── 0_fuzzy_matching.ipnyb
├── 1_data_preparation.ipynb
├── 2_topic_modelling.ipynb
├── 3_topic_merging_and_counts.ipynb
│── 4_output_exploration.ipynb
├── data preparation files/
│   ├── FYP_tags.txt                             # Excluded meta-referencing tags
│   ├── hashtag_df_no_FYP.pkl                    # Preprocessed DataFrame
│   └── extracted_hashtags_anonymized.pkl        # Input data
├── documents/
│   ├── docs_bert_final.pkl                      # Input documents
│   └── outlier_docs_bert_final.pkl              # Outlier documents
├── manual coding/
│   ├── Final topics IDs.xlsx                    # Full manual coding sheet for categories & topics with IDs and top hashtags
|   └── Incoherent topics IDs.xlsx               # List of topic IDs that were manually coded as "incoherent"
├── topic info/
│   ├── category_counts.xlsx                     # Document counts for each category
│   ├── corrected_topic_info.xlsx                # Corrected topic info for main model
│   ├── corrected_topic_info_outliers.xlsx       # Corrected topic info for outlier model
│   ├── merged_topic_info_with_categories.xlsx   # Final topic info table with merged topics, document counts & manual labels
|   └── topic_coherence_df.xlsx                  # All manually labelled topics including their coherence score and topic IDs
├── topic modelling files/
│   ├── bertopic_gridsearch_results.csv          # Hyperparameter gridsearch results
|   └── embedtest_results_df.pkl                 # Embedding model comparison test results 
└── topic models/                         
    ├── bertopic_model_final                     # BERTopic model file (initial run)
    ├── bertopic_model_outliers                  # BERTopic model file (outlier run)   
    ├── merged_topics.npy                        # Merged topics numpy array
    ├── outlier_topics.npy                       # Outlier topics numpy array
    └── topics.npy                               # Main model topics numpy array
```

## Workflow

1. **Fuzzy Matching** - Reduce hashtag noise via fuzzy matching
2. **Data Preparation** - Final TikTok hashtag data preparation (normalization & removing FYP tags)
3. **Topic Modelling** - Train BERTopic on sample, apply to full dataset
4. **Topic Merging** - Merge main and outlier model topics,recalculate counts and apply manually created topic labels
5. **Output Exploration** - Quantitatively & qualitatively explore output

## Configuration

Edit `config.py` to customize:

- Input/output paths

## Results

This pipeline produces:

- Fuzzy-matched hashtag variants
- Trained BERTopic models
- Topic assignments for all documents
- Readable excel sheets about topics and their document counts
- Quantitative & qualitative evaluation metrics

## License

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0.txt)

## Citation

If you use this code in your research, please cite:

```bibtex
@article{XXX,
  title={XXX},
  author={XXX},
  journal={XXX},
  year={2026}
}
```

## Acknowledgments

- BERTopic library by Maarten Grootendorst
- Sentence Transformers

## Contact

- XXX
- Project Link: XXXX\