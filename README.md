# BERTopic Analysis of TikTok Hashtag Data

## Overview
This repository contains a complete pipeline for topic modeling of TikTok hashtag data using BERTopic. The project processes ~5.3 million TikTok videos, extracts topics from hashtag patterns, and provides tools for topic validation and analysis.

## Features
- Preprocessing pipeline for TikTok hashtag data
- Two-stage BERTopic modeling (main + outlier processing)
- Topic merging and hierarchical categorization
- Quantitative evaluation (coherence, diversity metrics)
- Qualitative / manual coding sheets

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
├── tiktok_gpu.yml                               # Conda environment for Script 1-5
├── config.py                                    # Configuration file
├── 0_fuzzy_matching.ipnyb
├── 1_data_preparation.ipynb
├── 2_topic_modelling.ipynb
├── 3_topic_merging.ipynb
├── 4_topic_coherence.ipynb
│── 5_output_exploration.ipynb
├── data preparation files/
│   ├── FYP_tags.txt                             # Excluded tags
│   ├── hashtag_df_no_FYP.pkl                    # Preprocessed DataFrame
│   └── extracted_hashtags_anonymized.pkl        # Input data
├── documents/
│   ├── docs_bert_final.pkl                      # Final input documents for BERT
│   └── outlier_docs_bert_final.pkl              # Outlier documents from initial BERT run
├── manual coding/
│   ├── Final topics IDs.xlsx                    # Full manual coding sheet for categories & topics with IDs and top hashtags
|   └── Incoherent topics IDs.xlsx               # List of topic IDs that were manually coded as "incoherent"
├── topic info/
│   ├── category_counts.xlsx                     # Document counts for each category
│   ├── corrected_topic_info.xlsx                # Corrected topic info for main model
│   ├── corrected_topic_info_coutliers.xlsx      # Corrected topic info for outlier model
│   ├── merged_topic_info_with_categories.xlsx   # Final topic info table with merged topics, document counts & manual labels
|   └── topic_coherence_df.xlsx                  # All manually created topics including their coherence score and topic IDs
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

0. **Fuzzy Matching** - 
1. **Data Preparation** - Final TikTok hashtag data preparation (removing FYP tags)
2. **Topic Modelling** - Train BERTopic on 50k sample, apply to full dataset
3. **Topic Merging** - Merge main and outlier model topics and create counts and apply manually created topic labels
4. **Topic coherence** - Calculate coherence and diversity scores

## Configuration

Edit `config.py` to customize:
- Input/output paths

## Results

This pipeline produces:
- Fuzzy-matched hashtag variants
- Trained BERTopic models
- Topic assignments for all documents
- Readable excel sheets about topics and their document counts
- Quantitative evaluation metrics

## License

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0.txt)

## Citation

If you use this code in your research, please cite:
```bibtex
@article{yourname2024,
  title={Your Paper Title},
  author={Your Name},
  journal={Journal Name},
  year={2024}
}
```

## Acknowledgments

- BERTopic library by Maarten Grootendorst
- Sentence Transformers

## Contact

- Inga Vondenhof - i.k.vondenhof@uva.nl
- Project Link: https://github.com/yourusername/bertopic-tiktok