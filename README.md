# BERTopic Analysis of TikTok Hashtag Replication Data

## Overview

This repository contains an overview of the complete pipeline for topic modeling of TikTok hashtag data using BERTopic in What’s on Their For You Page? A Large-Scale Computational Approach to Analyzing Adolescents’ TikTok Archives Through Hashtag Topic Modeling.

## Features

- Preprocessing TikTok hashtags for topic modeling
- Two-stage BERTopic modeling for topic discovery
- Topic merging and hierarchical categorization based on human labels
- Quantitative & qualitative evaluation (coherence, diversity metrics)
- Manual coding sheets

## Note on sensitive data

This repository only functions as a resource to review outputs and scripts that were run to produce results of What’s on Their For You Page?.

Output and files that contained sensitive data were erased/removed. Notebooks are retained for inspection, and can only be reproduced by researchers who hold the sensitive data files or are reproduced with your own data.

## Want to model your own data?

Please refer to our [repository for a reusable pipeline](https://github.com/Project-AWeSoMe-UvA/BERTopicReusablePipelineAwesome), where you can supply and easily model your own data!

## Installation of this project

### Prerequisites Fuzzy Matching (Script 0)

- An SQLite tiktok_database.db file
- Python 3.11, PyArrow downgraded to v20.0

### Prerequisites BERTopic (Script 1-4)

- Python 3.10.18
- CUDA-capable GPU (recommended: NVIDIA GeForce RTX 3070 Ti)
- Miniconda

### Setup

```bash
# Create conda environment for fuzzy matching (Script 0)
conda env create -f fuzzy_environment.yml
conda activate fuzzy_environment

# Create conda environment for BERTopic (Script 1-4)
conda env create -f tiktok_gpu.yml
conda activate tiktok_gpu
```

## Project Structure

```
.
├── README.md
├── fuzzy_environment.yml                        # Conda environment for Script 0
├── tiktok_gpu.yml                               # Conda environment for Script 1-4
├── config.py                                    # Configuration file
├── 0_fuzzy_matching.ipnyb
├── 1_data_preparation.ipynb
├── 2_topic_modelling.ipynb
├── 3_topic_merging.ipynb
├── 4_output_exploration.ipynb
├── data preparation files/
│   ├── FYP_tags.txt                             # Hashtags that were removed from modeling
│   └── extracted_hashtags_anonymized.pkl        # Anonymized input data
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

0. Fuzzy Matching - Reduce hashtag noise via fuzzy matching
1. Data Preparation - TikTok hashtag data preparatio
2. Topic Modelling - BERTopic modeling
3. Topic Merging - Merge main and outlier model topics, recalculate counts and apply manually created topic labels
4. Output Exploration - Quantitatively & qualitatively explore output

## Results

This pipeline produced:

- Fuzzy-matched hashtag variants
- Trained BERTopic models
- Topic assignments for all documents
- Readable excel sheets about topics and their document counts
- Quantitative & qualitative evaluation metrics

## License

Apache 2.0

## Citation

If you use this code in your research, please cite:

```bibtex
@article{
  title={What’s on Their For You Page? A Large-Scale Computational Approach to Analyzing Adolescents’ TikTok Archives Through Hashtag Topic Modeling},
  author={van der Wal, Amber and Vondenhof, Inga and Mikalauskas, Konrad, and Godard, Rebecca and Zioni, Kfir and Loecherbach, Felicia and Beyens, Ine},
  journal={Computational Communication Research},
  year={2026}
}
```

## Acknowledgments

- BERTopic library by Maarten Grootendorst
- Sentence Transformers

## Contact

- project-awesome-bb@uva.nl
- Project Link: https://project-awesome.nl/
