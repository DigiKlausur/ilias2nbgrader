[![Build Status](https://travis-ci.org/DigiKlausur/ilias2nbgrader.svg?branch=master)](https://travis-ci.org/DigiKlausur/ilias2nbgrader)
[![Sonar Status](https://sonarcloud.io/api/project_badges/measure?project=DigiKlausur_ilias2nbgrader&metric=alert_status)](https://sonarcloud.io/dashboard?id=DigiKlausur_ilias2nbgrader)
[![Sonar Coverage](https://sonarcloud.io/api/project_badges/measure?project=DigiKlausur_ilias2nbgrader&metric=coverage)](https://sonarcloud.io/dashboard?id=DigiKlausur_ilias2nbgrader)

# ilias2nbgrader
Exchange between Ilias and Nbgrader

## Installation

Install via:

```pip install ilias2nbgrader```

## What does this tool do?

This tool provides functionality to import submissions from ILIAS to Nbgrader and to extract feedback from Nbgrader to ILIAS. This tool needs the following feature (available from ILIAS version 4.4):

https://docu.ilias.de/goto.php?target=wiki_1357_Upload_all_Feedback-Files_as_one_zip-archive

## How does it work?

### Importing submissions from ILIAS

You download a multiple submission archive (zip) and import it to Nbgrader via the ```SubmissionConverter```.

Example usage:
Suppose you have your Nbgrader course directory under ```test_course``` with the assignment ```assignment_1```:

```
test_course
├── source
│   └── assignment_1
│       ├── ps1.ipynb
│       └── data
│           └── dataset.csv
└── submitted
```
To import the multi-submission archive (e.g. ```submission_assignment1.zip```) from ILIAS, you download it and execute the ```SubmissionConverter``` the following way:

```
from ilias2nbgrader import SubmissionConverter
converter = SubmissionConverter()
resources = {
  'course_dir': 'test_course',                    # The path to the root dir of the course
  'assignment': 'assignment_1',                   # The name of the assignment
  'submission_zip': 'submission_assignment1.zip', # The path to the submission zip
  'path': 'tmp'                                   # The path to the temporary folder used for extracting
}
converter.convert(resources)
```

The converter will now go through the following stages:

1. ExtractAssignmentInfo - This will get the names of the notebooks and files in the assignment
2. Extract - Extract the submission zip to the temporary folder
3. CreateFolderStructure - Move single submissions to a subfolder named like the assignment
4. RenameNotebooks - Look for Jupyter notebooks in the submission and rename them if they aren't named correctly
5. AddExtraFiles - Copy additional files from the source assignment to the submissions (e.g. dataset.csv)
6. RestructureSubmission - Look into the code cells of the submitted notebooks and check under which relative path files are imported, move them to the corresponding relative paths
7. MoveToSubmitted - Move all submissions to the submitted folder of the course directory
8. DeleteTempFolders - Delete all temporary folders

After importing submissions to Nbgrader you will find a file ```converter.log``` that has information about the changes applied to the submission.

An example would be:
```
# File converter.log
[Create Folder Structure INFO] Moved submission to subfolder assignment_1
[Rename Notebooks INFO] Student_xyz: Rename ps1_1.ipynb to ps1.ipynb
[Add Extra Files INFO] Copied dataset.csv to data/dataset.csv
[Restructure Submission INFO] Moved data/dataset.csv to dataset.csv
```

In this example the student ```Student_xyz``` submitted an incorrectly named notebook (```ps_1.ipynb```) that got renamed. The additional file ```dataset.csv``` from the source assignment was copied over. Finally the notebook was analyzed to find out that the student loaded the dataset from the base folder instead of the subfolder ```data```, so the file ```dataset.csv``` was moved to the basefolder.

### Exporting feedback files to ILIAS

To export feedback back to ILIAS, you need to download the empty multi_feedback archive from ILIAS.

Then feedback can be exported the following way:

```
from ilias2nbgrader import FeedbackConverter
converter = FeedbackConverter()
resources = {
  'course_dir': 'test_course',                      # The path to the root dir of the course
  'assignment': 'assignment_1',                     # The name of the assignment
  'feedback_zip': 'multi_feedback_assignment1.zip', # The path to the empty feedback zip
  'path': 'tmp_feedback'                            # The path to the temporary folder used for extracting
}
converter.convert(resources)
```

Then you will find a feedback archive in the folder under ```path``` with the feedback in it. This archive can then be uploaded back to ILIAS to distribute the feedback for all students.

The feedback converter will go through the following stages:

1. ExtractAssignmentInfo - This will get the names of the notebooks to find the corresponding feedback html files
2. ExtractFeedback - Extract the empty feedback zip from ILIAS 
3. CopyFeedback - Copy over the html feedback files from Nbgrader
4. ZipFeedback - Create the feedback archive to upload to ILIAS
5. DeleteTempFolders - Delete all temporary folders

## Creating custom converters

In some cases you might want to disable some preprocessing steps or create your own custom pipeline for converting.
This can be done the following way:

```
from ilias2nbgrader.converters import Converter
from ilias2nbgrader.preprocessors import ExtractAssignmentInfo, Extract, \
  CreateFolderStructure, MoveToSubmitted, DeleteTempFolders

myconverter = Converter()
myconverter.preprocessors = [ExtractAssignmentInfo, Extract, CreateFolderStructure, \
                             MoveToSubmitted, DeleteTempFolders]
myconverter.init_preprocessors()

resources = ...

myconverter.convert(resources)
```
