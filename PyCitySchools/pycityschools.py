{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ef5a758d",
   "metadata": {},
   "outputs": [],
   "source": [
    "PyCity Schools Analysis\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a56af38e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dependencies and Setup\n",
    "import pandas as pd   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "8afd98fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "# source data files \n",
    "schools_data_to_load = \"Resources/schools_complete.csv\"\n",
    "student_data_to_load = \"Resources/students_complete.csv\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "8d4be9cc",
   "metadata": {},
   "outputs": [],
   "source": [
    "schools_data = pd.read_csv(schools_data_to_load)\n",
    "student_data = pd.read_csv(student_data_to_load)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "890db58f",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Combine data \n",
    "school_data_full = pd.merge(student_data, school_data, how = 'left', on=)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
