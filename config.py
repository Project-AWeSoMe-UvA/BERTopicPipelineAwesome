"""Configuration file for BERTopic project"""
from pathlib import Path

# Project root
PROJECT_ROOT = Path.cwd()

# =============================================================================
# DIRECTORIES
# =============================================================================
DB_DIR = PROJECT_ROOT / "database"
DATA_PREP_DIR = PROJECT_ROOT / "data preparation files"
DOCUMENTS_DIR = PROJECT_ROOT / "documents"
TOPIC_MODELLING_FILES_DIR = PROJECT_ROOT / "topic modelling files"
TOPIC_MODEL_DIR = PROJECT_ROOT / "topic models"
TOPIC_INFO_DIR = PROJECT_ROOT / "topic info"
FIGURES_DIR = PROJECT_ROOT / "figures"

# =============================================================================
# DATABASE FILES
# =============================================================================
DB_PATH = DB_DIR / "tiktok_database.db"

# =============================================================================
# DATA PREPARATION FILES
# =============================================================================
HASHTAG_DF_PATH = DATA_PREP_DIR / "extracted_hashtags_anonymized.pkl"
FYP_TAGS_PATH = DATA_PREP_DIR / "FYP_tags.txt"
HASHTAG_DF_NOFYP_PATH = DATA_PREP_DIR / "hashtag_df_no_FYP.pkl"

# =============================================================================
# DOCUMENT FILES
# =============================================================================
FINAL_DOCS_PATH = DOCUMENTS_DIR / "docs_bert_final.pkl"
OUTLIER_DOCS_PATH = DOCUMENTS_DIR / "outlier_docs_bert_final.pkl"

# =============================================================================
# EMBEDDINGS
# =============================================================================
EMBEDDINGS_PATH = TOPIC_MODELLING_FILES_DIR / "final_embeddings.npy"
EMBED_TEST_PATH = TOPIC_MODELLING_FILES_DIR / "embedtest_results_df.pkl"

# =============================================================================
# GRID SEARCH FILES
# =============================================================================
CHECKPOINT_PATH_GRIDSEARCH = TOPIC_MODELLING_FILES_DIR / "bertopic_gridsearch_checkpoint.pkl"
FINAL_CSV_PATH_GRIDSEARCH = TOPIC_MODELLING_FILES_DIR / "bertopic_gridsearch_results.csv"

# =============================================================================
# TOPIC MODELS
# =============================================================================
TOPIC_MODEL_PATH = TOPIC_MODEL_DIR / "bertopic_model_final"
TOPICS_ASSIGNED_PATH = TOPIC_MODEL_DIR / "topics.npy"
OUTLIER_MODEL_PATH = TOPIC_MODEL_DIR / "bertopic_model_outliers"
OUTLIER_TOPICS_PATH = TOPIC_MODEL_DIR / "outlier_topics.npy"
MERGED_TOPICS_PATH = TOPIC_MODEL_DIR / "merged_topics.npy"

# =============================================================================
# TOPIC INFO FILES
# =============================================================================
CORRECTED_TOPIC_INFO_PATH = TOPIC_INFO_DIR / "corrected_topic_info.xlsx"
CORRECTED_OUTLIER_INFO_PATH = TOPIC_INFO_DIR / "corrected_topic_info_outliers.xlsx"
MERGED_TOPICS_CATEGORIES_PATH = TOPIC_INFO_DIR / "merged_topic_info_with_categories.xlsx"
CATEGORY_COUNT_PATH = TOPIC_INFO_DIR / "category_counts.xlsx"
TOPIC_COUNT_PATH = TOPIC_INFO_DIR / "topic_counts.xlsx"
TOPIC_COHERENCE_PATH = TOPIC_INFO_DIR / "topic_coherence_df.xlsx"

# =============================================================================
# FIGURES
# =============================================================================
COHERENCE_FIGURE_PATH = FIGURES_DIR / "topic_coherence_comparison.png"