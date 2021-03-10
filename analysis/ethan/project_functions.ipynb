{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "solid-father",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pylab as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "atmospheric-inflation",
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_and_process(url_or_path_to_csv_file):\n",
    "\n",
    "    # Method Chain 1 (Load data, deal with missing data, and make data readable)\n",
    "\n",
    "    df1 = (\n",
    "          pd.read_csv(url_or_path_to_csv_file)\n",
    "          .dropna()\n",
    "          .sort_values(\"alcohol\", ascending=False)\n",
    "          .sort_values(\"fixed acidity\", ascending=False)\n",
    "          .reset_index(drop=True)\n",
    "      )\n",
    "\n",
    "    # Method Chain 2 (Create new columns, drop others, and do processing)\n",
    "\n",
    "     df2 = (\n",
    "          df1\n",
    "          .rename(columns={\"free sulfur dioxide\": \"free SO2\"})\n",
    "          .rename(columns={\"total sulfur dioxide\": \"total SO2\"})\n",
    "          .assign(High_quality = lambda x: x['quality']>4)\n",
    "          .loc[df1['residual sugar']>15]\n",
    "      )\n",
    "\n",
    "    # Make sure to return the latest dataframe\n",
    "\n",
    "    return df2"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
